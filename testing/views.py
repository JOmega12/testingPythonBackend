from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer
from testing import serializers



# this is where you can create your endpoint

def item_list(request):
    #get all drinks
    #serialize them
    #return json

    items = Item.objects.all()
    ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)
