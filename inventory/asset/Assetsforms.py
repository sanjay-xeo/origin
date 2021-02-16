from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_name', 'asset_date', 'asset_category', 'asset_number']
        labels = {'asset_name': 'Asset Name', 'asset_date': 'Asset Date', 'asset_category': 'Asset Category', 'asset_number': 'Number of Assets'}



