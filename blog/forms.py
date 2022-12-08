from django import forms

from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['created', 'parent']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form_field', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form_field', 'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class': 'form_field', 'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'class': 'form_field', 'placeholder': 'عنوان'}),
            'body': forms.Textarea(attrs={'class': 'form_field', 'placeholder': 'متن نظر'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form_field'
    #         visible.field.widget.attrs['class':'form_field'
