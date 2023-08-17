from django.urls import path

from webapp_api.views import echo_view_add, echo_view_subtract, echo_view_multiply, echo_view_divide

app_name = "webapp_api"

urlpatterns = [
    path("echo/add/", echo_view_add, name="echo_view_add"),
    path("echo/subtract/", echo_view_subtract, name="echo_view_subtract"),
    path("echo/multiply/", echo_view_multiply, name="echo_view_multiply"),
    path("echo/divide/", echo_view_divide, name="echo_view_divide"),
]