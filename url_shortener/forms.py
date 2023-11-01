from django import forms

class UrlForm(forms.form):
    long_url=forms.URLField(label="URL")

