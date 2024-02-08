from django.shortcuts import render
from .models import *

def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user 
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)

    food = Food.objects.all()
    context = {'foods': food, 'consumed_food': consumed_food}
    return render(request, 'tracker_app/index.html', context=context)