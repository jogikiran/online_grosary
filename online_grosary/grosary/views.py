from django.shortcuts import render, redirect
from .models import Grosary, Order
from django.contrib import messages


def create_grosary(request):
    if request.method == "POST":
        name = request. POST['name']
        image = request.FILES['image']
        prize = request.POST['prize']

        mart = Grosary(grosary_name=name, image=image, prize=prize, user=request.user)
        mart.save()

    return render(request, "grosaries_templates/create_grosary.html")

def grosary_list_view(request):
    grosary = Grosary.objects.all()
    return render(request, 'grosaries_templates/grosary_list.html', {'grosaries':grosary})


def grosary_details(request, id):
    mart = Grosary.objects.get(pk=id)
    return render(request, 'grosaries_templates/grosary_details.html', {'grosaries':mart})

def grosary_update(request, id):
    mart = Grosary.objects.get(pk=id)
    if request.method == "POST":
        name = request. POST['name']
        image = request.FILES['image']
        prize = request.POST['prize']

        mart.grosary_name=name
        mart.image=image
        mart.prize=prize
        mart.save()
        return redirect("/")
    return render(request, 'grosaries_templates/grosary_update.html', {'mart': mart})


def place_order(request):
    if request.method == "POST":
        id = request.POST['grosary_id']
        obj = Grosary.objects.get(pk=id)
        Order.objects.create(user=request.user, grosary=obj)
        messages.success(request, f'order placed successfully')
        return redirect('/grosary/grosary-list/')

def order_list(request):
    mart = Order.objects.all()
    return render(request, 'order_templates/order_list.html', {'marts':mart})

def grosary_dashboard(request):
    return render(request, 'dashboard_templates/index.html')


def my_order_list(request):
    mart = Order.objects.filter(user=request.user)
    context = {
        'marts':mart
    }
    return render(request, 'grosaries_templates/my_order_list.html', context)


def cancel_order(request, id):
    mart = Order.objects.get(pk=id)
    mart.delete()
    return redirect("/grosary/my-order-list/")

def delete_grosary(request, id):
    mart = Grosary.objects.get(pk=id)
    mart.delete()
    return redirect("/grosary/grosary-list/")