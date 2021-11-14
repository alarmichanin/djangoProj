from django.db import models
from django.db.models.fields import SlugField

# Create your models here.
class Route(models.Model):
    """ class of train route """

    start_point = models.ForeignKey("Station", verbose_name=("Start name"), 
        on_delete=models.CASCADE, related_name="start_point")
    end_point = models.ForeignKey("Station", verbose_name=("End name"), 
        on_delete=models.CASCADE, related_name="end_point")
    train = models.ForeignKey("Train", verbose_name=("train"), on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL", null=True)

    def __str__(self) -> str:
        return f"{self.start_point} - {self.end_point}"

class Station(models.Model):
    """ """

    name = models.CharField("station name", max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Train(models.Model):
    """ """

    station = models.ForeignKey(Station, verbose_name=(""), on_delete=models.CASCADE)
    number_of_railcar = models.IntegerField("number of railcar")

    def __str__(self) -> str:
        return f"{self.station} - {self.number_of_railcar}"


class RouteStation(models.Model):
    """ """

    route = models.ForeignKey(Route, verbose_name=(""), on_delete=models.CASCADE)
    stations = models.ManyToManyField(Station, verbose_name=(""))
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price_from_start = models.PositiveIntegerField("price")

    def __str__(self) -> str:
        return f"{self.route} - {self.stations}"