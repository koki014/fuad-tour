from django.shortcuts import render
from core.models import Slider, Service, InfoBlock
from tour.models import Tour


def index(request):
    context = {
        'sliders': Slider.objects.all(),
        'sow_tur': Tour.objects.filter(show_popular=True).all(),
        'service': Service.objects.last(),
        'info_block': InfoBlock.objects.all()[:3]

    }

    return render(request, 'index.html', context)
