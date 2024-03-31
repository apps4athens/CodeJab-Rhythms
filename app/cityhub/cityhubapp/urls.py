from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", LogoutView.as_view(next_page='home'), name="logout"),
    path("create-event/", views.create_event, name="create-event"),
    path("create-complaint/", views.create_complaint, name="create-complaint"),
    # Redirect the base URL to the login page
    path('', RedirectView.as_view(url='/home', permanent=True))
]