from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from datetime import timedelta
import uuid


def get_activation_key_expires():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', null=True)
    avatar = models.ImageField('аватар', upload_to='avatars', blank=True)

    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expired(self):
        return now() > self.activation_key_expires

    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()

    def basket_total_cost(self):
        return sum(map(lambda x: x.product_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.quantity, self.basket.all()))

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
        return 1, {}
