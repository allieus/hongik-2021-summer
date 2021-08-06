from django import forms

from journal.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 유저로부터 입력받을 필드들의 이름을 나열
        fields = ["journallist", "title", "content", "photo"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["message"]
