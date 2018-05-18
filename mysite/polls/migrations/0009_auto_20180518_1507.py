# Generated by Django 2.0.5 on 2018-05-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cu_photo_id_type',
            field=models.CharField(blank=True, choices=[('DRIVERS_LICENSE', "U.S. Driver's License/ID Card"), ('MILITARY_ID', 'U.S. Military ID'), ('DOJ_ID', 'U.S. Citizenship & Immigration Services/DOJ ID'), ('NATO_ID', 'NATO ID'), ('DOS_ID', 'U.S. Department of State ID')], default='DRIVERS_LICENSE', max_length=200, null=True, verbose_name='ID Type'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_address_line_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address Line 1'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_address_line_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_country',
            field=models.CharField(blank=True, default='USA', max_length=200, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_county',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_flag_military',
            field=models.NullBooleanField(verbose_name='Are you military personel stationed in Texas?'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_middle_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_phone_primary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_photo_id_state',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='ID State'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_state',
            field=models.CharField(blank=True, default='TX', max_length=2, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_suffix',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Suffix'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cu_zip',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_body_style',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Body Style'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_bond_request_explanation',
            field=models.TextField(blank=True, null=True, verbose_name='Provide an explanation for requesting a bonded title or tax assessor-collector hearing.'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_empty_weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Empty Weight'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_25_or_older',
            field=models.NullBooleanField(verbose_name='Is the vehicle 25 or more years old?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_abandoned',
            field=models.NullBooleanField(verbose_name='Is the vehicle an abandoned vehicle?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_assembled',
            field=models.NullBooleanField(verbose_name='Is the vehicle an assembled vehicle from new or used part(s) or a kit that has not been previously titled?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_complete',
            field=models.NullBooleanField(verbose_name='Is the vehicle complete?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_last_titled_in_tx',
            field=models.NullBooleanField(verbose_name='Was the vehicle last titled in Texas?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_legal_control',
            field=models.NullBooleanField(verbose_name='Are you in legal control of the vehicle?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_legal_posession',
            field=models.NullBooleanField(verbose_name='Are you in legal possession of the vehicle?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_manufactured_us',
            field=models.NullBooleanField(verbose_name='Was the vehicle manufactured for sale or distribution in the United States by a motor vehicle manufacturer?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_no_plates',
            field=models.CharField(blank=True, choices=[('HAS_PLATES', 'License plates and registration issued for this vehicle are being surrendered. The registration for this vehicle is not currently suspended or revoked.'), ('NO_PLATES', 'Vehicle has no license plates and/or registration.'), ('MIL_PLATES', 'Vehicle has been issued a license plate under the applicable status of forces agreement.')], max_length=200, null=True, verbose_name='Please select one:'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_nonrepairable',
            field=models.NullBooleanField(verbose_name='Is the vehicle a nonrepairable vehicle?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_pending_lawsuits',
            field=models.NullBooleanField(verbose_name='Is the vehicle involved in any pending lawsuits or disputes of ownership?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_salvage',
            field=models.NullBooleanField(verbose_name='Is the vehicle a salvage vehicle?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_subject_to_charges',
            field=models.NullBooleanField(verbose_name="Is the vehicle subject to storage or mechanic's charges?"),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_flag_subject_to_lien',
            field=models.NullBooleanField(verbose_name='Is the vehicle subject to any type of foreclosure lien?'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_lienholder_name_first',
            field=models.CharField(blank=True, default='N/A', max_length=200, null=True, verbose_name='Lienholder Name (First)'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_make',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_model',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_odometer_reading',
            field=models.IntegerField(blank=True, null=True, verbose_name='Odometer Reading'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_plate_number',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='License Plate Number'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_purchase_date',
            field=models.DateField(blank=True, null=True, verbose_name='Purchase Date'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_purchase_price_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Purchase Price (USD)'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_purchased_from_city',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='City Purchased From'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_purchased_from_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Seller Name'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_purchased_from_state',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='State Purchased From'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_seller_signature',
            field=models.CharField(blank=True, default='UNAVAILABLE', max_length=200, null=True, verbose_name='Seller Signature'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_vin',
            field=models.CharField(max_length=17, null=True, verbose_name='Vehicle Identification Number'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='v_year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True, verbose_name='Year'),
        ),
    ]