from django import forms
from firstapp.models import invalid_list
from django.core.exceptions import ValidationError

#检查comment是否满足字数要求
def words_validator(comment):
    if len(comment)<4:
        raise ValidationError('Not enough words')

#检查是否有违禁单词
def comment_validator(comment):
    IL = invalid_list.objects.all()

    for a in IL:

        if str(a) in comment:
            raise ValidationError('Your comment contains invalid words,please check it again.')

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(widget=forms.Textarea(attrs=None),
                              error_messages={
                                  'required':'Sorry, need words'

                                 },
                              validators=[words_validator,comment_validator]
                              )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

