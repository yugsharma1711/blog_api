
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls')),
    path('api/user/' ,include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('documentation/', get_schema_view(title="Documentation", description="OPEN_API", version="1.0.0")),
    path('',include_docs_urls(title='Documentation'))
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

