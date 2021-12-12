from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Expense API",
      default_version='v1',
      description="Management Sysmtem for managing expenses",
      terms_of_service="https://www.optimizeincgh.com/policies/terms/",
      contact=openapi.Contact(email="contact@expenses.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('expenses/', include('expenses.urls')),
    path('income/', include('incomes.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

admin.site.site_header = 'Expenses'
admin.site.site_title = 'Expanses Panel'
admin.site.index_title = 'Expenses'
admin.site.enable_nav_sidebar = True