import json

from django.http  import JsonResponse
from django.views import View

from .models import Actor, Movie, ActorMovie

class ActorView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            Actor.objects.create(
                first_name    = data['first_name'],
                last_name     = data['last_name'],
                date_of_birth = data['date_of_birth']
            )
            
            return JsonResponse({'message':'created'}, status=200)

        except KeyError:
            return JsonResponse({'error':'KeyError occured'}, status=400)
        except Actor.DoesNotExist:
            return JsonResponse({'error':'Does not exist'}, status=404)
        except Actor.MultipleObjectsReturned:
            return JsonResponse({'error':'multiple objects returned'}, status=400)
    
    def get(self,request):
        


class MovieView(View):
    def post(self,request):
    
    
    def get(self,request):