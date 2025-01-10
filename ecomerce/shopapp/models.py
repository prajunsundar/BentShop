from django.db import models
from django.shortcuts import reverse


GENDER_CHOICES=(
    ('M','men'),
    ('W','women'),
    ('K','kids')
)

PRODUCT_CHOICES=(
    ('C','cloths'),
    ('F','footwear'),
)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='product_image',blank=True)
    gender=models.CharField(max_length=200,choices=GENDER_CHOICES)
    product_type=models.CharField(max_length=200,choices=PRODUCT_CHOICES)
    slug=models.SlugField(max_length=250,unique=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)






    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shopapp:single-product',args=[self.slug])


    
