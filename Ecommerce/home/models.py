from django.db import models
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home:category_filter", args=[self.slug,])
    


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home:product_detail", args=[self.slug,])
    
    
    