# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import people
# from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Customer, Vehicle, ACCTForm

from django.http import HttpRequest

from django.db import models
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# from .models import people

def index(request):
    return render(request, 'EzForm/index.html')

def customers(request):
    all_customers = Customer.objects.order_by('cu_last_name')
    context = {'customer_list' : all_customers }
    return render(request, 'EzForm/customers.html', context)

def vehicles(request):
    return render(request, 'EzForm/vehicles.html')



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
def detail(request):
    if request.method == 'GET':
        template = loader.get_template('EzForm/formReview.html')
        context = {
            'customers': []
        }
        customers_on_file = people.objects.filter()
        for customer in customers_on_file:
            context['customers'].append(customer.person_name)

        return HttpResponse(template.render(context, request))
        
def forms(request):
    return render(request, 'EzForm/forms.html')




class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'

class CustomerDelete(DeleteView):
    model = Customer
    success_url = 'index' # check for correct url

class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'


class VehicleCreate(UpdateView):
    model = Vehicle
    fields = '__all__'

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = 'index' # check for correct url

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = '__all__'