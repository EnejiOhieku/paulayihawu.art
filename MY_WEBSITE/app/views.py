from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage, get_connection
from .admin import *

# Create your views here

def hero_image_url(request):
    return request._current_scheme_host + WebData.objects.all()[0].profile_pic.url

def index(request):
    return redirect('home')


def home(request):
    images = HomePageImage.objects.all()
    
    return render(request, 'home.html', {'hero_image': hero_image_url(request), 'images': images})


def biography(request):
    page_content = BiographyPage.objects.all()[0]
    
    data = {
        'hero_image': hero_image_url(request),
        'quote1': page_content.quote1,
        'paragraph1': page_content.paragraph1,
        'image1': page_content.image1,
        'image1_description': page_content.image1_description,
        'quote2': page_content.quote2,
        'paragraph2': page_content.paragraph2,
        'image2': page_content.image2,
        'image2_description': page_content.image2_description,
    }

    return render(request, 'biography.html', data)


def gallery(request):
    sections = GallerySection.objects.all()
    return render(request, 'gallery.html', {'hero_image': hero_image_url(request), 'sections': sections})

def gallery_section(request, section):
    base_url = request._current_scheme_host
    section = GallerySection.objects.get(name=section)
    categories_query_set = GalleryCategory.objects.filter(section=section)
    categories = {}
    for category in categories_query_set:
        artworks_query_set = Artwork.objects.filter(category=category)
        for artwork in artworks_query_set:
            if not categories.get(category):
                categories[category] = [artwork]
            else:
                categories[category].append(artwork)

    return render(request, 'gallery_section.html', {'section': section, 'categories': categories})


def exhibitions(request):
    occurences = ['upcoming', 'ongoing', 'past']

    data = {
        'hero_image': hero_image_url(request),
        'exhibitions': {},
    }

    for occurence in occurences:
        query = ExhibitionsPageItem.objects.filter(occurence=occurence)
        if len(query) > 0:
            data['exhibitions'][occurence.title()] = list(query)

    return render(request, 'exhibitions.html', data)


def publications(request):
    data = {
        'hero_image': hero_image_url(request),
        'publications': PublicationsPageItem.objects.all(),
    }
    return render(request, 'publications.html', data)


def prints(request):
    return render(request, 'prints.html')


def contact(request):
    data = {
        'hero_image': hero_image_url(request),
    }
    return render(request, 'contact.html', data)


def cart(request):
    return render(request, 'cart.html')


def send_contact_request(request):
    if request.method == "POST":
        with get_connection(
            host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT, 
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS) as connection:

            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            body = f"SUBJECT: {subject}\n NAME: {name}\n EMAIL: {email}\n CONTENT: {message}"
            main_email = "enejiohieku@gmail.com"
            
            email_message = EmailMessage(subject=f'paulayihawu.art SITE CONTACT REQUEST', body=body, from_email=settings.EMAIL_HOST_USER, to=[main_email], connection=connection)
            email_message.content_subtype = 'html'
            result = email_message.send(fail_silently=True)
            #result = send_mail(subject=f'paulayihawu.art SITE CONTACT REQUEST', body=body, from_email=settings.EMAIL_HOST_USER, to=[main_email], connection=connection, html_message=body)
            response = "OK" if result == 1 else "Message not sent"
            return HttpResponse(response)


def send_order_request(request):
    return HttpResponse()
