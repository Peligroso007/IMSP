import os

from django import template

register = template.Library()


@register.filter(name='is_teacher_or_admin')
def is_teacher_or_admin(user):
    if user.profile.role == 1 or user.profile.role == 2:
        return True
    return False