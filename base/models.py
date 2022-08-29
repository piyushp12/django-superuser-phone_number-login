from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import random


# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone number')

        user = self.model(
            phone_number=self.phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.model(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.is_superuser = True
        if user.is_superuser: user.user_type = "Admin"
        user.is_staff = True
        user.save(using=self._db)
        return user




class MyUser(AbstractBaseUser):
    phone_number = models.CharField("Phone Number",max_length=10, unique=True)
    full_name = models.CharField("Full Name", max_length=255, blank=True, null=True)
    email=models.EmailField("Email", max_length=255, blank=True, null=True)
    avatar = models.ImageField("Avatar", upload_to="Profile/%Y/%m/%d/", blank=True, null=True)
    dob = models.DateField(
        "Date of Birth", max_length=20, blank=True, null=True),
    address = models.TextField("Address", blank=True, null=True)
    otp=models.CharField("OTP", max_length=4, blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    otp_verify = models.BooleanField(default=False)
    is_superuser = models.BooleanField("Super User", default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def create_otp(self):
        otp = random.randint(1000, 9999)
        self.otp = otp
        self.otp_varify = False
        self.save()
        return otp
        
    class Meta:
        verbose_name_plural = 'My User'