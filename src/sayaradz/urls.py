from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from system_api.views import list_Model
from system_api.views import list_Marque
from system_api.views import list_Model_Marque
from system_api.views import liste_Marque, liste_Modele


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Automobiliste/consultations/listmodel', list_Model),
    path('Automobiliste/consultations/listmarque', list_Marque),
    path('Automobiliste/consultations/modelmarque', list_Model_Marque),
    path('Automobiliste/consultations/detailsmarque', liste_Marque.as_view()),
    path('Automobiliste/consultations/detailsmodel/<str:Id_Marque>', liste_Modele.as_view()),


]

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
