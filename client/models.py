from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_type = models.CharField(max_length=200)
    description= models.TextField(max_length=800)
    client_alias = models.CharField(max_length=500)
    client_address = models.CharField(max_length=500)
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
        return self.client_name
