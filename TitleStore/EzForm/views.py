
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpRequest, Http404, FileResponse

from django.template import loader

from django.shortcuts import get_object_or_404, render
from .models import Customer, Vehicle, AcctForm

from django.db import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView

import json
import os

from .acct_form_filler import makePdf as acct_pdf_maker

# dashboard view
def index(request):
    return render(request, 'EzForm/index.html')

# customer list view
def customers(request):
    all_customers = Customer.objects.order_by('cu_last_name')
    context = {'customer_list' : all_customers }
    return render(request, 'EzForm/customers.html', context)

# vehicle list view
def vehicles(request):
    all_vehicles = Vehicle.objects.order_by('Customer')
    context = {'vehicle_list' : all_vehicles }
    return render(request, 'EzForm/vehicles.html', context)



def customer_review(request):
    if request.method == 'GET':
        template = loader.get_template('EzForm/formReview.html')
        context = {
            'customers': []
        }
        customers_on_file = Customer.objects.filter()
        for customer in customers_on_file:
            context['customers'].append(customer.cu_last_name + ', ' + customer.cu_first_name)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(customer_review, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['vehicle_list'] = Vehicle.objects.all()
        return context

    return HttpResponse(template.render(context, request))

def forms(request):
    return render(request, 'EzForm/forms.html')

def customer_info_to_review(request, cu_name):
    dataToSendToClient = {}
    customer_query = cu_name.split(', ')

    cu_last_name = customer_query[0]
    cu_first_name = customer_query[1]
    customers_on_file = Customer.objects.get(cu_last_name=cu_last_name, cu_first_name=cu_first_name)
    customer_file = customers_on_file.__dict__


    for key in customer_file:
        if key != '_state':
            dataToSendToClient[key] = customer_file[key]

    vehicle_on_file = Vehicle.objects.get(Customer=customer_file['id'])
    vehicle_file = vehicle_on_file.__dict__
    for key in vehicle_file:
        if key != '_state':
            dataToSendToClient[key] = vehicle_file[key]



    response = JsonResponse(dataToSendToClient)
    return response


class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/customers/'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = '/customers/'

class CustomerUpdate(UpdateView):
    model = Customer

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CustomerUpdate, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['vehicle_list'] = Vehicle.objects.all()
        return context

    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/customers/'

class VehicleCreate(CreateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_create_form'
    success_url = '/vehicles/'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = '/vehicles/'

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/vehicles/'

class AcctFormCreate(CreateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_create_form'

class AcctFormDelete(DeleteView):
    model = AcctForm
    success_url = 'index' # check for correct url

class AcctFormUpdate(UpdateView):
    model = AcctForm
    fields = '__all__'
    template_name_suffix = '_update_form'

def makeAcctPdf(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        c_id = body['id']
        for key in body:
            stringToBool(body, key)

        updateCustomer = {}
        updateVehicle = {}
        for customerKey in body:
            updateCustomer[customerKey] = body[customerKey]
            if customerKey == 'cu_flag_military':
                break

        for vehicleKey in body:
            if vehicleKey not in updateCustomer:
                updateVehicle[vehicleKey] = body[vehicleKey]

        print(updateCustomer)
        print(updateVehicle)

        #TODO: redirect user to PDF page
        try:
             # Overlay pdf dumped to prevent same info from being copied
            if os.path.exists('overlay_PDF.pdf'):
                os.remove('overlay_PDF.pdf')
            acct_pdf_maker(data=body) # sends POST data to make pdf
            customer = Customer.objects.filter(id=c_id).update(**updateCustomer)

        except (RuntimeError, TypeError, NameError):
            return JsonResponse({'errorMessage': 'There was no record found matching the customer id: ' + c_id + ' please try again.'})

        return pdf_view()
    else:
        return Http404()

def stringToBool(data, key):
    options = ('true', 'false', 'null')
    if data[key] in options:
        data[key] = bool(data[key])
        print(data[key], type(data[key]))


    # pdf should be already made when this is called
def pdf_view():
    try:
        return FileResponse(open('result_form.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
