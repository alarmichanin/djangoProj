from django.urls import path
from order_ticket.views import OrderRailcarSeat


urlpatterns = [
    path("routs_for_user/<rout_slug>/", OrderRailcarSeat.as_view() , name="order_ticket")
]