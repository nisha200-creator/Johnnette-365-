
from django.conf import settings
from django.urls import path
from Megazine import views
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("article", views.article, name="article"),
    path("singlepage",views.singlepage,name='singlepage'),
    path("about",views.about,name='about'),
         
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)