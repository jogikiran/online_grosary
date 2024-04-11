from django.urls import path
from .views import (create_grosary, 
                    grosary_list_view, 
                    grosary_details, 
                    grosary_update, 
                    place_order, 
                    order_list, 
                    grosary_dashboard, 
                    my_order_list, 
                    cancel_order, 
                    delete_grosary
)

urlpatterns = [
    path('create-grosary/', create_grosary),
    path('grosary-list/', grosary_list_view),
    path('grosary-details/<int:id>/', grosary_details),
    path('grosary-update/<int:id>/', grosary_update),
    path('place-order/', place_order),
    path('order-list/', order_list),
    path('grosary-dashboard/', grosary_dashboard),
    path('my-order-list/', my_order_list),
    path('cancel-order/<int:id>/', cancel_order),
    path('delete-grosary/<int:id>/', delete_grosary),
]