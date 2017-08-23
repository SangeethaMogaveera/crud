from __future__ import unicode_literals
from django.db import models
#from category import models as Category_models
from subcategory import models as Subcategory_models




class Brand(models.Model):

    #cat_id= models.ForeignKey(Category_models.Category,on_delete=models.CASCADE)
    sub_cat_id = models.ForeignKey(Subcategory_models.Subcategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False,null=True)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name