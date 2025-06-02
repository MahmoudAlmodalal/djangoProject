from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    
    statas_book = [
        ('avalable', 'avalable'),
        ('rental', 'rental'),
        ('sold', 'sold')
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos',null=True,blank=True) 
    photo_author = models.ImageField(upload_to='photos',null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    retal_price_day = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    rental_peroid = models.IntegerField(null=True,blank=True)
    total_rental_price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    pages = models.IntegerField(null=True,blank=True)
    statas = models.CharField(max_length=50, choices=statas_book,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True,blank=True)

    def __str__(self):
        return self.title
