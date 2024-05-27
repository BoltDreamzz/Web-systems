from django.db import models
from authusers.models import User
from core.models import TeamMember


# Create your models here.
class Representative(models.Model):
    representative = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    # profile_pic = models.ImageField(upload_to='rep_profile', null=True, blank=False)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.representative.name


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)
    # Add any additional fields you need for your conversation


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# class Message(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(Representative, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
