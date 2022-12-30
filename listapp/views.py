from django.shortcuts import render
from .models import ShoppingItem
from .models import ShoppingListItem

def listapp(request):
    if request.method == 'POST':
        print('received data:', request.POST['itemName'])
        new_shopping_item = ShoppingItem.objects.create(name=request.POST['itemName'])
        ShoppingListItem.objects.create(shopping_item=new_shopping_item)
    all_items = ShoppingListItem.objects.all()
    return render(request, 'list.html', {'all_items': all_items})
    