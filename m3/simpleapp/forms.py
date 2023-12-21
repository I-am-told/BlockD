from django import forms
from  .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'quantity',
            'category',
            'price',
            'material',
        ]
    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')

        if name == description:
            raise ValidationError(
                'Описание не может быть идентично названию'
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError(
                'Название должно начинаться с заглавной буквы'
            )
        return name

