from django.test import TestCase
from shop.models import User, Tovar

# Create your tests here.

class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(login = 'zetilin', password = '1367')
        Tovar.objects.create(name = 'Crocsic', price = 3.3)

    def test_user_str(self):
        a = User.objects.get(id = 1)
        self.assertEqual(a.login, str(a)) 

    def test_tovar_str(self):
        a = Tovar.objects.get(id = 1)
        self.assertEqual(a.name, str(a)) 