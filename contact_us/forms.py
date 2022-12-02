from django import forms

from .models import ContactUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'title', 'text']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'placeholder': 'عنوان'}),
            'text': forms.Textarea(attrs={'placeholder': 'پیام'}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form_field require'
