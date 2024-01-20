from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, Paginator, EmptyPage, PageNotAnInteger



def post_list(request):
    object_list = Post.published.all()  # a list of the posts
    paginator = Paginator(object_list, 2)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'app1/post/list.html', dict(page=page, posts=posts))


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request, 'app1/post/detail.html', {'post': post})

