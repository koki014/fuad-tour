from core.models import Logo, ContactInfo, SocialMedia
from tour.models import Country


def main(request):
    context = {
        'countries': Country.objects.all(),
        'logo': Logo.objects.last(),
        'contact_info': ContactInfo.objects.last(),
        'media': SocialMedia.objects.all(),
        'media_whatsapp': SocialMedia.objects.filter(media='whatsapp').last()
    }

    return context
