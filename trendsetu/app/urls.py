from django.urls import path
from . import views 
urlpatterns = [
path("", views.home), 

    path("home/", views.home, name="home"), 
    path("thrift/", views.thriftView.as_view(),name="thrift"), 
        path('bags/', views.bags_view, name='bags'),
path('accessories/', views.accessories_view, name='accessories'), 
    path('sell/', views.sell_clothing, name='sell_clothing'),

    
]
