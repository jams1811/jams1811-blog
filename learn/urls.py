from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'learn'

urlpatterns = [
    path('', views.all_learn, name='all_learn'),
    path('books', views.book, name='book'),
    path('articles', views.article, name='article'),
    path('people', views.people, name='people'),
    path('about', views.about, name='about'),
    path('progress', views.progress, name='progress'),
    path('courses', views.course, name='course'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
