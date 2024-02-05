from django.db import models

# Create your models here.

class Items(models.Model):
    category=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='product',blank=True,null=True)
    stock=models.IntegerField()
    availability=models.BooleanField(default=True)
    last_update=models.DateTimeField(auto_now=True)
    create_time=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Items,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


