from django.urls import path

from LibraryMS import views

urlpatterns=[
    path('', views.loginfun, name='login'),

    path('register', views.registerfun, name='register'),
    path('logout', views.logoutfun, name='logout'),
    path('home',views.home, name='home'),
    path('add',views.add, name='add'),
    path('search',views.search, name='search'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.deletefun,name='delete'),
    path('dummy1/', views.dummy1, name='dummy1')

]