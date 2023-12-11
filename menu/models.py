from django.db import models

class Item(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default="http://www.energyfit.com.mk/wp-content/plugins/ap_background/images/default/default_1.png")
    