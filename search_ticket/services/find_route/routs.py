from search_ticket.models import RouteStation, Station
from itertools import chain


def get_routs_according_to_direction(start_point, end_point):
    """finds routs according to stations that there are
    in each route"""

    if not (start_point or end_point):
        raise ValueError
    storage = []
    for i in list(
        chain(
            RouteStation.objects.filter(stations__name=start_point.name),
            RouteStation.objects.filter(stations__name=end_point.name),
        )
    ):
        if i.stations.filter(name=start_point.name) and i.stations.filter(
            name=end_point.name
        ):
            if (
                i.stations.get(name=start_point.name).id
                < i.stations.get(name=end_point.name).id
            ):
                storage.append(i.route)
    return storage


def get_station_by_name(station_name):

    return Station.objects.filter(name=station_name).first()


def get_unique_stations():

    stations = Station.objects.all()
    return {elem.name for elem in stations}
