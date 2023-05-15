from django.urls import path
from .views import teacher_list, teacher_detail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', teacher_list, name='teacher_index'),
    path('<int:pk>/', teacher_detail, name='teacher_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)