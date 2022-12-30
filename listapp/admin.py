from django.contrib import admin
from .models import ShoppingItem
from .models import ShoppingListItem

# Register your models here.
admin.site.register(ShoppingItem)
admin.site.register(ShoppingListItem)
