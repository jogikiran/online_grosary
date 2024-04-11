from django.urls import path
from .views import grosary_dashboard, admin_grosary_list, admin_order_list

app_name="superadmin"
urlpatterns = [
    path('grosary-dashboard/', grosary_dashboard, name='grosary_dashboard'),
    path('admin-list/', admin_grosary_list, name='admin_grosary_list'),
    path('admin-order-list/', admin_order_list, name='admin_order_list'),
    
]