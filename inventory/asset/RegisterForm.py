from django import forms
from .models import Registration

# class PizzaForm(forms.Form):
# 	toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
# 	size = forms.ChoiceField(label='Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])


class RegisterForms(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'uname', 'pwd', 'cpwd']
        labels = {'name': 'Name', 'email': 'E-mail', 'phone': 'Phone', 'uname': 'Username', 'pwd': 'Password', 'cpwd': 'Confirm Password'}
        # widgets = {'pwd':forms.PasswordInput}


