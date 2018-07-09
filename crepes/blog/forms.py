from django import forms
from django.template.defaultfilters import slugify
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:

        model = Article

        exclude = ('date', )

    def clean_slug(self):
        # Permet juste d'auto-remplir le champ slug
        # en fonction du titre
        titre = self.cleaned_data['titre']
        slug = slugify(titre)
        return slug


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('date', 'is_visible', 'article', )
