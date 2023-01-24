from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_one = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    image_two = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    image_three = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    image_four = models.ImageField(upload_to=user_directory_path, null=True, blank=True)


class Car(models.Model):

    type_choises = [
        ('Продаю личный автомобиль', 'Продаю личный автомобиль'),
        ('Автомобиль приобретен на продажу', 'Автомобиль приобретен на продажу')
    ]

    pts_choises = [
        ('Оригинальный', 'Оригинал'),
        ('Дубликат', 'Дубликат'),
        ('Электронный', 'Электронный')
    ]

    communication_choises = [
        ('По телефону и в сообщениях', 'По телефону и в сообщениях'),
        ('В сообщениях', 'В сообщениях')
    ]

    fresh_choises = [
        ('Новый', 'Новый'),
        ('С пробегом', 'С пробегом')
    ]
    category = models.CharField(max_length=40, default='car')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Автор
    fresh = models.CharField(max_length=50, choices=fresh_choises, blank=True)
    ad_type = models.CharField(max_length=50, choices=type_choises)  # Вид обьявления
    color = models.CharField('Цвет', max_length=30)  # Цвет машины
    vin_body = models.CharField(max_length=30)  # Вин кузова
    gos_number = models.CharField(max_length=30)  # Гос.номер
    brand = models.CharField(max_length=30)  # Марка автомобиля
    mileage = models.PositiveIntegerField()  # Пробег автомобиля
    year = models.PositiveIntegerField()  # Год авто
    condition = models.CharField(max_length=30)  # Состояние авто
    pts = models.CharField(max_length=30, choices=pts_choises)  # Вид ПТС
    score_pts = models.PositiveIntegerField()  # Количество владельцев птс
    description = models.TextField()  # Описание
    price = models.IntegerField()  # Цена
    number_phone = models.CharField(max_length=30)  # Номер телефона для связи
    published_date = models.DateTimeField()  # Дата обьявления
    communication_method = models.CharField(max_length=40, choices=communication_choises, blank=True)  # Способ связи
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


#class GalleryCar(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
#    product = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='images')


class Scooters(models.Model):
    scooter_choises = [
        ('Скутер', 'Скутер'),
        ('Макси-скутер', 'Макси-скутер'),
        ('Мопед', 'Мопед'),
        ('Минибайк', 'Минибайк')
    ]
    engine_choises = [
        ('Бензин', 'Бензин'),
        ('Электро', 'Электро')
    ]
    pts_choises = [
        ('Оригинальный', 'Оригинал'),
        ('Дубликат', 'Дубликат'),
        ('Электронный', 'Электронный')
    ]

    communication_choises = [
        ('По телефону и в сообщениях', 'По телефону и в сообщениях'),
        ('В сообщениях', 'В сообщениях')
    ]
    category = models.CharField(max_length=40, default='scooters')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Автор
    published_date = models.DateTimeField()  # Дата обьявления
    title = models.CharField(max_length=100)  # Название обьявления
    vin_body = models.CharField(max_length=30)  # Вин кузова
    brand = models.CharField(max_length=30)  # Марка скутера
    type_scooter = models.CharField(max_length=50, choices=scooter_choises)  # Тип скутера
    year = models.PositiveIntegerField()  # Год выпуска
    type_engine = models.CharField(max_length=30, choices=engine_choises)  # Тип двигателя
    power = models.PositiveIntegerField()  # Мощность двигателя
    volume_engine = models.PositiveIntegerField()  # Обьём двигателя
    mileage = models.PositiveIntegerField()  # Пробег скутера
    condition = models.CharField(max_length=30)  # Состояние авто
    pts = models.CharField(max_length=30, choices=pts_choises)  # Вид ПТС
    score_pts = models.PositiveIntegerField()  # Количество владельцев птс
    price = models.PositiveIntegerField()  # Цена
    description = models.TextField()  # Описание
    number_phone = models.CharField(max_length=30)  # Номер телефона для связи
    communication_method = models.CharField(max_length=40, choices=communication_choises, blank=True)  # Способ связи
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


#class GalleryScooters(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
#    product = models.ForeignKey(Scooters, on_delete=models.CASCADE, related_name='images')


class Motorcycles(models.Model):
    scooter_choises = [
        ('Скутер', 'Скутер'),
        ('Макси-скутер', 'Макси-скутер'),
        ('Мопед', 'Мопед'),
        ('Минибайк', 'Минибайк')
    ]
    engine_choises = [
        ('Бензин', 'Бензин'),
        ('Электро', 'Электро')
    ]
    pts_choises = [
        ('Оригинальный', 'Оригинал'),
        ('Дубликат', 'Дубликат'),
        ('Электронный', 'Электронный')
    ]

    communication_choises = [
        ('По телефону и в сообщениях', 'По телефону и в сообщениях'),
        ('В сообщениях', 'В сообщениях')
    ]
    category = models.CharField(max_length=40, default='motorcycles')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Автор
    published_date = models.DateTimeField()  # Дата обьявления
    title = models.CharField(max_length=100)  # Название обьявления
    vin_body = models.CharField(max_length=30)  # Вин кузова
    brand = models.CharField(max_length=30)  # Марка скутера
    type_scooter = models.CharField(max_length=50, choices=scooter_choises)  # Тип скутера
    year = models.PositiveIntegerField()  # Год выпуска
    type_engine = models.CharField(max_length=30, choices=engine_choises)  # Тип двигателя
    power = models.PositiveIntegerField()  # Мощность двигателя
    volume_engine = models.PositiveIntegerField()  # Обьём двигателя
    mileage = models.PositiveIntegerField()  # Пробег скутера
    condition = models.CharField(max_length=30)  # Состояние авто
    pts = models.CharField(max_length=30, choices=pts_choises)  # Вид ПТС
    score_pts = models.PositiveIntegerField()  # Количество владельцев птс
    price = models.PositiveIntegerField()  # Цена
    description = models.TextField()  # Описание
    number_phone = models.CharField(max_length=30)  # Номер телефона для связи
    communication_method = models.CharField(max_length=40, choices=communication_choises, blank=True)  # Способ связи
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

#class GalleryMotorcycles(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
#    product = models.ForeignKey(Motorcycles, on_delete=models.CASCADE, related_name='images')



