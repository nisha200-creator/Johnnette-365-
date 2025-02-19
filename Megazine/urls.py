
from django.conf import settings
from django.urls import path
from Megazine import views
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("singlepage",views.singlepage,name='singlepage'),
    path("about",views.about,name='about'),
    path("articles",views.Articles,name='articles'),
    path("page",views.page,name='page'),  
    path("page2",views.page2,name='page2'),     

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)