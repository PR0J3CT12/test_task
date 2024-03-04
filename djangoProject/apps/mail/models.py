from django.db import models


class Letter(models.Model):
    TYPE_CHOICES = (
        (0, 'Письмо'),
        (1, 'Заказное письмо'),
        (2, 'Ценное письмо'),
        (3, 'Экспресс-письмо'),
    )

    id = models.AutoField(primary_key=True)
    sender = models.CharField('ФИО отправителя', max_length=100)
    receiver = models.CharField('ФИО получателя', max_length=100)
    point_of_dispatch = models.CharField('Пункт отправки', max_length=100)
    point_of_receipt = models.CharField('Пункт получения', max_length=100)
    index_dispatch = models.IntegerField('Индекс места отправки')
    index_receipt = models.IntegerField('Индекс места получения')
    letter_type = models.IntegerField('Тип письма', choices=TYPE_CHOICES)
    weight = models.IntegerField('Вес письма')
    is_given = models.BooleanField(default=False)

    class Meta:
        db_table = 'letters'


class Parcel(models.Model):
    TYPE_CHOICES = (
        (0, 'Мелкий пакет'),
        (1, 'Посылка'),
        (2, 'Посылка 1 класса'),
        (3, 'Ценная посылка'),
        (4, 'Международная посылка'),
        (5, 'Экспресс-посылка'),
    )

    id = models.AutoField(primary_key=True)
    sender = models.CharField('ФИО отправителя', max_length=100)
    receiver = models.CharField('ФИО получателя', max_length=100)
    point_of_dispatch = models.CharField('Пункт отправки', max_length=100)
    point_of_receipt = models.CharField('Пункт получения', max_length=100)
    index_dispatch = models.IntegerField('Индекс места отправки')
    index_receipt = models.IntegerField('Индекс места получения')
    phone = models.CharField('Тип посылки', max_length=11)
    parcel_type = models.IntegerField('Тип посылки', choices=TYPE_CHOICES)
    amount = models.IntegerField('Сумма платежа')
    is_given = models.BooleanField(default=False)

    class Meta:
        db_table = 'parcels'
