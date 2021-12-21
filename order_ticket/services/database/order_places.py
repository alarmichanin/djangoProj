from order_ticket.models import Ticket
from search_ticket.models import RoutTrain, Route, Train


def fill_tickets(route):
    trains = RoutTrain.objects.filter(route=route).first().train.all()
    for train in trains:
        for railcar_number in range(1, train.number_of_railcar + 1):
            for number_of_seat in range(1, 41):
                Ticket.objects.create(
                    route=route,
                    train=train,
                    railcar_number=railcar_number,
                    seat=number_of_seat,
                )


def get_available_seats(rout_slug, train_slug, railcar_number):
    available_seats = {
        elem.seat
        for elem in Ticket.objects.filter(
            route=Route.objects.get(slug=rout_slug),
            train=Train.objects.get(slug=train_slug),
            railcar_number=int(railcar_number),
            is_taken=False,
        )
    }
    return available_seats


def get_available_trains(rout_slug):
    trains = Ticket.objects.filter(
        route=Route.objects.get(slug=rout_slug), is_taken=False
    )
    return {elem.train for elem in trains}


def get_available_railcars(rout_slug, train_slug):

    available_reilcars = {
        elem.railcar_number
        for elem in Ticket.objects.filter(
            route=Route.objects.get(slug=rout_slug),
            train=Train.objects.get(slug=train_slug),
            is_taken=False,
        )
    }
    return available_reilcars
