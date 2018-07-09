from django.contrib import admin
from django.utils.text import Truncator

from .models import Article, Categorie, Comment


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('titre', 'auteur', 'date', 'is_visible', 'apercu_article')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Général', {
            'classes': ['collapse', 'extrapretty', ],
            'fields': ('auteur', 'categorie', 'titre', 'slug', 'is_visible',)
        }),

        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte du HTML.',
            'fields': ('contenu', )
        }),
    )

    # Colonnes personnalisees
    def apercu_article(self, article):
        """Retourne les 40 premiers caracteres
        du contenu de l'article + points de
        suspenssion si plus long"""
        return Truncator(article.contenu).\
            chars(40, truncate='...')

    # En tete de la colonne apercu_contenu
    apercu_article.short_description = 'Apercu du contenu'

    # Champs pre-remplis
    prepopulated_fields = {'slug': ('titre', ), }


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'apercu_commentaire', 'date', 'is_visible')
    list_filter = ('pseudo', 'contenu', 'is_visible')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('contenu',)

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (pseudo, visibilite)
        ('Général', {
            'classes': ['collapse', 'extrapretty', ],
            'fields': ('pseudo', 'is_visible',)
        }),

        # Fieldset 2 : contenu du commentaire
        ('Contenu du commentaire', {
            'description': 'Le formulaire n\'accepte pas du HTML.',
            'fields': ('contenu', )
        }),
    )

    # personalise la colonne
    def apercu_commentaire(self, comment):
        """Retourne les 50 premiers caracteres
        du contenu du commentaire + points de
        suspenssion si plus long"""
        return Truncator(comment.contenu).chars(50, truncate='...')

    # En tete de la colonne apercu_commentaire
    apercu_commentaire.short_description = 'Apercu du commentaire'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Categorie)
