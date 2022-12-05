from django import forms
from django.core import validators


class ContactForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خود را وارد کنید', 'class': 'form_field'}),
        label="نام ",
        validators=[
            validators.MaxLengthValidator(100, "نام شما نمیتواند بیش از 100 کاراکتر باشد")])

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خانوادگی خود را وارد کنید', 'class': 'form_field'}),
        label="نام خانوادگی",
        validators=[
            validators.MaxLengthValidator(100, "نام خانوادگی شما نمیتواند بیش از 100 کاراکتر باشد")])

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'form_field'}),
        label="ایمیل",
        validators=[
            validators.MaxLengthValidator(200, "تعداد کاراکترهایایمیل شما نمیتواند بیش از ۲۰۰ کاراکتر باشد.")
        ])

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'عنوان پیام خود را وارد کنید', 'class': 'form_field'}),
        label="عنوان",
        validators=[
            validators.MaxLengthValidator(250, "تعداد کاراکترهای  شما نمیتواند بیش از 250 کاراکتر باشد.")
        ])

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'متن پیام خود را وارد کنید', 'class': 'form_field'}),
        label="متن پیام",
    )

