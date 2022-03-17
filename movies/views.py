import json

from django.http  import JsonResponse
from django.views import View

from .models import Actor, Movie

class ActorView(View):
    def get(self,request):
        result = [{
            'first_name' : actor.first_name,
            'last_name'  : actor.last_name,
            'movie_lst'  : [{
                'title'  : movie.title,
            } for movie in actor.movies.all()]
        } for actor in Actor.objects.all()]

        return JsonResponse({'result':result},status=201)            
        
class MovieView(View):
    def get(self,request):
        result = [{
            'title'        : movie.title,
            'running_time' : movie.running_time,
            'actor_lst'    : [{
                'actor' : actor.last_name + actor.first_name
            } for actor in movie.actors_set.all()]
        } for movie in Movie.objects.all()]
    
        return JsonResponse({'result':result}, status=201)