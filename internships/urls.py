from django.contrib import admin
from django.urls import path, include
# import internships.urls as internships
from .views import HNGListView

app_name = "internships"

urlpatterns = [
    path('hng/', HNGListView.as_view()),
]
