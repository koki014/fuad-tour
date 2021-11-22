from django.shortcuts import render
from tour.models import *
from tour.forms import ApplyForm


def tour_detail(request, id):
    tour = Tour.objects.filter(id=id).last(),
    for obj in tour:
        print(obj.title)
    error = ''
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            if form.is_valid():
                reservation = form.save()
                tour = Tour.objects.get(id=int(id))
                reservation.name_tour = tour
                reservation.save()


        else:
            error = 'Məlumat səhv daxil edilib!'
    form = ApplyForm()
    context = {
        "info": Reservation.objects.last(),
        "tour_inside": Tour.objects.filter(id=id).last(),
        "rest": Tour.objects.all()[:4],
        'form': form,
        'error': error,

    }
    return render(request, 'tour_detail.html', context)


def country_detail(request, id):
    country = Country.objects.filter(id=id).last()
    tours = Tour.objects.filter(country=country).all()

    context = {
        "tours": tours,
        "country": country,

    }
    return render(request, 'tours.html', context)
