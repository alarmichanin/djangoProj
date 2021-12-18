from django.urls import path
from order_ticket.views import order_seat, order_railcar, OrderTicket


urlpatterns = [
    path("routs_for_user/<rout_slug>/<railcar>/", order_seat , name="order_seat"),
    path("routs_for_user/<rout_slug>/", order_railcar , name="order_railcar"),
    path("routs_for_user/<rout_slug>/<railcar>/<seat>/", OrderTicket.as_view() , name="order_tiket"),

]