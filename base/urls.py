from django.urls import path,include
from base . views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard",DashboardView.as_view(),name="dashboard"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("forgot-password", ForgotPasswordView.as_view(), name="forgot-password"),
    path("verify-otp", VerifyOTPView.as_view(), name="verify-otp"),
    path("set-password", SetPasswordView.as_view(), name="set-password"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
]