from django import forms
from pybo.models import Question, Answer

# seems like django version DTO.
# there is ModelForm and Form class in django
# forms.Form is
# forms.ModelForm is connected with Model.
# so if you save the form, then you can save the data to the model.
# then this is entity. wtf
# Model Form needs the inner class Meta to connect with the model.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['title', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        # bootstrap classes for form.as_p()
        # we can use to auto generate the form in the template.
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        
        # translate generated labels name.
        labels = {
            'title': '제목',
            'content': '내용',
        }  


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }