from django.urls import path
from .views import governers_index, full_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', governers_index, name='governers_index'),
    path('<int:pk>/', full_view, name='full_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)