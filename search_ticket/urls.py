from django.urls import path
from search_ticket.views import (
    get_home_page,
    AvaluableRouts,
    AboutView,
    TestimonialsView,
    FeaturesView,
    TeamView,
    PricingView,
    ContactsView,
)

urlpatterns = [
    path("", get_home_page, name="home"),
    path(
        "routs_for_user/<start>/<end>",
        AvaluableRouts.as_view(),
        name="get_avaluable_routs",
    ),
    path("about/", AboutView.as_view(), name="about_view"),
    path("testimonials/", TestimonialsView.as_view(), name="testimonials_view"),
    path("features/", FeaturesView.as_view(), name="features_view"),
    path("team/", TeamView.as_view(), name="team_view"),
    path("pricing/", PricingView.as_view(), name="pricing_view"),
    path("contacts/", ContactsView.as_view(), name="contacts_view"),

]
