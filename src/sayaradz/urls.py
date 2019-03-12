from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.static import serve

from marque.views import  ListeMarques #list_Marque,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('marque/',include('marque.urls')),
    path('modele/',include('modele.urls')),
    path('version/',include('version.urls')),
    path('option/', include('option.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})

]

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
