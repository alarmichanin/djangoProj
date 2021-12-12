from django.views.generic import ListView
from order_ticket.services.database.order_seat import fill_tickets
from search_ticket.utils import DataMixin
from icecream import ic
from order_ticket.models import Ticket
from search_ticket.models import Route
# Create your views here.

class OrderRailcarSeat(DataMixin, ListView):
    """all avaluable routs according
    to parameters
    """
    model = Ticket
    template_name = "order_ticket/choose_place.html"

    def get_queryset(self):

        rout_slug = self.kwargs.get("rout_slug")
        route = Route.objects.filter(slug=rout_slug).first()

        if not Ticket.objects.all():
            fill_tickets(route)

        if Ticket.objects.all():
            ic(True)    
        return Ticket.objects.all()
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)  # like dynamic list
    #     c_def = self.get_user_context(
    #         start_point=self.request.session["start_point"],
    #         end_point=self.request.session["end_point"],
    #     )
    #     return dict(list(context.items()) + list(c_def.items()))
