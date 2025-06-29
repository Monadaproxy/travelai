from django import forms

class TripPlanForm(forms.Form):
    destination = forms.CharField(label="Город", max_length=100)
    start_date = forms.DateField(label="Дата начала", widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label="Дата окончания", widget=forms.DateInput(attrs={'type': 'date'}))
    interests = forms.CharField(
        label="Интересы (через запятую)",
        help_text="Например: музеи, еда, архитектура",
        widget=forms.Textarea(attrs={'rows': 2})
    )