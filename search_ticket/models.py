from django.db import models


class Route(models.Model):
    # Create your models here.
    """class of train route"""

    start_point = models.ForeignKey(
        "Station",
        verbose_name=("Start name"),
        on_delete=models.CASCADE,
        related_name="start_point",
    )
    end_point = models.ForeignKey(
        "Station",
        verbose_name=("End name"),
        on_delete=models.CASCADE,
        related_name="end_point",
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
        null=True,
        blank=True,
    )
    # rout_train = models.ForeignKey(
    #     "RoutTrain",
    #     related_name="rout_train",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )

    # rout_station = models.ForeignKey(
    #     "RouteStation",
    #     related_name="route_station",
    #     on_delete=models.CASCADE,
    #     null=True,
    # )

    def __str__(self) -> str:
        return f"{self.start_point} - {self.end_point}"


class Station(models.Model):
    """ """

    name = models.CharField("station name", max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Train(models.Model):
    """ """

    number_of_railcar = models.IntegerField("number of railcar")
    name = models.CharField(max_length=150, null=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="URL",
        null=True,
        blank=True,
    ) 
    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"


class RoutTrain(models.Model):
    """ """

    route = models.ForeignKey(
        Route, related_name="routtrain_route", on_delete=models.CASCADE
    )
    train = models.ManyToManyField(
        Train, related_name="routtrain_train", verbose_name=("")
    )

    def __str__(self) -> str:
        return f"RoutTrain - {self.route} "


class RouteStation(models.Model):
    """ """

    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    stations = models.ManyToManyField(Station, verbose_name=(""))
    time = models.TimeField(auto_now=False, auto_now_add=False)
    price_from_start = models.PositiveIntegerField("price")

    def __str__(self) -> str:
        return f"{self.route.start_point} - {self.route.end_point}"

