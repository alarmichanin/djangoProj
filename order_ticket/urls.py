from django.urls import path
from order_ticket.views import (
    order_seat,
    order_railcar,
    OrderTicket,
    order_train,
    TicketInfo,
)


urlpatterns = [
    path(
        "routs_for_user/<start>/<end>/<rout_slug>/<train>/<railcar>/",
        order_seat,
        name="order_seat",
    ),
    path(
        "routs_for_user/<start>/<end>/<rout_slug>/<train>/",
        order_railcar,
        name="order_railcar",
    ),
    path("routs_for_user/<start>/<end>/<rout_slug>/", order_train, name="order_train"),
    path(
        "routs_for_user/<start>/<end>/<rout_slug>/<train>/<railcar>/<seat>/",
        OrderTicket.as_view(),
        name="order_ticket",
    ),
    path(
        "tickets/<ticket>/<ip>",
        TicketInfo.as_view(),
        name="ticket_info",
    ),
]
