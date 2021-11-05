from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from book.views import main
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', main, name="main"),
    path('book/', include('book.urls')),
    path('solution/', include('solution.urls')),
    path('account/', include('account.urls')),
    path('mail/', include('mail.urls'),)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
