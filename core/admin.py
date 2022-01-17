from django.contrib import admin

# Custom User
from django.contrib.auth import admin as auth_admin
from .models import User

# Forms User
from .forms import UserChangeForm
from .forms import UserCreationForm


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
