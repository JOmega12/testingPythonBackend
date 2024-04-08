from django.contrib import admin
from .models import Item

# you import the model from models.py
admin.site.register(Item)