from django import forms


class VoteResultForm(forms.Form):
    polling_unit = forms.CharField()
    party = forms.ChoiceField(choices=[('PDP', 'PDP'), ('ACN', 'ACN'), ('DPP', 'DPP'), ('PPA', 'PPA'), ('JP', 'JP'), ('CDC', 'CDC'), ('ANPP', 'ANPP'), ('LABOUR', 'LABOUR'), ('CPP', 'CPP')])
    results = forms.CharField()