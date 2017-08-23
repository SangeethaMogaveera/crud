from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _

class Consultant(models.Model):
    consultant_name = models.CharField(max_length=100)
    consultant_type = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    consultant_address= models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email_id= models.CharField(max_length=100)
    bank_MICR_code= models.CharField(max_length=100)
    sales_tax_reg_no= models.IntegerField()
    vat_reg_no = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    branch_address= models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=200)
    tin_no= models.IntegerField()
    pan_no=models.CharField(max_length=100)
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
        return self.consultant_name

