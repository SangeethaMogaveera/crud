from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _

class StatutoryRegistrations(models.Model):
    kst_no = models.CharField(max_length=100, default=None, null=True)
    cst_no = models.CharField(max_length=100, default=None, null=True)
    service_tax_no = models.CharField(max_length=100, default=None, null=True)
    esi_no = models.CharField(max_length=100, default=None, null=True)
    pf_no = models.CharField(max_length=100, default=None, null=True)
    income_tax_pan_number = models.CharField(max_length=100, default=None, null=True)
    work_contract_tax_number = models.CharField(max_length=100, default=None, null=True)


class ValidityOfLicences(models.Model):
    shops_and_establishments = models.CharField(max_length=200, default=None, null=True)
    contract_labour_act = models.CharField(max_length=200, default=None, null=True)
    others = models.CharField(max_length=500, default=None, null=True)


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    categories = (
        ('contractor','CONTRACTOR'),
        ('oem','OEM'),
        ('supplier','SUPPLIER')
    )
    vendor_type = models.CharField(max_length=200, choices=categories)
    description = models.TextField(max_length=800)
    client_name = models.CharField(max_length=300)
    client_alias = models.CharField(max_length=200)
    consultant_name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    validity_of_licences = models.OneToOneField(ValidityOfLicences, on_delete=models.CASCADE, null=True)
    year_of_establishment = models.IntegerField()
    name_of_the_propreiter = models.CharField(max_length=500,null=True)
    nature_of_services_offered = models.CharField(max_length=100)
    statutory_registrations = models.OneToOneField(StatutoryRegistrations, on_delete=models.CASCADE, null=True)
    previous_year_turnover = models.PositiveIntegerField(default=None)
    income_tax_paid_and_cleared_till = models.CharField(max_length=100, default=None)
    banker_details = models.CharField(max_length=200)
    contact_details = models.CharField(max_length=500)
    tin_no= models.CharField(max_length=100, default=None)
    pan_no=models.CharField(max_length=100,default=True)
    enabled=models.BooleanField(default=True)
    INACTIVE = False
    ACTIVE = True
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )

    state = models.BooleanField(max_length=100,default=True,choices=STATUS)
    date = models.DateTimeField(default=datetime.datetime.now())



    def __str__(self):
        return self.vendor_name

