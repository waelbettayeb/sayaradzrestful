
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from system_api.views import list_Model
from system_api.views import list_Marque
from system_api.views import list_Version

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listmodel', list_Model),
    path('listmarque', list_Marque),
    path('listVersion', list_Version),
]

