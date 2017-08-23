from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from  client import models as Client_models
from  consultant import models as Consultant_models


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    site_address = models.CharField(max_length=100)
    construction_place = models.CharField(max_length=100)
    survey_no = models.CharField(max_length=100)
    enabled=models.BooleanField(default=True)
    client = models.ForeignKey(Client_models.Client)
    consultant = models.ForeignKey(Consultant_models.Consultant)
    INACTIVE = False
    ACTIVE = True
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )

    state = models.BooleanField(max_length=100,default=True,choices=STATUS)
    date = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.project_name

