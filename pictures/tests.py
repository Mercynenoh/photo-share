from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mercy= Author(first_name = 'Mercy', last_name ='Chep', email ='mercy@gmail.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.mercy,Editor))
