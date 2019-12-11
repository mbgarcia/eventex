from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Pedro Silva', cpf='12345678901', email='cliente@mail.com', phone='11-90872-9876')
        self.response = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_mail_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEquals(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'cliente@mail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Pedro Silva', '12345678901', 'cliente@mail.com', '11-90872-9876']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)