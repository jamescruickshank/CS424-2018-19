from django.urls import path, include

from rest_framework import routers


from . import views


router = routers.DefaultRouter()
router.register(r'members',views.MemberViewSet)
router.register(r'committeeroles',views.CommitteeRoleViewSet)


urlpatterns = [
    path('member/id/<int:member_id>', views.member, name="member_profile"),
    path('members', views.member_list),
    path('member/update/id/<int:member_id>', views.member_update, name="member_update"),
    path('member/id/<int:member_id>/ajax_last_name', views.ajax_last_name_update),
    path('restapi/',include(router.urls))
]
