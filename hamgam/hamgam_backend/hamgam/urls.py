from django.contrib import admin
from django.urls import path, include, re_path
from . import views
#from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
#schema_view = get_swagger_view(title='Hamgam API')
schema_view = get_schema_view(
   openapi.Info(
      title="Hamgam API",
      default_version='v1',
      description="This is hamgam's api viewssss",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="khoramism@khoramism.ir"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('mamad', views.mamad),

    path('api/admin/', admin.site.urls),
        # ...
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/ideas/', include('idea.urls')),
    path('api/skills/', include('skill.urls')),
    path('api/accounts/', include('account.urls')),
    path('api/docs/', include('docs.urls')),
    path("ckeditor/", include('ckeditor_uploader.urls')), # <-- here
    #path('api/accounts/', include('rest_auth.urls')),
    #path('api/swag', schema_view)
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


