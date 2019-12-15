from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):

    def setUp(self):
        Subscription.objects.create(name='Pedro Silva', cpf='12345678901',
                                    email='cliente@mail.com', phone='11-90872-9876')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action_mark_as_paid(self):
        """Action mark_as_paid should be installed"""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid"""
        self.prepare_mock()

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user"""

        mock = self.prepare_mock()

        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def prepare_mock(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        real_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        return mock
