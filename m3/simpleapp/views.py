from datetime import datetime
from pprint import pprint
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .filters import ProductFilter



class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2 # вот так мы можем указать количество записей на странице

    # Метод get_contex_data позволяет нам изменить набор данных,
    # который будет передан в шаблон

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в виде объекта класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем отфильтрованный список товров
        return self.filterset.qs


    def get_context_data(self, **kwargs):

        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'
        # context['time_mow'] = datetime.utcnow()   ------- мы изавбляемся от переменной time_mow
        # поскольку мы теперь используем тег current_time
        # Добавим еще одну перменную, что бы на ее примере
        # расммотреть работу еще одного фильтра
        context['next_sale'] = None
        # Добавляем объект фильтрации в контекст
        context['filterset'] = self.filterset
        pprint(context)
        return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'
