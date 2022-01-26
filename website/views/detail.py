from django.shortcuts import render

from website.models import Post


def post_detail(request, year, month, day, post):
    """
        Retorna o detalhamento de determinado post
    """
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__day=day)
    context = {'post': post}
    return render(request, 'website/detail.html', context)