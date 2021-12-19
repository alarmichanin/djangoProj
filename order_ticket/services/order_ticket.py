from order_ticket.models import Discount, Ticket, OrderTicket
from search_ticket.models import Route, Train


def get_client_ip(request):  # get current ip address

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_discount(discount):
    discount_obj = Discount.objects.filter(discount_code=discount)
    print(Discount.objects.all())
    return discount_obj.first().discount if discount_obj else 0


def get_route(route_slug):
    return Route.objects.get(slug=route_slug)


def get_train(train_slug):
    return Train.objects.get(slug=train_slug)


def get_ticket(route, train, railcar, seat):
    return Ticket.objects.get(
        route=route, train=train, railcar_number=railcar, seat=seat
    )


def create_customer_ticket(
    ip, ticket, start, end, name, surname, patronymic, discount, email
):

    OrderTicket.objects.create(
        ip=ip,
        ticket=ticket,
        start_point=start,
        end_point=end,
        customer_name=name,
        customer_surname=surname,
        customer_patronymic=patronymic,
        discount=discount,
        email=email,
        price=100 - 100 * discount,
    )
    ticket.is_taken = True
    ticket.save()


def get_ordered_ticket(ticket_id, ip):

    return OrderTicket.objects.get(ticket=Ticket.objects.get(id=ticket_id), ip=ip)
