# These tests exist to provide basic test coverage for fec-eregs (the component
# modules are already tested. We just want to make sure they're playing nicely
# with each other). When one of these tests fails, please write a more specific
# test to catch the actual problem.


from django.test import TestCase
from django.test import Client

class StatusTestCase(TestCase):
  def test_home_loads(self):
    response = Client().get('/')
    self.assertEqual(response.status_code, 200)

  def test_about_loads(self):
    response = Client().get('/about')
    self.assertEqual(response.status_code, 200)