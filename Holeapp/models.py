from django.db import models
from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    head_quater=models.CharField(max_length=40)
    logo=models.ImageField(upload_to='logos',blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
     return reverse("company_list", kwargs={'pk': self.pk})

    

class Product(models.Model):
    prod_name=models.CharField(max_length=100)
    color=models.CharField(max_length=20)
    price=models.IntegerField()
    est_year=models.IntegerField()
    milage=models.IntegerField()
    prod_img=models.ImageField(upload_to="photos",blank=True,null=True)
    advantage=models.CharField(max_length=1000,null=True)
    name=models.ForeignKey(Company,related_name="campany",on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name
    
