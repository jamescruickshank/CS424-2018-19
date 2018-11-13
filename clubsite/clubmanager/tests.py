from django.test import TestCase, Client

from clubmanager.models import Member

from IPython import embed

# Create your tests here.


class MemberModelTest(TestCase):
    def setUp(self):
        Member.objects.create(first_name='Donald',last_name='Trump')
        Member.objects.create(first_name="Michael", last_name="Kelly")


    def test_initials(self):
        m = Member.objects.get(first_name="Michael")
        self.assertEqual(m.initials(),'MK')


class MemberDetailViewTest(TestCase):
    def setUp(self):
        Member.objects.create(first_name='Jim',last_name='Cruickshank')
        
    def test_member_detail_view(self):
        c = Client()
        response = c.get('/clubmanager/member/id/1')
        self.assertEqual(response.status_code,200)

