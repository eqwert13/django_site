from django import forms


class PasswordForm(forms.Form):
    LENGTH_CHOICES = [(i, str(i)) for i in range(6, 33)]

    length = forms.ChoiceField(label="Длина пароля", choices=LENGTH_CHOICES, initial=12)
    uppercase = forms.BooleanField(label="A-Z", initial=True, required=False)
    lowercase = forms.BooleanField(label="a-z", initial=True, required=False)
    digits = forms.BooleanField(label="0-9", initial=True, required=False)
    symbols = forms.BooleanField(label="!@#$%^&*", initial=True, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["length"].widget.attrs.update(
            {
                "class": "w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-green-500 focus:border-green-500"
            }
        )
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update(
                    {
                        "class": "h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded"
                    }
                )
