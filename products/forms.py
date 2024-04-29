from django.forms import ModelForm, Textarea
from products.models import Comment


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'aria-label': 'Comentarios',
                'placeholder': 'Deja tu comentario',
                'id': 'formComment'
            }),
        }