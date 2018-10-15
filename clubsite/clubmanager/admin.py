from django.contrib import admin

# Register your models here.

from clubmanager.models import Member, CommitteeRole

admin.site.register(Member)
admin.site.register(CommitteeRole)
