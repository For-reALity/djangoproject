from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('enter/', views.enter, name='enter'),
    path('enter/jackets/', views.jackets, name='jackets'),
    path('enter/jackets/addjackets/', views.addjackets, name='addjackets'),
    path('enter/shirts/', views.shirts, name='shirts'),
    path('enter/shirts/addshirts/', views.addshirts, name='addshirts'),
    path('enter/pants/', views.pants, name='pants'),
    path('enter/pants/addpants/', views.addpants, name='addpants'),
    path('enter/shoes/', views.shoes, name='shoes'),
    path('enter/shoes/addshoes/', views.addshoes, name='addshoes'),
    path('list/', views.list, name='list'),
    path('list/viewjackets/', views.viewjackets, name='viewjackets'),
    path('list/viewshirts/', views.viewshirts, name='viewshirts'),
    path('list/viewpants/', views.viewpants, name='viewpants'),
    path('list/viewshoes/', views.viewshoes, name='viewshoes'),
    path('delete/', views.delete, name='delete'),
    path('delete/deletejackets/', views.deletejackets, name='deletejackets'),
    #path('delete/deletejackets/delete/', views.deletethatjacket, name='deletethatjacket'),
    #path('delete/deletejackets/delete/<str:jackets>', views.deletethatjacket, name='deletethatjacket'),
    path('delete/deleteshirts/', views.deleteshirts, name='deleteshirts'),
    path('delete/deletepants/', views.deletepants, name='deletepants'),
    path('delete/deleteshoes/', views.deleteshoes, name='deleteshoes'),
]
