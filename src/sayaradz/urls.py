from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from system_api.views import list_Model,list_Version
from system_api.views import list_Marque
from system_api.views import list_Model_Marque
from system_api.views import liste_Marque, liste_Modele,liste_Versions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Automobiliste/consultations/listmodel', list_Model,name='list_Model'),
    path('Automobiliste/consultations/listmarque', list_Marque,name='list_Marque'),
    path('Automobiliste/consultations/modelmarque', list_Model_Marque,name='list_Model_Marque'),
    path('Automobiliste/consultations/listVersion', list_Version,name='list_Version'),
    path('Automobiliste/consultations/detailsmarque', liste_Marque.as_view(), name='liste_Marque'),
    path('Automobiliste/consultations/detailsmodel/<str:Id_Marque>', liste_Modele.as_view(), name='liste_Modele.'),
    path('Automobiliste/consultations/detailsversion/<str:Id_Modele>', liste_Versions.as_view(), name='liste_Versions'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)