from django.urls import path
from order_and_pay.views import *

urlpatterns = [
    path('', make_order, name='make_order'),
    path('<int:order_number>', view_order, name='view_order'),
    path('<int:order_number>/pay', pay_order, name='pay_order'),
    path('search/', search_order, name='search_order'),
    path('my_order/', my_order, name='my_order'),
]
