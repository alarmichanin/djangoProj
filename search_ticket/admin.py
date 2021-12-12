from django.contrib import admin

from search_ticket.models import RoutTrain, Route, RouteStation, Station, Train


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('start_point','end_point', "rout_train")
    fields = ('start_point','end_point', "rout_train", "slug")
    prepopulated_fields = {"slug": ("start_point", "end_point")}


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("name", )
    fields = ('name',)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ("name","number_of_railcar",)
    fields = ("name", "number_of_railcar", )


@admin.register(RoutTrain)
class RoutTrainAdmin(admin.ModelAdmin):
    list_display = ("route",)
    fields = ("route", "train" )


@admin.register(RouteStation)
class RouteStationAdmin(admin.ModelAdmin):
    list_display = ("time", "price_from_start")
    fields = ("stations", "time",  "price_from_start")
