from django.db import models

# Create your models here.

 # company info 
# product


class companyinformation(models.model):
    name = models.charfield(max_length=100)
    description = models.TextField()


class category(models.mode):
    name = models.CharField(max_length=100)

            

  
    class product(models.mode):
        product_name = models.CharField(max_length=100)
        description = models.TextField()
        category = models.ForeignKey(category, on_deleted =models.CASCAE)
