from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    image = models.URLField()
    release_date = models.DateTimeField(null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(max_length=100, unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
