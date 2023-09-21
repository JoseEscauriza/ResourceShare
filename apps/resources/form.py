from django import forms


class PostResourceForm(forms.Form):
    category_choices = [("Databases", "Databases"),
                        ("Programming languages", "Programming languages")]

    tag_choices = [("1", "Paid"), ("2", "Free"), ("3", "SQL"), ("4", "Python"),
                   ("5", "Django"), ("6", "Mid-level"), ("7", "Advanced"), ("8", "Beginner")]

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'title-input',
                   'placeholder': 'Enter a title'}))  # input type="text"

    link = forms.URLField(
        widget=forms.TextInput(
            attrs={'class': 'link-input',
                   'placeholder': 'Please enter a valid URL'}))  # input type="url"

    description = forms.CharField(
        widget=forms.Textarea)  # input type="textarea"

    category = forms.ChoiceField(
        widget=forms.RadioSelect, choices=category_choices)

    tags = forms.ChoiceField(
        widget=forms.RadioSelect, choices=tag_choices)
