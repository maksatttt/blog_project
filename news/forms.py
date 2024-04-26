from django import forms
from django.utils import timezone
from .models import Articles

class ArticlesForm(forms.ModelForm):
    image = forms.ImageField(label='Изображение', required=False)  # Добавляем поле для загрузки изображения

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'image']  # Включаем поле изображения в форму

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.date = timezone.now()  # Устанавливаем текущую дату и время
        if commit:
            instance.save()
        return instance