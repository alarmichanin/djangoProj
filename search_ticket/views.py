from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic import ListView, TemplateView
from search_ticket.services.find_route.routs import (
    get_routs_according_to_direction,
    get_station_by_name,
)
from search_ticket.utils import DataMixin
from django.contrib import messages
from search_ticket.models import Route, RouteStation
from .forms import SearchRouteForm
from icecream import ic

# Create your views here.


def get_home_page(request):

    if request.method == "POST":
        form = SearchRouteForm(request.POST)

        if form.is_valid():
            request.session.set_expiry(1000)
            request.session["start_point"] = form.cleaned_data["start_point"]
            request.session["end_point"] = form.cleaned_data["end_point"]
            request.session["date"] = request.POST["date"]
            return HttpResponseRedirect(reverse("get_avaluable_routs"))
        else:
            messages.add_message(
                request,
                messages.Error,
                "Some problems came out, fix them and try again",
            )
    else:

        form = SearchRouteForm()

    return render(
        request, template_name="search_ticket/home_page.html", context={"form": form}
    )


class AvaluableRouts(DataMixin, ListView):
    """all avaluable routs according
    to parameters
    """

    model = RouteStation
    template_name = "search_ticket/get_avaluable_routs.html"
    context_object_name = "all_routs"

    def get_queryset(self):

        result = get_routs_according_to_direction(
            get_station_by_name(self.request.session["start_point"]),
            get_station_by_name(self.request.session["end_point"]),
        )
        return RouteStation.objects.filter(route__in=result)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # like dynamic list
        c_def = self.get_user_context(
            start_point=self.request.session["start_point"],
            end_point=self.request.session["end_point"],
        )
        return dict(list(context.items()) + list(c_def.items()))


class AboutView(DataMixin, TemplateView):
    template_name = "booking/about.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class TestimonialsView(DataMixin, TemplateView):
    template_name = "booking/testimonials.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class FeaturesView(DataMixin, TemplateView):
    template_name = "booking/features.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class TeamView(DataMixin, TemplateView):
    template_name = "booking/team.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class PricingView(DataMixin, TemplateView):
    template_name = "booking/pricing.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ContactsView(DataMixin, TemplateView):
    template_name = "booking/contacts.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)  # add some variable to show
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
