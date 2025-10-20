from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, gmail, password=None):
        if not username:
            raise ValueError('نام کاربری الزامی است')
        if not gmail:
            raise ValueError('جیمیل الزامی است')

        user = self.model(
            username=username,
            gmail=gmail,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, gmail, password=None):
        user = self.create_user(
            username=username,
            password=password,
            gmail=gmail
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name='نام کاربری')
    gmail = models.CharField(max_length=150, unique=True, verbose_name='ایمیل')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['gmail']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'