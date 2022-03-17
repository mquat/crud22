
import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class OwnerView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            Owner.objects.create(
                name  = data['name'],
                email = data['email'],
                age   = data['age']
            )
            return JsonResponse({'message':'success'},status=200)
        except KeyError:
            return JsonResponse({'error':'KEYERROR'},status=400)

    def get(self,request):
        result = [{
            'name'     : owner.name,
            'email'    : owner.email,
            'age'      : owner.age,
            'dog_info' : [{
                'name'   : dog.name,
                'age'    : dog.age
            } 
            for dog in owner.dog_set.all()]} 
            for owner in Owner.objects.all()]
        
        return JsonResponse({'result':result},status=201)

class DogView(View):
    def post(self,request):
        try: 
            data = json.loads(request.body)
            owner = Owner.objects.get(name=data['owner'])	
            Dog.objects.create(
                name  = data['name'],
                age   = data['age'],
                owner = owner.id	#Owner.object(1)의 id값 
            )
            return JsonResponse({"message":'created'},status=200)

        except KeyError:
            return JsonResponse({'error':'KEYERROR'},status=400)
        except Owner.DoesNotExist:
            return JsonResponse({'error':'specified owner does not exist'},status=404)
        except Owner.MultipleObjectsReturned:
            return JsonResponse({'error':'multiple objects returned'},status=400)

    def get(self,request):
        result = [{
            'name'     : dog.name,
            'age'      : dog.age,
            'host_name': dog.owner.name
            } 
        for dog in Dog.objects.all()]
        
        return JsonResponse({"message":result},status=201)