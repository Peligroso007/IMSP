from django.contrib.auth.models import User
from django.db.models import Q

from app.models import Profile

def get_all_user():
    users = User.objects.filter(~Q(id=1))
    return users

def get_user_by_id(user_id):
    return User.objects.get(pk=user_id)

def add_new_user(form):
    user = form.save(commit=False)
    user.is_active = False
    user.is_staff = 1
    user.save()
    user.profile.role = form.cleaned_data.get('role')
    user.profile.organization_id = form.cleaned_data.get('organization_id')
    user.profile.save()
    return user

def update_user(form):
    user = form.save(commit=False)
    user.profile.role = form.cleaned_data.get('role')
    user.profile.organization_id = form.cleaned_data.get('organization_id')
    user.profile.save()
    user.save()
    return user

def delete_user_by_id(pk):
    User.objects.get(pk=pk).delete()
    return True