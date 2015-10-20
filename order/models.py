from django.db import models

# Create your models here.
STATUS = (
    ('1', 'created'),
    ('2', 'wash'),
    ('3', 'dry'),
    ('4', 'iron'),
    ('5','complete')
)

class orders(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders')
    id = models.AutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)
    order_type = models.CharField(max_length=10,blank=True,null=True)
    special_instructions = models.CharField(max_length=200,blank=True,null=True)
    #roadrunner Details for order
    delivery_id = models.CharField(max_length=200, blank=True, null=True)
    roadrunner_order_id = models.CharField(max_length=200, blank=True, null=True)

