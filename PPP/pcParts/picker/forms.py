from django import forms
from .models import SavedSelections

class PCAssemblyForm(forms.ModelForm):
    class Meta:
        model = SavedSelections
        fields = [
            'case_id', 
            'cpu_cooler_id', 
            'cpu_id', 
            'internal_hard_drive_id', 
            'memory_id', 
            'motherboard_id', 
            'power_supply_id', 
            'gpu_id'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False 