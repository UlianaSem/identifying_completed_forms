from django.db import models


class FieldType(models.Model):
    field_type = models.CharField(max_length=100, verbose_name="название типа", unique=True)

    def __str__(self):
        return self.field_type

    class Meta:
        verbose_name = 'тип поля'
        verbose_name_plural = 'типы полей'


class Field(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    type = models.ForeignKey(FieldType, on_delete=models.CASCADE, verbose_name="тип поля")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'поле'
        verbose_name_plural = 'поля'


class Form(models.Model):
    name = models.CharField(max_length=100, verbose_name="название", unique=True)
    fields = models.ManyToManyField(Field, related_name="fields")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'
