from django.forms import Form, CharField, IntegerField


class PersonForm(Form):
    name = CharField(label='Введите имя')
    age = IntegerField(label='Введите возраст')
