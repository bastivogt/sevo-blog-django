from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(label="Name", label_suffix="", max_length=100)
    email = forms.EmailField(label="E-Mail", label_suffix="")
    comment = forms.CharField(label="Kommentar", label_suffix="", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["comment"].widget.attrs["class"] = "form-control"
