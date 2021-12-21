from order_ticket.models import Ticket
from search_ticket.models import RoutTrain,Route


def fill_tickets():
    for route in Route.objects.all():
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
