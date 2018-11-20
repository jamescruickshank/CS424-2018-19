from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth.decorators import login_required

from IPython import embed

from clubmanager.forms import MemberForm

from clubmanager.models import Member, CommitteeRole

from clubmanager.serializers import MemberSerializer, CommitteeRoleSerializer


from rest_framework import viewsets

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


def member_update(request,member_id):
    member = Member.objects.get(id=member_id)
    if request.method=="POST":
        form = MemberForm(request.POST, instance=member) # populates the form fields with POST data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('member_profile',kwargs={'member_id':member_id}))
        else:
            return HttpResponseRedirect('/')

    form = MemberForm(instance=member)
    return render(request,'clubmanager/member_update.html',{
            'form':form
        })


def ajax_last_name_update(request,member_id):
    m = Member.objects.get(id=member_id)
    return HttpResponse(m.last_name)


# some class based viewsets for the REST api

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CommitteeRoleViewSet(viewsets.ModelViewSet):
    queryset = CommitteeRole.objects.all()
    serializer_class = CommitteeRoleSerializer
