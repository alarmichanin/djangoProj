from django.contrib import admin
from django.urls import path, include
from search_ticket.views import get_home_page, AvaluableRouts

urlpatterns = [
    
    path("", get_home_page, name="home"),
    path("routs_for_user/", AvaluableRouts.as_view(), name="get_avaluable_routs"),

]