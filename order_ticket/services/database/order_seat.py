from order_ticket.models import Ticket


def fill_tickets(route):
    for train in route.rout_train.train.all():
        for railcar_number in range(1, train.number_of_railcar + 1):
            for number_of_seat in range(1, 41):
                Ticket.objects.create(
                    route=route,
                    train=train,
                    railcar_number=railcar_number,
                    seat=number_of_seat,
                )
