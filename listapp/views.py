from django.shortcuts import render
from .models import ShoppingItem
from .models import ShoppingListItem
import json

def listapp(request):
    if request.method == 'POST':
        print('received data:', request.POST['itemName'])
        new_shopping_item = ShoppingItem.objects.create(name=request.POST['itemName'])
        ShoppingListItem.objects.create(shopping_item=new_shopping_item)
    elif request.method == 'PUT':
        request_body = json.loads(request.body.decode('utf-8'))
        print(request_body['itemName'])
        item = ShoppingListItem.objects.get(shopping_item__name=request_body['itemName'])
        item.done = not item.done
        item.save()
    all_items = ShoppingListItem.objects.all()
    return render(request, 'list.html', {'all_items': all_items})
    