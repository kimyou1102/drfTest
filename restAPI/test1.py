from django.test import TestCase

class FixturesTestCase(TestCase):
  fixtures = ['restAPI/fixtures/initial_data.json']
  def test_it(self):
    print('test')
