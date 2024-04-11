from django.shortcuts import render
from grosary.models import Grosary, Order

from django.http import Http404

def grosary_dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request, 'dashboard_templates/index.html')
    else :
        raise Http404
    
def admin_grosary_list(request):
    mart = Grosary.objects.all()
    context = {
        'grosaries' : mart
    }
    return render(request, 'dashboard_templates/admin_grosary_list.html', context)

def admin_order_list(request):
    status = request.GET.get('status')
    quireset = Order.objects.all()
    if status == 'confirmed':
        quireset = quireset.filter(status='order confirmed')
    if status == 'processing':
        quireset = quireset.filter(status='order processing')
    if status == 'shipping':
        quireset = quireset.filter(status='order shipping')
    if status == 'cancelled':
        quireset = quireset.filter(status='order cancelled')
    if status == 'delivered':
        quireset = quireset.filter(status='order delivered')

    context = {
        'orders': quireset
    }
    return render(request, 'dashboard_templates/admin_order_list.html', context)
