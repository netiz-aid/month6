from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import CustomTokenObtainPairView

from . import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/products/", include("product.urls")),
    path("api/v1/users/", include("users.urls")),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += swagger.urlpatterns