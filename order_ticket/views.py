from order_ticket.services.order_ticket import (
    get_discount,
    get_route,
    get_train,
    get_ticket,
    get_client_ip,
    create_customer_ticket,
    get_ordered_ticket,
)
from search_ticket.services.find_route.routs import get_station_by_name
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from order_ticket.models import Ticket
from search_ticket.models import Route, Train
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse
from order_ticket.forms import OrderTicketForm
from icecream import ic
from django.contrib import messages
from order_ticket.models import Railcar


def order_train(request, start, end, rout_slug):

    if request.method == "POST":
        train = request.POST.get("train").strip()
        return HttpResponseRedirect(
            reverse(
                "order_railcar",
                kwargs={
                    "start": start,
                    "end": end,
                    "rout_slug": rout_slug,
                    "train": train,
                },
            )
        )
    available_trains = Ticket.objects.filter(
        route=Route.objects.get(slug=rout_slug), is_taken=False
    )
    available_trains = {elem.train for elem in available_trains}
    return render(
        request,
        "order_ticket/order_train.html",
        context={
            "route_slug": rout_slug,
            "start": start,
            "end": end,
            "trains": available_trains,
        },
    )


def order_railcar(request, start, end, rout_slug, train):

    if request.method == "POST":
        railcar = request.POST.get("railcar")
        return HttpResponseRedirect(
            reverse(
                "order_seat",
                kwargs={
                    "start": start,
                    "end": end,
                    "rout_slug": rout_slug,
                    "train": train,
                    "railcar": railcar,
                },
            )
        )
    try:
        available_reilcars = {
            elem.railcar_number
            for elem in Ticket.objects.filter(
                route=Route.objects.get(slug=rout_slug),
                train=Train.objects.get(slug=train),
                is_taken=False,
            )
        }
    except Exception:
        messages.add_message(
            request,
            messages.ERROR,
            "there is no such train on this direction",
        )
        return HttpResponseRedirect(
            reverse(
                "order_train",
                kwargs={
                    "start": start,
                    "end": end,
                    "rout_slug": rout_slug,
                },
            )
        )

    return render(
        request,
        "order_ticket/choose_place.html",
        context={
            "start": start,
            "end": end,
            "route_slug": rout_slug,
            "train": train,
            "railcars": available_reilcars,
        },
    )


def order_seat(request, start, end, rout_slug, train, railcar):

    if request.method == "POST":
        seat = request.POST.get("seat")
        try:
            if int(seat) not in range(1, Railcar.objects.first().amount_of_seats):
                raise ValueError
        except Exception:
            messages.add_message(
                request,
                messages.ERROR,
                "Invalid number of seats",
            )
            return HttpResponseRedirect(
                reverse(
                    "order_seat",
                    kwargs={
                        "start": start,
                        "end": end,
                        "rout_slug": rout_slug,
                        "train": train,
                        "railcar": railcar,
                    },
                )
            )
        return HttpResponseRedirect(
            reverse(
                "order_ticket",
                kwargs={
                    "start": start,
                    "end": end,
                    "rout_slug": rout_slug,
                    "train": train,
                    "railcar": railcar,
                    "seat": seat,
                },
            )
        )

    try:
        available_seats = {
            elem.seat
            for elem in Ticket.objects.filter(
                route=Route.objects.get(slug=rout_slug),
                train=Train.objects.get(slug=train),
                railcar_number=int(railcar),
                is_taken=False,
            )
        }
        if int(railcar) not in range(
            1, Train.objects.get(slug=train).number_of_railcar
        ):
            raise ValueError

    except Exception:

        messages.add_message(
            request,
            messages.ERROR,
            "there is no such railcar on this direction",
        )
        return HttpResponseRedirect(
            reverse(
                "order_railcar",
                kwargs={
                    "start": start,
                    "end": end,
                    "rout_slug": rout_slug,
                    "train": train,
                },
            )
        )

    return render(
        request,
        "order_ticket/order_seat.html",
        context={
            "start": start,
            "end": end,
            "route_slug": rout_slug,
            "train": train,
            "railcar": railcar,
            "seats": available_seats,
        },
    )


class OrderTicket(FormView):

    model = Ticket
    template_name = "order_ticket/order_ticket.html"

    def post(self, request, *args, **kwargs):
        start = self.kwargs["start"]
        end = self.kwargs["end"]
        rout_slug = self.kwargs["rout_slug"]
        train_slug = self.kwargs["train"]
        railcar = self.kwargs["railcar"]
        seat = self.kwargs["seat"]

        form = OrderTicketForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            patronymic = form.cleaned_data["patronymic"]
            disc = form.cleaned_data["discount"]
            if disc:
                if not get_discount(disc):
                    messages.add_message(request, messages.ERROR, "discount is invalid")
                    return HttpResponseRedirect(
                        reverse(
                            "order_ticket",
                            kwargs={
                                "start": start,
                                "end": end,
                                "rout_slug": rout_slug,
                                "train": train_slug,
                                "railcar": railcar,
                                "seat": seat,
                            },
                        )
                    )
                discount = get_discount(disc)
            else:
                discount = 0
            email = form.cleaned_data["email"]
            ticket = get_ticket(
                get_route(rout_slug), get_train(train_slug), railcar, seat
            )
            create_customer_ticket(
                get_client_ip(request),
                ticket,
                get_station_by_name(start),
                get_station_by_name(end),
                name,
                surname,
                patronymic,
                discount,
                email,
            )
            return HttpResponseRedirect(
                reverse(
                    "ticket_info",
                    kwargs={
                        "ip": get_client_ip(request),
                        "ticket": ticket.id,
                    },
                )
            )

        else:
            messages.add_message(request, messages.ERROR, "Form is invalid")
            return HttpResponseRedirect(
                reverse(
                    "order_ticket",
                    kwargs={
                        "start": start,
                        "end": end,
                        "rout_slug": rout_slug,
                        "train": train_slug,
                        "railcar": railcar,
                        "seat": seat,
                    },
                )
            )

    def get_context_data(self, **kwargs):

        form = OrderTicketForm(self.request.POST)
        context = {"title": "order", "form": form}
        return context


class TicketInfo(TemplateView):

    template_name = "order_ticket/ticket_info.html"

    def get_context_data(self, **kwargs):

        ticket_id = self.kwargs["ticket"]
        ip = self.kwargs["ip"]

        ordered_ticket = get_ordered_ticket(ticket_id, ip)
        context = {"ordered_ticket": ordered_ticket}
        return context
