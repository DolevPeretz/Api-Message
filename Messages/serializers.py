from rest_framework import serializers
# from .models import ApiMessage
from Messages.models import *
from .models import *



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
       
        fields = [
            'id',
            'sender',
            'Receiver',
            'Subject',
            'Message',
            'creation_Date',
        ]
    def update(self):
        message.set_Read(True)
        user.save()
        return user
    def get_accounts_items(self, obj):
        account_query = Message.objects.filter(sender=obj.id)
        serializer = AccountSerializer(account_query, many=True)
        return serializer.data
        