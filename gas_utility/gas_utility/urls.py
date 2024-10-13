from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customers import views as customer_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls', namespace='customers')),
    path('support/', include('support.urls', namespace='support')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', customer_views.home, name='home'),  # Home page
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
