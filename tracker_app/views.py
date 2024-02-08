from django.shortcuts import render, redirect
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

def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('tracker_app:index')
    return render(request, 'tracker_app/delete.html')