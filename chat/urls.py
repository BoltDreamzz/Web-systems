# urls.py

from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    # path('choose-representative/', views.choose_representative, name='choose_representative'),
    path('send-message/<int:representative_id>/', views.send_message, name='send_message'),
    path('conversation-detail/<int:representative_id>/', views.conversation_detail, name='conversation_detail'),
    path('inbox/', views.inbox, name='inbox'),
]
