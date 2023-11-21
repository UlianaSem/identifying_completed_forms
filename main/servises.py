import re

from main.models import Form, Field, FieldType

ROW_DATE = [r"\d\d.\d\d.\d{4}", r"\d{4}-\d\d-\d\d"]
ROW_PHONE = [r"\s7\s\d{3}\s\d{3}\s\d\d\s\d\d", r"\s7\d{10}"]
ROW_EMAIL = r"\w+?@\w+?\.[a-zA-Z]{2,6}"


def check_format(data):
    """
    Проверяет к какому типу данных относятся параметры
    :param data: данные для проверки
    :return: словарь с типами данных
    """
    return_data = {}

    for item, value in data.items():
        if re.match(ROW_DATE[0], value):
            date = value.split('.')

            if '00' < date[0] < '32' and '00' < date[1] < '13':
                return_data[item] = 'date'
            else:
                return_data[item] = 'text'

        elif re.match(ROW_DATE[1], value):
            date = value.split('-')

            if '00' < date[2] < '32' and '00' < date[1] < '13':
                return_data[item] = 'date'
            else:
                return_data[item] = 'text'

        elif re.match(ROW_PHONE[0], value) or re.match(ROW_PHONE[1], value):
            return_data[item] = 'phone'

        elif re.match(ROW_EMAIL, value):
            return_data[item] = "email"

        else:
            return_data[item] = 'text'

    return return_data


def search_form(valid_data):
    """
    Ищет шаблон формы в базе данных
    :param valid_data: форма для поиска
    :return: шаблон формы
    """
    field_query = Field.objects.filter(name__in=valid_data.keys()).filter(type__in=FieldType.objects.filter(
        field_type__in=valid_data.values()).values_list("id", flat=True))

    forms_with_fields = Form.objects.filter(pk__in=[form.pk for form in Form.objects.all()
                                                    if field_query.intersection(form.fields.all())])

    forms_with_another_fields = Form.objects.filter(pk__in=[form.pk for form in Form.objects.all()
                                                            if form.fields.all().difference(field_query)])

    forms = forms_with_fields.difference(forms_with_another_fields)

    if [form for form in forms if form.fields.count() == len(valid_data)]:
        form = forms[0]

    else:
        form = forms.first()

    return form
