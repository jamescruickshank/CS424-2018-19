from django.shortcuts import render
from django.http import HttpResponse

from IPython import embed


from clubmanager.models import Member

# Create your views here.


def member(request,member_id):
    member = Member.objects.get(id=member_id)

    response = render(request,'clubmanager/member_detail.html',{
        'member':member
        })
    return response

def member_list(request):
    members = Member.objects.all()

    response=render(request,'clubmanager/member_list.html',{
            'members':members
    })
    return response
