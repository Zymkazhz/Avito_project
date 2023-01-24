from decimal import Decimal
from django.conf import settings
from appsite.models import Car, Scooters, Motorcycles


class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        car_objects = Car.objects.filter(id__in=product_ids)
        scooters_objects = Scooters.objects.filter(id__in=product_ids)
        motorcycles_objects = Motorcycles.objects.filter(id__in=product_ids)
        ads = []
        ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                     'published_date': model.published_date, 'id': model.pk,
                     'image_one': model.gallery.image_one} for model in car_objects])
        ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                     'published_date': model.published_date, 'id': model.pk,
                     'image_one': model.gallery.image_one} for model in scooters_objects])
        ads.extend([{'brand': model.brand, 'price': model.price, 'category': model.category,
                     'published_date': model.published_date, 'id': model.pk,
                     'image_one': model.gallery.image_one} for model in motorcycles_objects])

        cart = self.cart.copy()
        for product in ads:
            cart[str(product['id'])]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        """
        Удаляем товар
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()
