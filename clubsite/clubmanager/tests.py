from django.test import TestCase


from clubmanager.models import Member

# Create your tests here.


class MemberModelTest(TestCase):
    def test_initials_format(self):
        m = Member(first_name='Donald',last_name='Trump')
        self.assertEqual(m.initials(),'DT')

