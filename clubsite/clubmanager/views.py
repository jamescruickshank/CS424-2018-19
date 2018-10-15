from django.shortcuts import render
from django.http import HttpResponse

from IPython import embed


from clubmanager.models import Member

# Create your views here.


def member(request,member_id):
    member = Member.objects.get(id=member_id)

    return HttpResponse('%s %s'%(member.first_name,member.last_name))

def member_list(request):
    members = Member.objects.all()
    embed()


    return HttResponse('This should be a list of members')
