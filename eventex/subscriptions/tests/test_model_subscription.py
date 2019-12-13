from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Marcelo Garcia",
            email="marcelo@mail.com",
            cpf="12345678901",
            phone="11-99876-8976"
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Marcelo Garcia', str(self.obj))

    def test_paid_default_to_False(self):
        self.assertEqual(False, self.obj.paid)