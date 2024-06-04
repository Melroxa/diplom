from django.shortcuts import render, get_object_or_404
from .models import Service, Category, CategoryMaster, Master


def index(request):
    title = 'Мармилен'
    categories = Category.objects.all()
    services = Service.objects.filter(category__in=categories)
    categories_master = CategoryMaster.objects.all()

    return render(request, 'main/main.html', {'title': title,
                                              'categories': categories,
                                              'services': services,
                                              'categories_master': categories_master})


def category_master_detail(request, category_slug):
    category_instance = get_object_or_404(CategoryMaster, slug=category_slug)
    masters = Master.objects.filter(category=category_instance)
    context = {'category_instance': category_instance, 'masters': masters}
    return render(request, 'main/master_details.html', context)


def contacts_page(request):
    title = 'Контакты'
    return render(request, 'main/contacts_page.html', {"title": title})


def about(request):
    return render(request, 'main/about.html')
