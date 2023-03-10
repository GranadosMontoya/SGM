from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField(unique=True)
    amount = models.IntegerField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2,)

    def __str__(self):
        return self.name +'--'+str(self.code)

