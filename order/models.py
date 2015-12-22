from django.db import models

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
    modified_at_time = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    order_type = models.CharField(max_length=10,blank=True,null=True)
    special_instructions = models.CharField(max_length=200,blank=True,null=True)
    p_id = models.IntegerField(blank=True,null=True)

    delivery_id = models.CharField(max_length=200, blank=True, null=True)
    roadrunner_order_id = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

class DriverDetails(models.Model):
    orders = models.ForeignKey(orders)
    id = models.AutoField(primary_key=True)
    driver_phone = models.CharField(max_length=20,blank=True,null=True)
    order_id = models.CharField(max_length=20,blank=True,null=True)
    delivery_id = models.CharField(max_length=20,blank=True,null=True)
    new_trip = models.BooleanField(blank=True)
    driver_name = models.CharField(max_length=20,blank=True,null=True)

#medium small or large
class Size(models.Model):
    size_id = models.AutoField(primary_key=True)
    size_name = models.CharField(max_length=10)

    def __unicode__(self):
        return unicode(self.size_name)

#shirt or pant
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=10)

    def __unicode__(self):
        return unicode(self.type_name)
#blue green etc
class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    color_name = models.CharField(max_length=10)
    def __unicode__(self):
        return unicode(self.color_name)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=10)
    def __unicode__(self):
        return unicode(self.brand_name)

class ClothInfo(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(orders,related_name='ClothInfo')
    size = models.ForeignKey(Size)
    type = models.ForeignKey(Type)
    color = models.ForeignKey(Color)
    brand = models.ForeignKey(Brand,null=True)
    gender = models.CharField(max_length=7)
    damage = models.BooleanField(default=False)

