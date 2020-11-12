from django.db import models
from django.contrib.auth.models import User
    
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    company_name = models.CharField(max_length = 50,blank=True, null=True)
    company_id = models.EmailField(max_length = 50, blank=True, null=True)
    mobile_number = models.BigIntegerField(blank=True, null=True)
    services = models.CharField(max_length = 70, blank=True, null=True)
    description = models.CharField(max_length = 300, blank=True, null=True)
    # image = models.ImageField()

    class Meta:
        app_label = "partners"
        db_table = "Registration"

