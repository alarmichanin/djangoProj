from django.urls import path
from order_ticket.views import OrderSeat, OrderRailcar


urlpatterns = [
    path("routs_for_user/<rout_slug>/<railcar>/", OrderSeat.as_view() , name="order_ticket"),
    path("routs_for_user/<rout_slug>/", OrderRailcar.as_view() , name="order_railcar")

]