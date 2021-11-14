from django.core.validators import RegexValidator
from django.db import models
from django.db.models.fields import CharField, PositiveBigIntegerField
from search_ticket.models import Station, Train, Route

# Create your models here.
class Railcar(models.Model):
    """ """

    type_of_railcar = models.ForeignKey("RailCarType", verbose_name=(""), on_delete=models.CASCADE)
    train = models.ForeignKey(Train, verbose_name=(""), on_delete=models.CASCADE)
    number = models.PositiveBigIntegerField()
    amount_of_seats = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return f"{self.type_of_railcar} - {self.train}"


class Discount(models.Model):
    """ """

    discount_code = models.CharField(max_length = 50,
        validators=[RegexValidator(
            regex="^[A-Z]{2}[0-9]{8}"
        )]
        )
    discount = models.PositiveBigIntegerField() 

    def __str__(self) -> str:
        return super().__str__()   


class RailCarType(models.Model):
    """ """

    name = models.CharField(("railcar_type_name"), max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Ticket(models.Model):
    """ """

    train = models.ForeignKey(Train, verbose_name=(""), on_delete=models.CASCADE)
    route = models.ForeignKey(Route, verbose_name=(""), on_delete=models.CASCADE)
    railcar_number = models.PositiveIntegerField((""))
    seat = models.PositiveIntegerField((""))
    purchase_date = models.DateField((""), auto_now=False, auto_now_add=False)
    departure_date = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    is_taken = models.BooleanField((""), default=False)

    def __str__(self) -> str:
        return ""


class OrderTicket(models.Model):
    """ """

    ticket = models.ForeignKey(Ticket, verbose_name=(""), on_delete=models.CASCADE)
    start_point = models.ForeignKey(Station, verbose_name=("Start name"), 
        on_delete=models.CASCADE, related_name="point_start")
    end_point = models.ForeignKey(Station, verbose_name=("End name"), 
        on_delete=models.CASCADE, related_name="point_end")

    customer_name = models.CharField(("name"), max_length=50)
    customer_surname = models.CharField(("surname"), max_length=50)
    customer_patronymic = models.CharField(("patronymic"), max_length=50)

    discount = models.ForeignKey(Discount, verbose_name=(""), on_delete=models.CASCADE)
    price = models.PositiveIntegerField(("ticket price"))
    email = models.CharField(("customer email"), max_length=100,
        validators=[RegexValidator(
            regex="^[\w.]+@[\w-]+.+[\w-]{2,4}$"
        )]    )
    