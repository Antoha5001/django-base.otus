from django.test import TestCase

# Create your tests here.

class PgTest(TestCase):

    def test_false_this(self):
        print(self.assertFalse(True))

    def test_true_this(self):
        print(self.assertTrue(True))
