from django.shortcuts import render 
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from .serializers import PostSerializer
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from Messages.models import *
from django.http import Http404
from rest_framework import viewsets
from django.contrib.auth.models import User
import datetime
from django.db.models import Q

@permission_classes([IsAuthenticated])
class list_posts(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    def get_queryset(self):
        user=self.request.user
        return Message.objects.filter(Q(Q(Q(sender=user) & Q(Sender_Delete=False))) |(Q(Q(Receiver=user) & Q(Receiver_Delete=False))))

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        user=self.request.user
        parms=kwargs
        Messagefilter=list_posts.get_queryset(self)
        mesageUser= [Message.objects.get(id=i.id) for i in Messagefilter]
        if (parms['pk']=='UnRead'):
            mesage=[i for i in mesageUser if i.Read==False and i.Receiver==user]
            serlizer=PostSerializer(mesage,many=True)
            return Response(serlizer.data)  
        else:
            mesage=[i for i in mesageUser if i.Subject==parms['pk']]
        for i in mesageUser:
            if i.Receiver==user:
                i.Read=True
                i.save()
        serlizer=PostSerializer(mesage,many=True)
        return  Response(serlizer.data)  

    def destroy(self, request, *args, **kwargs):
        parms=kwargs
        mesage=Message.objects.filter(Subject=parms['pk'])
        mem=mesage.first()
        if(mem.Receiver==self.request.user):
            mem.Receiver_Delete=True
            mem.save()
        if(mem.sender==self.request.user):
            mem.Sender_Delete=True
            mem.save()
        response={"message":"message has been deleted"}
        return Response(data=response,status=status.HTTP_204_NO_CONTENT) 


   

    
  