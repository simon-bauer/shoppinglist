from django.shortcuts import render
from .models import ShoppingItem
from .models import ShoppingListItem
import json

def listapp(request):
    if request.method == 'POST':
        item_name = request.POST['itemName']
        print('add item with name: ', item_name)
        
        items = ShoppingListItem.objects.filter(shopping_item__name=item_name)
        if len(items) > 0:
            print('Item already in ShoppingList. Do Nothing.')
            pass
        else:
            items = ShoppingItem.objects.filter(name=item_name)
            if len(items) > 0:
                print('ShoppingItem already exist, reuse it.')
                new_shopping_item = items[0]
            else:
                print('Create Shopping Item')
                new_shopping_item = ShoppingItem.objects.create(name=item_name)
            ShoppingListItem.objects.create(shopping_item=new_shopping_item)
    elif request.method == 'PUT':
        request_body = json.loads(request.body.decode('utf-8'))
        print(request_body['itemName'])
        for item in ShoppingListItem.objects.filter(shopping_item__name=request_body['itemName']):
            item.done = not item.done
            item.save()
    elif request.method == 'DELETE':
        for item in ShoppingListItem.objects.filter(done=True):
            item.delete()
        
    all_items = ShoppingListItem.objects.all().order_by('shopping_item__position', 'shopping_item__name')
    item_suggestions = ShoppingItem.objects.all()
    return render(request, 'list.html', {'all_items': all_items, 'item_suggestions': item_suggestions})
    