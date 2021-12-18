# from order_ticket.services.database.order_seat import fill_tickets
from django.http import HttpResponseRedirect
from search_ticket.utils import DataMixin
from icecream import ic
from order_ticket.models import Ticket
from search_ticket.models import Route
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse


def order_railcar(request, rout_slug):

    if request.method == "POST":
        railcar = request.POST.get("railcar")
        ic(rout_slug, railcar)
        return HttpResponseRedirect(reverse("order_seat", kwargs={"rout_slug": rout_slug, "railcar":railcar}))
    ic(rout_slug)
    print("here")
    return render(request, "order_ticket/choose_place.html", context={"route_slug" : rout_slug})


def order_seat(request, rout_slug, railcar):

    if request.method == "POST":
        seat = request.POST.get("seat")
        return HttpResponseRedirect(reverse("order_tiket", kwargs={"rout_slug": rout_slug, "railcar":railcar, "seat" : seat}))
    ic(rout_slug)
    print("here")
    return render(request, "order_ticket/order_seat.html", context={"route_slug" : rout_slug, "railcar": railcar})


class OrderTicket(FormView):
    
    model = Ticket
    template_name = "order_ticket/order_ticket.html"

    def get_queryset(self):

        return Ticket.objects.all()

    def get_context_data(self, **kwargs):
        context = {"title" : "order"}
        return context