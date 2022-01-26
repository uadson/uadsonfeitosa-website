from django.shortcuts import render

from website.models import Post


def post_list(request):
    """
       Retorna uma lista de postagens na página principal
    """
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'website/home.html', context)
