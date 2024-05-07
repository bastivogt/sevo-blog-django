from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="E-Mail")
    comment = forms.CharField(label="Kommentar", widget=forms.Textarea)