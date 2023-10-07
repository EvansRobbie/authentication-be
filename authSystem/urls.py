
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path(
        "docs/",
        include_docs_urls(
            title="Authentication Backend API Documentation"
        ),
    ),
    path('admin/', admin.site.urls),
    # third part libs urls
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('auth/', include('djoser.social.urls')),
    path('password/', include('account.urls'))
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
