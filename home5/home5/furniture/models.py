from django.db import models
import django_filters




class Furniture(models.Model):
    oder_number = models.CharField("Номер заказа", max_length = 50)
    material = models.CharField("Наиминование", max_length = 50)
    size = models.CharField("Размер", max_length = 50)
    oder_date = models.DateTimeField("Дата заказа")
    delivery_date = models.DateTimeField("Дата сдачи")
    sn_number = models.CharField("SN", max_length = 50)
    status = models.CharField("Статус", max_length = 50)
    
    
    def __str__(self):
        return self.oder_number


