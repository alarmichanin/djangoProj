from order_ticket.services.database.order_seat import fill_tickets
from search_ticket.utils import DataMixin
from icecream import ic
from order_ticket.models import Ticket
from search_ticket.models import Route
from django.views.generic.edit import FormView
from order_ticket.forms import OrderSeatForm, OrderRailcarForm


class OrderSeat(DataMixin, FormView):
    """all avaluable routs according
    to parameters
    """

    model = Ticket
    template_name = "order_ticket/choose_place.html"

    def get_queryset(self):

        return Ticket.objects.all()

    def get_context_data(self, **kwargs):
        rout_slug = self.kwargs.get("rout_slug")
        self.route = Route.objects.filter(slug=rout_slug).first()
        form = OrderSeatForm(self.route, self.request.POST)
        context = {"form": form}

        if form.is_valid():
            select_date = self.request.POST
            print(select_date)

        return context


class OrderRailcar(DataMixin, FormView):
    """all avaluable routs according
    to parameters
    """

    model = Ticket
    template_name = "order_ticket/choose_place.html"

    def get_queryset(self):

        rout_slug = self.kwargs.get("rout_slug")
        self.route = Route.objects.filter(slug=rout_slug).first()

        if not Ticket.objects.all():
            fill_tickets(self.route)

        if Ticket.objects.all():
            ic(True)
        return Ticket.objects.all()

    def get_context_data(self, **kwargs):

        rout_slug = self.kwargs.get("rout_slug")
        self.route = Route.objects.filter(slug=rout_slug).first()
        form = OrderRailcarForm(self.route, self.request.POST)  # <- remove this line
        

        context = {"form": form}

        return context
