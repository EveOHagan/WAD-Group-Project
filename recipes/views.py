from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import *
from recipes.forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def index(request):
    recipes = Recipe.objects.order_by('name')
    cats = Category.objects.all()
    chefs = Chef.objects.order_by('username')
    dinners = Category.objects.get(name="Dinner").recipe_set.all()
    context_dict = {'recipes':recipes, 'cats':cats, 'chefs':chefs, 'dinners':dinners}
    response = render(request,'recipes/index.html', context=context_dict)
    return response
