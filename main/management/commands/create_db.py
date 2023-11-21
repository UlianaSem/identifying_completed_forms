from django.core.management import BaseCommand

from main.models import Field, FieldType, Form


class Command(BaseCommand):
    FIELDS = [("field_name_1", "email"), ("field_name_2", "phone"), ("field_name_3", "text"), ("email", "email"),
              ("field_name_1", "date"), ("field_name_2", "date"), ("field_name_4", "date")]

    FORMS = [("Form email, phone", [1, 2]), ("Form email, phone, text", [1, 2, 3]), ("Email", [4]), ("Date", [5]),
             ("Form email, date", [1,  6]), ("Form email, phone, text, name", [1, 2, 3, 7])]

    def handle(self, *args, **options):

        for type_ in ["email", "phone", "text", "date"]:
            FieldType.objects.create(field_type=type_)

        for field in self.FIELDS:
            Field.objects.create(name=field[0], type=FieldType.objects.get(field_type=field[1]))

        for form in self.FORMS:
            form_obj = Form.objects.create(name=form[0])
            form_obj.fields.set(Field.objects.filter(pk__in=form[1]))
