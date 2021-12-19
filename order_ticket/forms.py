from django import forms
from order_ticket.models import Ticket
from search_ticket.models import RoutTrain


class OrderSeatForm(forms.Form):
    """class of creating new post using modelform"""

    def __init__(self, route, *args, **kwargs):
        super(OrderSeatForm, self).__init__(*args, **kwargs)
        self.route = route

        a = [
            (elem, f"{elem.seat} {elem.is_taken}")
            for elem in Ticket.objects.filter(route=self.route)
        ]

        self.fields["like"] = forms.ChoiceField(choices=a)


class OrderRailcarForm(forms.Form):
    """class of creating new post using modelform"""

    def __init__(self, route, *args, **kwargs):
        super(OrderRailcarForm, self).__init__(*args, **kwargs)
        self.route = route

        a = [
            (elem, elem)
            for elem in range(
                1,
                RoutTrain.objects.filter(route=self.route)
                .first()
                .train.get()
                .number_of_railcar
                + 1,
            )
        ]

        print(Ticket.objects.filter(route=self.route))
        self.fields["like"] = forms.ChoiceField(choices=a)


class OrderTicketForm(forms.Form):
    """class of creating new post using modelform"""

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    surname = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    discount = forms.CharField(required=False, widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "validate"}))
    # date = forms.DateField(
    #     widget=DatePickerInput(format='%m/%d/%Y')
    # )
