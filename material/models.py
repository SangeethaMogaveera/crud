from __future__ import unicode_literals
from django.db import models
from brand import models as Brand_models


class Material(models.Model):


    brand_id = models.ForeignKey(Brand_models.Brand)
    name = models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


