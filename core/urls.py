from django.urls import path

from . import views

urlpatterns = [
    # view route only
    path('', views.index, name='index'),
    path('request', views.ViewSendRequest, name='ViewSendRequest'),

    path('success_drawing', views.success_drawing, name='success_drawing'),
    path('get_location', views.get_location, name='get_location'),
    path('test_api', views.test_api, name='test_api'),
]
