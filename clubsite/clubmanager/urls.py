from django.urls import path

from . import views

urlpatterns = [
    path('member/id/<int:member_id>', views.member, name="member_profile"),
    path('members', views.member_list),
]
