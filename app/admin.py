from django.contrib import admin
from app.models import *


# Register your models here.
admin.site.register(WebData, WebDataAdmin)
admin.site.register(HomePageImage)
admin.site.register(BiographyPage, BiographyPageAdmin)
admin.site.register(GallerySection)
admin.site.register(GalleryCategory)
admin.site.register(Artwork)
admin.site.register(PublicationsPageItem)
admin.site.register(ExhibitionsPageItem)
admin.site.register(Print)
