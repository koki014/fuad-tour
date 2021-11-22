from django.contrib import admin

from tour.models import Tour, Day, TourImage, Country, Reservation

admin.site.register(Day)
admin.site.register(Country)
admin.site.register(Reservation)


class TourImageInline(admin.StackedInline):
    model = TourImage
    extra = 1


# Django Admin register
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]
    list_display = ('title', 'country',)
