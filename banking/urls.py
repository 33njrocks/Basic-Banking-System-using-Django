from django.urls import path
from . import views
 
urlpatterns = [
    path('customer',views.customer,name='customer'),
    path('history',views.history,name='history'),
    path('profile/<int:id>/',views.profile,name='profile')
]