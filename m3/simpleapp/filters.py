from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Product, Material

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем, должен чем-то напоминать нам дженерики


class ProductFilter(FilterSet):
    material = ModelMultipleChoiceFilter(
        field_name='material',
        queryset=Material.objects.all(),
        label='Material',
        conjoined=True,
    )

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            # Количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',
                'gt',
            ],
        }