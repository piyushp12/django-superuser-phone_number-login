from django.shortcuts import render,redirect
from django.views import View
#  from base.custom_context_processor import subject_renderer as ct
# # Create your views here.
from django.contrib.auth import authenticate,login,logout
from .models import *



class HomeView(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        params = request.POST
        user = authenticate(phone_number=params["phone"], password=params["password"])
        if user is not None and user.user_type == "Admin":
            login(request,user)
            return redirect("app:dashboard")
        elif user is not None and user.user_type == "Farm":
            login(request, user)
            return redirect("farm:dashboard")
        elif user is not None and user.user_type == "Group":
            login(request, user)
            return redirect("group:dashboard")
        elif user is not None and user.user_type == "Staff":
            login(request, user)
            return redirect("staff:dashboard")
        else:
            return redirect("app:home")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("app:home")


class ForgotPasswordView(View):
    def get(self, request):
        return render(request, "common/forgot-password.html")
    def post(self, request):
        return redirect("app:verify-otp")

class VerifyOTPView(View):
    def get(self, request):
        return render(request, "common/otp-verify.html")
    def post(self, request):
        return redirect("app:set-password")

class SetPasswordView(View):
    def get(self, request):
        return render(request, "common/set-password.html")
    def post(self, request):
        return redirect("app:home")

class DashboardView(View):
    def get(self, request):
        return render(request, "dashboard.html")


class StaffManagementView(View):
    def get(self, request):
        return render(request, "admin/staff_management/list-farms-staff.html")