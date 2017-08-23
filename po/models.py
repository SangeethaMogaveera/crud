from django.db import models
#import datetime
from django.utils.translation import ugettext_lazy as _
from vendors import models as Vendor_models
from project import models as Project_models
from material import models as Material_models

class Po(models.Model):
    project = models.ForeignKey(Project_models.Project)
    vendor = models.ForeignKey(Vendor_models.Vendor)
    material = models.ManyToManyField(Material_models.Material)
    expected_date=models.DateField('expected_date',blank=True,null=True)
    comment= models.TextField(max_length=800)
    INACTIVE = False
    ACTIVE = True
    STATUS_CHOICHES=(
    ('or','Ordered'),
    ('in','In Progress'),
    ('par','Partial Delivered'),
    ('del','Delivered')
    )

    status=models.CharField(max_length=300,default=True,choices=STATUS_CHOICHES)

    #date = models.DateTimeField(default=datetime.datetime.now())

    # def __str__(self):
    #     return self.material




