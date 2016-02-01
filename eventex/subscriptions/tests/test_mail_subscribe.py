from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Gabriel Cardoso', cpf='12345678901',
                    email='gabriel_cardoso010@yahoo.com.br', phone='00-0000-0000')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'gabriel_cardoso010@yahoo.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['gabriel_cardoso010@yahoo.com.br', 'gabriel_cardoso010@yahoo.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_budy(self):
        contents = [
            'Gabriel Cardoso',
            '12345678901',
            'gabriel_cardoso010@yahoo.com.br',
            '00-0000-0000',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

