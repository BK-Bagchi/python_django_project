from django import forms


class user_form(forms.Form):
    user_name = forms.CharField(max_length=20, label="Full Name", widget=forms.TextInput(
        attrs={'placeholder': 'Enter you full name', 'style': 'width: 300px'}))
    user_email = forms.EmailField(max_length=20, label="Email", widget=forms.TextInput(
        attrs={'placeholder': 'Enter your email'}))
    user_birthday = forms.DateField(label="Birthday",
                                    widget=forms.TextInput(attrs={'type': 'date'}))

# user_name, user_email, user_birthday works as user input fields that we used to make with HTML
