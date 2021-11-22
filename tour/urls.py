from django.urls import path

from tour.views import *

urlpatterns = [
    path('tours/<int:id>/', country_detail, name='country_detail'),
    path('tour_detail/<int:id>/', tour_detail, name='tour_detail')
]
