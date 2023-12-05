from django import forms as f
from blog_app import models as m


class BlogCreateForm(f.ModelForm):
    title = f.CharField(label='Заголовок', widget=f.TextInput(attrs={'class': 'my-same-widht'}))
    content = f.CharField(label='Содержимое', widget=f.Textarea(attrs={'class': 'my-big-textarea'}))
    preview = f.ImageField(label='Превью', required=False, widget=f.FileInput(attrs={'class': 'my-same-widht'}))
    is_published = f.BooleanField(label='Статус публикации',widget=f.CheckboxInput(attrs={'class': 'my-checkbox'}))

    class Meta:
        model = m.Blog
        fields = ['title', 'content', 'preview', 'is_published']