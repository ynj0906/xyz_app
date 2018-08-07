from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    set_number = models.IntegerField("セット番号")
    name = models.CharField("名前", max_length=255)
    image_url = models.URLField("画像url", blank=True)
    rating = models.FloatField("レーティング", default=0)
    piece_count = models.IntegerField("ピース数", default=0)
    minifig_count = models.IntegerField("ミニフィング数", default=0)
    us_price = models.FloatField("US価格", default=0.0)
    owner_count = models.IntegerField("オーナー数", default=0)
    want_it_count = models.IntegerField("欲しい数", default=0)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return self.name

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    def __str__(self):
        return "wish kist - {}".format(self.user.username)
