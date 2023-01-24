from django import forms

from .models import Car, Gallery, Scooters, Motorcycles
from django.forms import ModelForm, TextInput, Select, FileInput, NumberInput, Textarea, ClearableFileInput


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['color', 'vin_body', 'ad_type', 'vin_body', 'gos_number', 'brand',
                  'mileage', 'condition', 'pts', 'score_pts', 'description', 'price',
                  'number_phone', 'communication_method', 'fresh', 'year']
        widgets = {
            "color": TextInput(attrs={'class': 'form',}),
            "ad_type": Select(attrs={'class': 'form'}),
            "vin_body": TextInput(attrs={'class': 'form_vin'}),
            "gos_number": TextInput(attrs={'class': 'form'}),
            "brand": TextInput(attrs={'class': 'form'}),
            "mileage": NumberInput(attrs={'class': 'form'}),
            "condition": TextInput(attrs={'class': 'form'}),
            "pts": Select(attrs={'class': 'form'}),
            "score_pts": NumberInput(attrs={'class': 'form'}),
            "description": Textarea(attrs={'class': 'form-desc'}),
            "price": NumberInput(attrs={'class': 'form'}),
            "number_phone": TextInput(attrs={'class': 'form'}),
            "communication_method": Select(attrs={'class': 'form'}),
            "fresh": Select(attrs={'class': 'form'}),
            "year": NumberInput(attrs={'class': 'form'})
        }


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image_one', 'image_two', 'image_three', 'image_four']
        widgets = {
            'image_one': FileInput(attrs={'class': 'form'}),
            'image_two': FileInput(attrs={'class': 'form'}),
            'image_three': FileInput(attrs={'class': 'form'}),
            'image_four': FileInput(attrs={'class': 'form'})
        }


class ScootersForm(forms.ModelForm):
    class Meta:
        model = Scooters
        fields = ['title', 'vin_body', 'brand', 'type_scooter', 'year', 'type_engine', 'power',
                  'volume_engine', 'mileage', 'condition', 'pts', 'score_pts', 'price',
                  'description', 'number_phone', 'communication_method']
        widgets = {
            'title': TextInput(attrs={'class': 'form', 'id': 'form-3'}),
            'vin_body': TextInput(attrs={'class': 'form'}),
            'brand': TextInput(attrs={'class': 'form'}),
            'type_scooter': Select(attrs={'class': 'form'}),
            'year': NumberInput(attrs={'class': 'form'}),
            'type_engine': Select(attrs={'class': 'form'}),
            'power': NumberInput(attrs={'class': 'form'}),
            'volume_engine': NumberInput(attrs={'class': 'form'}),
            'mileage': NumberInput(attrs={'class': 'form'}),
            'condition': TextInput(attrs={'class': 'form'}),
            'pts': Select(attrs={'class': 'form'}),
            'score_pts': NumberInput(attrs={'class': 'form'}),
            'price': NumberInput(attrs={'class': 'form'}),
            'description': TextInput(attrs={'class': 'form-desc'}),
            'number_phone': TextInput(attrs={'class': 'form'}),
            'communication_method': Select(attrs={'class': 'form'})
        }


class MotorcyclesForm(forms.ModelForm):
    class Meta:
        model = Motorcycles
        fields = ['title', 'vin_body', 'brand', 'type_scooter', 'year', 'type_engine', 'power',
                  'volume_engine', 'mileage', 'condition', 'pts', 'score_pts', 'price',
                  'description', 'number_phone', 'communication_method']
        widgets = {
            'title': TextInput(attrs={'class': 'form', 'id': 'form-3'}),
            'vin_body': TextInput(attrs={'class': 'form'}),
            'brand': TextInput(attrs={'class': 'form'}),
            'type_scooter': Select(attrs={'class': 'form'}),
            'year': NumberInput(attrs={'class': 'form'}),
            'type_engine': Select(attrs={'class': 'form'}),
            'power': NumberInput(attrs={'class': 'form'}),
            'volume_engine': NumberInput(attrs={'class': 'form'}),
            'mileage': NumberInput(attrs={'class': 'form'}),
            'condition': TextInput(attrs={'class': 'form'}),
            'pts': Select(attrs={'class': 'form'}),
            'score_pts': NumberInput(attrs={'class': 'form'}),
            'price': NumberInput(attrs={'class': 'form'}),
            'description': TextInput(attrs={'class': 'form-desc'}),
            'number_phone': TextInput(attrs={'class': 'form'}),
            'communication_method': Select(attrs={'class': 'form'})
        }