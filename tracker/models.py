from django.db import models

decide = {
        ('pending', 'pending'),
        ('active', 'active'),
        ('delivered', 'delivered'),
        ('delayed', 'delayed'),
    }


class Tracker(models.Model):
    order_id = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    order_address = models.CharField(max_length=100)
    order_destination = models.CharField(max_length=100)
    order_email_address = models.CharField(max_length=100)
    order_phone_phone_number = models.CharField(max_length=100)
    order_content = models.CharField(max_length=100, default='empty')
    order_status = models.CharField(max_length=100, choices=decide, default=1)
    order_progress  = models.IntegerField(blank=True, null=True, default=1)
    

def __str__():
    return self.order_id

    