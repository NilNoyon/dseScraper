from django.db import models

# Create your models here.
class DSE(models.Model):
    brand = models.CharField(max_length = 150, null=True)
    amount = models.IntegerField(null=True)
    status = models.IntegerField(null=True)
    old = models.CharField(max_length = 10, null=True)
    current = models.CharField(max_length = 10, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        db_table = 'dse'