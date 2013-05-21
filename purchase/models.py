from django.db import models

class Pricing(models.Model):
    price = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.price)

class Purchase(models.Model):
    price = models.ManyToManyField(Pricing)

