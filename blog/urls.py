from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('blog/<int:id>' , views.main , name='main'),
]
