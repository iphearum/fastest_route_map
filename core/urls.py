from django.urls import path
from . import views

urlpatterns = [
    # view route only
    path('', views.index, name='index'),
    path('success_drawing', views.test_api, name='success_drawing'),
    path('test_api', views.test_api, name='test_api'),

    # class Route
    path('request', views.Route.ViewSendRequest, name='ViewSendRequest'),
    path('get_location', views.Route.get_location, name='get_location'),
]
