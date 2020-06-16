from django.contrib import admin
from .models import material
from .models import Book
from .models import Article
from .models import About
from .models import People

# Register your models here.
admin.site.register(material)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(People)
admin.site.register(About)
