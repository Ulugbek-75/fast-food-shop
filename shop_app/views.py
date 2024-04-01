# from django.shortcuts import render, redirect
# from django.views import View
# from shop_app.models import Category, Food
# from shop_app.form import CommentForm
# from django.http import HttpResponseNotAllowed
#
#
# class FeaneListview(View):
#
#     def get(self, request):
#         form = CommentForm()
#         category = Category.objects.filter()
#         food = Food.objects.filter()
#
#         context = {
#             'form': form,
#             'category': category,
#             'food': food,
#         }
#
#         return render(request, 'index.html', context)
#
#
#
#     def post(self, request):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Define the URL pattern for message_list
#         else:
#             # Handle invalid form data
#             return HttpResponseNotAllowed(["GET"])  # You may want to customize the response for invalid data



from shop_app.models import *
from django.shortcuts import render

def home(requests):
    ctg = Category.objects.all()
    food = Food.objects.all()
    ctx = {
        "ctg": ctg,
        "food": food
    }
    return render(requests, 'base.html', ctx)

def contact(requests):
    ctx = {}
    return render(requests, 'blog/about.html', ctx)

def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    food = Food.objects.all().filter(types_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'food': food
    }
    return render(requests, 'blog/menu.html', ctx)
def register(requests):
    ctx = {}
    return render(requests, 'blog/register.html', ctx)

def single(requests):
    ctx = {}
    return render(requests, 'blog/book.html', ctx)