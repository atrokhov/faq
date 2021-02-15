from .models import Answer, UserLikes, UserDislikes
from django import forms

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('body',)
		widgets = {'question': forms.HiddenInput()}

class LikeForm(forms.ModelForm):
	class Meta:
		model = UserLikes
		fields = ()
		widgets = {'answer': forms.HiddenInput()}

class DislikeForm(forms.ModelForm):
	class Meta:
		model = UserDislikes
		fields = ()
		widgets = {'answer': forms.HiddenInput()}

class BestAnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ()
		widgets = {'answer': forms.HiddenInput()}