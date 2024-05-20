from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_message(self):
        # Optional: Add custom validation logic here (e.g., minimum message length)
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError('Message must be at least 10 characters long.')
        return message
