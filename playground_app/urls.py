from django.urls import path
from . import views


#URLConfiguration
#!اكتب اللى انا عاوزه فى البحث بعد كتابة مكان  app (playground-app)
urlpatterns = [
    path('hello/', views.say_hello)
]
