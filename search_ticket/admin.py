from django.contrib import admin

from search_ticket.models import Route, RouteStation, Station, Train


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('start_point','end_point', "train")
    fields = ('start_point','end_point', "train", "slug")


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", )
    fields = ('name',)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('station', "number_of_railcar")
    fields = ('station', "number_of_railcar")


@admin.register(RouteStation)
class RouteStationAdmin(admin.ModelAdmin):
    list_display = ('route', "time", "price_from_start")
    fields = ('route', "stations", "time",  "price_from_start")
