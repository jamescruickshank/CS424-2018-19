
from rest_framework import serializers

from clubmanager.models import Member, CommitteeRole


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('first_name','last_name','date_of_birth')


class CommitteeRoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommitteeRole
        fields = ('name','member')
