from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    
    def __str__(self):
        return self.name
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default="http://www.energyfit.com.mk/wp-content/plugins/ap_background/images/default/default_1.png")
    
    def get_absolute_url(self):
        return reverse("menu:detail", kwargs={"pk": self.pk})
    