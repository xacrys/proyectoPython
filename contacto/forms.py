from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "nombre"}
        ),
        max_length=12,
        min_length=5,
    )
    email = forms.EmailField(
        label="Correo",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "suemail@hotmail.com"}
        ),
        max_length=40,
        min_length=12,
    )
    content = forms.CharField(
        label="Contenido",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Aquí coloque su mensaje",
            }
        ),
        max_length=500,
        min_length=50,
    )
