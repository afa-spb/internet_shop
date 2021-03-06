from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('category/', categories, name='categories'),
    path('category/<slug>', category, name='category'),
    path('product/<int:pk>', product_card, name='product_card')
]
