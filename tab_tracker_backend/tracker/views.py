from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from urllib.parse import urlparse
from . models import *
from datetime import timedelta
from . filters import NewTabFilter


# Create your views here.

@api_view(['GET'])
def NewTabList(request):
    
    newtab = NewTab.objects.all()
    serializer = NewTabSerializer(newtab, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def NewTabFilterView(request):
   
    queryset = NewTab.objects.all()
    filterset = NewTabFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = NewTabSerializer(queryset, many=True)
    
    return Response(serializer.data)



@api_view(['POST'])
def NewTabCreate(request):
    #if request.user.is_landlord == True:
        all_new = NewTab.objects.all()
        if request.method == "POST":
            for i in all_new:
                if i.time_closed == "":
                    i.time_closed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    i.save()
                if i.diff == "":
                    i.time_opened = i.time_opened[:-7]
                    i.diff = datetime.strptime(i.time_closed, "%Y-%m-%d %H:%M:%S")-datetime.strptime(i.time_opened, "%Y-%m-%d %H:%M:%S")
                    
                    i.save()
            
            serializer = NewTabSerializer(data=request.data)
            
            
        if serializer.is_valid():
            serializer.validated_data["url"] = urlparse(serializer.validated_data["url"]).netloc 
            
                
            serializer.save()

        return Response(serializer.data)





@api_view(['POST'])
def SwitchTabCreate(request):
    #if request.user.is_landlord == True:
        all_switch = SwitchTab.objects.all()
        if request.method == "POST":
            for i in all_switch:
                if i.time_closed == "":
                    i.time_closed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                    i.save()
                if i.diff == "":
                    #i.diff = float(i.time_closed)-float(i.time_opened)
                    
                    
                    i.save
            serializer = SwitchTabSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)



@api_view(['GET'])
def SwitchTabList(request):
    
    switchtab = SwitchTab.objects.all()
   
    serializer = SwitchTabSerializer(switchtab, many=True)
    return Response(serializer.data)