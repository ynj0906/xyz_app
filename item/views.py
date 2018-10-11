from itertools import count

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import ItemForm
from .models import Item, WishList

#from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


"""
class Page(ListView):
    model = Item #利用するモデル
    context_object_name = 'item_index' #オブジェクト名の設定（標準ではobject_listとなってしまう）
    template_name = 'item/list.html' #テンプレートページの指定
    paginate_by = 5 #1ページあたりのページ数
"""

@login_required
def index(request):
    #item一覧を取得し、辞書に格納
    items = Item.objects.all()
    #items = items.order_by("created_at").annotate(replies=count('name') - 1)
    #items = Item.objects.get(pk=pk)
    #items = Item.objects.all().order_by("created_at")
    paginator = Paginator(items, 50)
    page = request.GET.get('page', 1)
    page_obj = paginator.get_page(page)



    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(page)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)


    return TemplateResponse(request, 'item/list.html',{"items": items, "topics":topics, "page_obj": page_obj})


@login_required
def edit(request, item_id):
    # itemの取得（itemが存在しない場合404を表示）
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index'))
    else:
        form = ItemForm(instance=item)
        
    context = {'form': form, 'item': item}
    return TemplateResponse(request, 'item/edit.html', context=context)

@login_required
@require_POST
def delete(request, item_id):
    # itemの取得（itemが存在しない場合404を表示）
    item = get_object_or_404(Item, pk=item_id)
    item.delete()

    return HttpResponseRedirect(reverse('item_index'))

@login_required
@require_POST
def add_to_wish_list(request,item_id):
    item = get_object_or_404(Item, id=item_id)
    #wishlistの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)
    

    #wishlistに該当するitemを追加
    wish_list.items.add(item)

    return HttpResponseRedirect(reverse("wish_list_index"))

@login_required
@require_POST
def delete_from_wish_list(request, item_id):
    # itemの取得（itemが存在しない場合404を表示）
    item = get_object_or_404(Item, pk=item_id)

    # wish_listの取得（wish_listが存在しない新規に作成）
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # wish_listから該当するitemを削除
    wish_list.items.remove(item)

    return HttpResponseRedirect(reverse('wish_list_index'))

@login_required
def wish_list_index(request):
    # 欲しいものリストの取得
    wish_list, created = WishList.objects.get_or_create(user=request.user)

    # 欲しいものに含まれるitem一覧を取得し、辞書に格納
    context = {'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)



@login_required
#hello()関数
def hello(request):
    context = {"message": "メッセージ"}
    return TemplateResponse(request, "base.html", context)


def post(request, post_id):
    return HttpResponse("post_idは = {} です。".format(post_id))

@login_required
def title(request, title):
    return HttpResponse(request, "base.html")


