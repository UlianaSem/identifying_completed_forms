from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import FieldType, Field, Form


class FormTestCase(APITestCase):
    FIELDS = [("field_name_1", "email"), ("field_name_2", "phone")]

    def setUp(self):

        for type_ in ["email", "phone", "text", "date"]:
            FieldType.objects.create(field_type=type_)

        for field in self.FIELDS:
            Field.objects.create(name=field[0], type=FieldType.objects.get(field_type=field[1]))

        self.form = Form.objects.create(name="Form email, phone")
        self.form.fields.set(Field.objects.filter(pk__in=[1, 2]))

    def test_get_form(self):
        first_response = self.client.post(
            reverse('main:get-form') + '?' + urlencode({"field_name_1": "aa@aa.ru", "field_name_2": "+79505619328"}, doseq=True)
        )

        self.assertEquals(first_response.status_code, status.HTTP_200_OK)
        self.assertEquals(first_response.json(), {"template_name": "Form email, phone"})

        second_response = self.client.post(
            reverse('main:get-form') + '?' + urlencode({"field": "phone"}, doseq=True)
        )

        self.assertEquals(second_response.status_code, status.HTTP_200_OK)
        self.assertEquals(second_response.json(), {"field": "text"})
