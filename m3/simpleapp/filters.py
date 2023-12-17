from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем, должен чем-то напоминать нам дженерики


class ProductFilter(FilterSet):
    # material = ModelChoiceFilter(
    #     field_name='productmaterial__material',
    #     queryset=Material.objects.all(),
    #     # label='Material',
    #     # empty_label='любой',
    # )

    class Meta:
        model = Product
        fields = {
            'productmaterial__material': ['exact'],
            'name': ['icontains'],
            # Количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',
                'gt',
            ],
        }