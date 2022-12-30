from django.db import models
from django.utils.translation import gettext_lazy as _

class ShoppingItem(models.Model):

    class Position(models.TextChoices):
        IRGENDWO = '0', _('0_Irgendwo')
        OBST = '1', _('1_Obst')
        KÄSE = '2', _('2_Käse')
        JOGHURT = '3', _('3_Joghurt')
        NUDELN = '4', _('4_Nudeln')
        GETRÄNKE = '5', _('5_Getränke')
        
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=2, choices=Position.choices, default=Position.IRGENDWO)

    def __str__(self):
        return self.name + ', pos:' + self.position


class ShoppingListItem(models.Model):
    shopping_item = models.ForeignKey(ShoppingItem, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.shopping_item) + ', done:' + str(self.done)
