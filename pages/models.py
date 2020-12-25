from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGOREY = (
        ('Indoor', 'Indoor'),
       
        ('Out Door', 'Out Door'),
    )
    color = (
        ('new', 'new'),
        ('sold', 'sold'),
        ('offer', 'offer'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    categorey = models.CharField(max_length=200, null=True, choices=CATEGOREY)
    feature = models.CharField(max_length=200,null=True,choices=color)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    images = models.ImageField(null=True, upload_to='photos/%Y/%m/%d')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('out of delivery', 'out of delivery'), 
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    


