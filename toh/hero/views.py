from django.http import (
    HttpRequest,
    HttpResponse, 
    HttpResponseBadRequest, 
    HttpResponseNotAllowed, 
    JsonResponse
)
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from json.decoder import JSONDecodeError
from .models import Hero

def index(request: HttpRequest):
    if 'visit_count' not in request.session:
        request.session['visit_count'] = 1
    else:
        request.session['visit_count'] += 1
    return HttpResponse(f"Hello you visited {request.session['visit_count']} times")

def id(request: HttpRequest, id):
    return HttpResponse(f'Your id is {id}!')

def name(request: HttpRequest, name):
    return HttpResponse(f'Your name is {name}!')

def hero_list(request: HttpRequest):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        return JsonResponse(hero_all_list, safe=False)
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {'id': hero.id, 'name': hero.name}
        return JsonResponse(response_dict, status=201)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def hero_info(request: HttpRequest, id):
    if request.method == 'GET':
        hero = Hero.objects.get(id=id)
        return JsonResponse({"id": hero.id, "name": hero.name, "age": hero.age})
    elif request.method == 'PUT':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            hero_age = json.loads(body)['age']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero.objects.get(id=id)
        hero.name = hero_name
        hero.age = hero_age
        hero.save()
        response_dict = {"id": hero.id, "name": hero.name, "age": hero.age}
        return JsonResponse(response_dict, status=200)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT'])

@ensure_csrf_cookie
def token(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET'])