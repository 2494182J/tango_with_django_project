from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # no need context_dict= {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):

    context_dict = {}
    try:
# Can we find a category name slug with the given name?

        category = Category.objects.get(slug=category_name_slug)
# Retrieve all of the associated pages.

        pages = Page.objects.filter(category=category)
# Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
# We also add the category object from

        context_dict['category'] = category
    except Category.DoesNotExist:
# We get here if we didn't find the specified category.

        context_dict['category'] = None
        context_dict['pages'] = None
# Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)