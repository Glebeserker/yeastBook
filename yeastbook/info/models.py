from django.db import models

# Create your models here.
class YeastCompany(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self) -> str:
        return self.name
    
    def return_absolute_url(self):
        return f'/{self.slug}/'
    
class YeastType(models.Model):
    name = models.CharField(max_length= 180)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self) -> str:
        return self.name
    
    def return_absolute_url(self):
        return f'/{self.slug}/'
    
class Yeast(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField()
    gen_info = models.TextField()
    sec_info = models.TextField()
    company = models.ForeignKey(YeastCompany, related_name='yeasts', on_delete=models.CASCADE)
    yeast_type = models.ForeignKey(YeastType, related_name='yeastss',on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('id', )
        
    def __str__(self) -> str:
        return self.name
    
    def return_absolute_url(self):
        return f'/{self.slug}/'