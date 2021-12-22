from account.forms import RegisterUserForm, LoginUserForm
from search_ticket.utils import DataMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render


class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    """Show register form"""

    form_class = RegisterUserForm
    template_name = "account/register.html"
    success_message = "User added successfully"
    success_url = reverse_lazy("sign_in")
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Registration", ico="menu/img/ico/home_pink.png"
        )
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):

    """Autorization class"""

    form_class = LoginUserForm
    template_name = "account/sign_in.html"
    error_message = "Something went wrong"
    success_message = f"Successfully sign in"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(title="Sign in", ico="menu/img/ico/home_pink.png")

        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(LogoutView, SuccessMessageMixin):

    next_page = "home"
    success_message = "Logout successfully"


def handle_not_found(request, exception):
    return render(request, "admin/404.html")


def handle_server_error(request):
    return render(request, "admin/500.html")


def handler_forbiden(request, exception):
    return render(request, "admin/403.html")


def handle_url_error(request, exception):
    return render(request, "admin/400.html", status=400)
