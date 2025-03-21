import django_filters
from .models import FoodItem,Category

# class FoodItemFilter(django_filters.FilterSet):
#     # category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains', label='Category')
#     category = django_filters.ChoiceFilter(
#         field_name='category__name',
#         choices=[(category.name, category.name) for category in Category.objects.all()],  # Generate category choices
#         label='Category'
#     )
#     name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Search')
#     vegetarian = django_filters.BooleanFilter(field_name='is_vegetarian', label='Vegetarian')
#     vegan = django_filters.BooleanFilter(field_name='is_vegan', label='Vegan')

#     class Meta:
#         model = FoodItem
#         fields = ['category', 'name', 'vegetarian', 'vegan']
        
class FoodItemFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(
        field_name='category__name',
        choices=[(category.name, category.name) for category in Category.objects.all()],
        label='Category'
    )
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Search')
    vegetarian = django_filters.BooleanFilter(field_name='is_vegetarian', label='Vegetarian')
    vegan = django_filters.BooleanFilter(field_name='is_vegan', label='Vegan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.data:  # Pre-select the category from the URL
            self.filters['category'].field.initial = self.data['category']

    class Meta:
        model = FoodItem
        fields = ['category', 'name', 'vegetarian', 'vegan']
