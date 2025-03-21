from django import forms
from .models import FoodItem,Category

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'price', 'description', 'image', 'category', 'is_vegan', 'is_vegetarian']
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        category = cleaned_data.get("category")
        is_vegan = cleaned_data.get("is_vegan")
        is_vegetarian = cleaned_data.get("is_vegetarian")

        if FoodItem.objects.filter(name=name, category=category, is_vegan=is_vegan, is_vegetarian=is_vegetarian).exists():
            raise forms.ValidationError("A food item with this Name, Category, Vegan, and Vegetarian status already exists.")
        
        return cleaned_data

class MenuUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File")

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']