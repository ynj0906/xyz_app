#url関数のインポート
from django.conf.urls import url

from . import views

#ルーティングの設定

urlpatterns = [

    
    url(r"^$", views.index, name="item_index"),
#アイテムの更新
    url(r"^(?P<item_id>[0-9]+)/edit/$", views.edit, name="item_edit"),
    
#アイテムの削除
    url(r"^(?P<item_id>[0-9]+)/delete/$", views.delete, name="item_delete"),
    
#ほしいものリストへの追加
    url(r"^(?P<item_id>[0-9]+)/add/wish_list/$", views.add_to_wish_list, name="item_add_wish_list"),
#ほしいものリストからの削除
    url(r"^(?P<item_id>[0-9]+)/delete/wish_list/$",views.delete_from_wish_list, name="item_delete_wish_list"),
#ほしいものリストの一覧
    url(r"^wish_list/$", views.wish_list_index, name="wish_list_index"),
    url(r"^hello/$", views.hello, name="hello"),
    url(r"^post/(?P<post_id>\d+)/$", views.post, name="post"),
    url(r"^hello/$", views.title, name="title"),
    #url(r'^$', views.Page.as_view(), name="item_index"),

    ]
