from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from marque.views import  ListeMarques #list_Marque,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('marque/',include('marque.urls')),
    path('modele/',include('modele.urls')),
    path('version/',include('version.urls'))

]

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
