from django.urls import path

from new_app import views

urlpatterns = [
   path("text",views.text,name="text"),
   path("tem", views.tem, name="tem"),
   path("dash",views.dashboard,name="dash"),
   path("dash2",views.dashboard2,name="dash2")
]
