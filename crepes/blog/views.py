from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import CommentForm


def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre; un formulaire pour commenter ainsi que
    les commentaires lies a cet article
    """
    article = get_object_or_404(Article, slug=slug)
    commentaires = article.comment_set.filter(is_visible=True)
    if len(list(commentaires)) > 0:
        coment = True
    form = CommentForm(request.POST or None)

    if form.is_valid():

        #variable de verification d'envoie du formulaire
        envoi = True

        #enregistrement dans la base de donnees
        form = form.save(commit=False)
        form.article = article
        form.save()
        return redirect('blog_lire', slug=slug)

    return render(request, 'blog/lire_article.html', locals())
