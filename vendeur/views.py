from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VendeurSerializer
from .models import Vendeur

# Create your views here.



#API REST 
@api_view(['GET'])
def allVendeurs(request):
    vendeurs = Vendeur.objects.all()
    serialization = VendeurSerializer(vendeurs, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def getVendeur(request, id):
    vendeur = Vendeur.objects.get(id=id)
    serialization = VendeurSerializer(vendeur)
    return Response(serialization.data)

@api_view(['POST'])
def addVendeur(request):
    serializer = VendeurSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateVendeur(request, id):
    vendeur = Vendeur.objects.get(id=id)
    serialization = VendeurSerializer(instance=vendeur, data=request.data)
    if serialization.is_valid():
        serialization.save()
    return Response(serialization.data)

@api_view(['DELETE'])
def deleteVendeur(request, id):
    vendeur = Vendeur.objects.get(id=id)
    vendeur.delete()
    return Response("Vendeur supprimé avec succès!")
