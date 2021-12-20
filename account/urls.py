from django.urls import path
from account.views import RegisterUser, LoginUser, LogoutUser


urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("sign_in/", LoginUser.as_view(), name="sign_in"),
    path("logout/<slug:admin_name>", LogoutUser.as_view(), name="logout")
]