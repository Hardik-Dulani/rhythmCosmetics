from django.db import models

# Create your models here.
class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=5000,default="")
    desc2 = models.CharField(max_length=5000,default='')
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images/",default="")
    availabilty = models.IntegerField(default=1)
    directions = models.CharField(max_length=4000,default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, default="")
    query = models.CharField(max_length=400,default="")


    def __str__(self):
        return self.name
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=500)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email  = models.CharField(max_length=90)
    address =  models.CharField(max_length=180)
    city = models.CharField(max_length=90)
    state= models.CharField(max_length=90)
    zip_code = models.CharField(max_length=90)
    phone = models.CharField(max_length=13,default="")
    payment_ref =models.CharField(max_length=25,default='')
    payment_conf = models.IntegerField(default=0)
    dispatched = models.IntegerField(default=0)
    timestamp= models.DateField(auto_now_add= True)
    link = models.CharField(max_length=5000,default='nil')
    primary_prod = models.CharField(max_length=500,default='nil')
    def __str__(self):
        return self.name + str(self.order_id)


