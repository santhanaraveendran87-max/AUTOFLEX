from django.contrib import admin

# Register your models here.
from.models import user
admin.site.register(user)

from.models import work
admin.site.register(work)

from.models import show
admin.site.register(show)

from.models import spare
admin.site.register(spare)

from.models import feedback
admin.site.register(feedback)

from.models import carsell
admin.site.register(carsell)

from.models import bikesell
admin.site.register(bikesell)

from.models import carrent
admin.site.register(carrent)

from.models import bikerent
admin.site.register(bikerent)

from.models import BookingCarsell
admin.site.register(BookingCarsell)

from.models import BookingCarRent
admin.site.register(BookingCarRent)

from.models import Car_renting_transactions
admin.site.register(Car_renting_transactions)

