from django.contrib import admin
from .models import Message, Representative, Conversation

# Register your models here.

admin.site.register([Message, Representative, Conversation])