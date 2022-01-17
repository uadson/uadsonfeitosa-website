from django.shortcuts import render

from django.views.generic import TemplateView

from website.models import Post


class HomeView(TemplateView):

    template_name = 'website/home.html'


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'website/list.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__day=day)
    context = {'post': post}
    return render(request, 'website/detail.html', context)