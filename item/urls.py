#url関数のインポート
from django.conf.urls import url

from . import views

#ルーティングの設定

urlpatterns = [
    url(r"^hello/$", views.hello, name="hello"),
    url(r"^post/(?P<post_id>\d+)/$", views.post, name="post"),
    ]
