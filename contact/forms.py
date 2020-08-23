from django import forms as forms

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)
class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(
        widget= forms.Textarea(),
        initial = "Contact me for jobs and dev stuffs"
    )
    sender = forms.EmailField(required=False,)

    def clean_message(self):
        message = self.clean_data.get('message', '')
        num_words = len(message.split())
        if num_words < 15:
            raise forms.ValidationError("Number of words entered is not enough")
        return message
        