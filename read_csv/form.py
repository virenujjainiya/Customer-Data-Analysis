from django import forms
from read_csv.models import csvs

class csvform(forms.ModelForm):
    class Meta():
        model=csvs
        fields=['csv_file',]