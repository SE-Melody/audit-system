from django import forms

from StudApp.models import Apply

class BettingForm(forms.ModelForm):
    # admin_mileage = forms.IntegerField(max_value=160)
    # apply_time = forms.DateTimeField

    class Meta:
        model = Apply
        fields = ['admin_mileage']
        labels = {
            'admin_mileage': '마일리지'
        }