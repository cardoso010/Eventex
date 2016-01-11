from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Gabriel Cardoso',
            cpf='12345678901',
            email='gabriel@cardoso.com.br',
            phone='00-00000000'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription mus have an outo created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Gabriel Cardoso', str(self.obj))
