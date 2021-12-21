from django.contrib import admin

from order_ticket.models import Discount, OrderTicket, RailCarType, Railcar, Ticket

# Register your models here.

@admin.register(Railcar)
class RailcarAdmin(admin.ModelAdmin):
    list_display = ('train','type_of_railcar', "number")
    fields = ('type_of_railcar', "train", "number", "amount_of_seats")


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_code','discount')
    fields = ('discount_code','discount')


@admin.register(RailCarType)
class RailCarTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('train', "route", "railcar_number", "seat", "purchase_date", "is_taken")
    fields = ('train', "route", "railcar_number", "seat", "purchase_date", "departure_date", "is_taken")


@admin.register(OrderTicket)
class OrderTicketAdmin(admin.ModelAdmin):
    list_display = ('ticket', "start_point", "end_point", "customer_name", "customer_surname", )
    readonly_fields = ('ticket', "start_point", "end_point", "customer_name", "customer_surname",
    "discount", "price", "email")
    fields = ('ticket', "start_point", "end_point", "customer_name", "customer_surname",
    "discount", "price", "email")

