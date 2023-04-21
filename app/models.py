from django.db.models import *
from django.contrib import admin
from django.http import HttpRequest
import uuid

# Create your models here.


class WebData(Model):
    profile_pic = ImageField(upload_to='images/')


class WebDataAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        base_add_permission = super().has_add_permission(request)
        if not WebData.objects.exists() and base_add_permission:
            return True   
        return False
    
    def has_delete_permission(self, *args) -> bool:
        return False


class HomePageImage(Model):
    image = ImageField(upload_to='images/')

    def __str__(self) -> str:
        return f"home page image {self.id}"

class BiographyPage(Model):
    quote1 = TextField(blank=True)
    paragraph1 = TextField()
    image1 = ImageField(upload_to='images/')
    image1_description = TextField(blank=True)

    quote2 = TextField(blank=True)
    paragraph2 = TextField()
    image2 = ImageField(upload_to='images/')
    image2_description = TextField(blank=True)


class BiographyPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        base_add_permission = super().has_add_permission(request)
        if not BiographyPage.objects.exists() and base_add_permission:
            return True   
        return False
    
    def has_delete_permission(self, *args) -> bool:
        return False


class GallerySection(Model):
    name = CharField(max_length=20, unique=True)
    image_description = ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.name.title()
    
class GalleryCategory(Model):
    name = CharField(max_length=200)
    description = TextField()
    section = ForeignKey(GallerySection, on_delete=CASCADE)

    def __str__(self) -> str:
        return str(self.name).title()

def get_uuid():
    return str(uuid.uuid4()).replace('-', '')

class Artwork(Model):
    uuid = UUIDField(default=get_uuid, editable=False)
    image = ImageField(upload_to='images/')
    category = ForeignKey(GalleryCategory, on_delete=CASCADE)
    description = TextField(max_length=400)

    def __str__(self) -> str:
        category_items = Artwork.objects.filter(category=self.category)
        category_id = 1
        for item in category_items.all():
            if item.id == self.id:
                break
            category_id += 1
        return f"{str(self.category).title()} {category_id}"


class PublicationsPageItem(Model):
    title = CharField(max_length=100)
    content_text = CharField(max_length=200)
    content_link = URLField()
    date = CharField(max_length=4)
    def __str__(self) -> str:
        return str(self.title.title())

class ExhibitionsPageItem(Model):
    date = CharField(max_length=200)
    title = CharField(max_length=200)
    choices = [
        ('past', 'Past'),
        ('ongoing', 'Ongoing'),
        ('upcoming', 'Upcoming'),
    ]
    occurence = CharField(default='past', choices=choices, max_length=10)  

    def __str__(self):
        return self.title

class Print(Model):
    image = ImageField(upload_to='images/')
    price = CharField(max_length=200)
    description = TextField()
    category = CharField(max_length=200)
    print_medium = CharField(max_length=200)
    size = CharField(max_length=200)

class NewslettersSuscriber(Model):
    name = CharField(max_length=200)
    email = EmailField()


    # facebook_link = URLField()
    # instagram_link = URLField()
    # twitter_link = URLField()
