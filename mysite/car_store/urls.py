from django.urls import path
from .views import *

urlpatterns = [
    path('', CarViewSet.as_view({'get':'list','post':'create'}) ),
    path('<int:pk>/', CarViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('model/', ModelViewSet.as_view({'get':'list','post':'create'}) ),
    path('model/<int:pk>/', ModelViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('marka/', MarkaViewSet.as_view({'get':'list','post':'create'}) ),
    path('marka/<int:pk>/', MarkaViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]