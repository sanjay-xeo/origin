from django import forms
from .models import AssetCat

# class PizzaForm(forms.Form):
# 	toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)
# 	size = forms.ChoiceField(label='Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])


class Assetcatform(forms.ModelForm):
    class Meta:
        model = AssetCat
        fields = ['cat_name']
        labels = {'cat_name': 'Category Name'}
        # widgets = {'pwd':forms.PasswordInput}


