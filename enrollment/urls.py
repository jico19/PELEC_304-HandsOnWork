from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('course.urls')),
    # path('', include('students.urls')),
    # path('', include('registrations.urls')),
    path('', include('online_enrollment.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
