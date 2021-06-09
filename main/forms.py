from django import forms
from .models import Comment
from .models import Card
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'username', 'text', 'product', 'img'
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'number', 'username', 'month', 'year', 'num'
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 'password', 'email', 'first_name', 'last_name'
        ]