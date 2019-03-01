from django import forms
from .models import NewCarModel


# linked to model
class NewCarForm(forms.ModelForm):
    class Meta:
        model = NewCarModel
        fields = '__all__'

    def clean_mpg(self):
        mpg = self.cleaned_data['mpg']
        if mpg < 20:
            raise forms.ValidationError('That is less than a truck!')
        if mpg > 500:
            raise forms.ValidationError('That is impossible in 2019!')

        return mpg

    def clean_modelYear(self):
        year = self.cleaned_data['modelYear']
        if year < 2019:
            raise forms.ValidationError('That is not new!!!')

        return year