from django.db import models

# Create your models here.
STATUS = (
    ('0' , 'cancelled'),
    ('1', 'created'),
    ('2', 'wash'),
    ('3', 'dry'),
    ('4', 'iron'),
    ('5','processComplete'),
    ('6','shipRequest'),
    ('7','shipped'),
    ('8','completed')
)

class orders(models.Model):
    owner = models.ForeignKey('auth.User', related_name='orders')
    id = models.AutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True,null=True)
    weight = models.FloatField(blank=True,null=True)
    created_at_time = models.DateTimeField(auto_now_add=True, blank=True)

    status = models.CharField(max_length=1, choices=STATUS, default='1')
    order_type = models.CharField(max_length=10,blank=True,null=True)
    special_instructions = models.CharField(max_length=200,blank=True,null=True)
    p_id = models.IntegerField(blank=True,null=True)

    delivery_id = models.CharField(max_length=200, blank=True, null=True)
    roadrunner_order_id = models.CharField(max_length=200, blank=True, null=True)


#medium small or large
class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=10)

#shirt or pant
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=10)

#blue green etc
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=10)

class ClothInfo(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(orders)
    size = models.ForeignKey(Size)
    type = models.ForeignKey(Type)
    color = models.ForeignKey(Color)
    gender = models.CharField(max_length=7)