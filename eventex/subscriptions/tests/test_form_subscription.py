from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        self.form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(self.form.fields))

    def test_cpf_is_digit(self):
        form = self.make_validated_form(cpf='ABCD5678901')

        self.assert_form_error_code(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='12345')

        self.assert_form_error_code(form, 'cpf', 'length')

    def assert_form_error_code(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Pedro Silva', cpf='12345678901', email='cliente@mail.com', phone='11-90872-9876')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
