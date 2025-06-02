from django import forms;
from .models import *;


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'price',
            'retal_price_day',
            'rental_peroid',
            'total_rental_price',
            'pages',
            'statas',
            'category',
        
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'rental_peroid': forms.NumberInput(attrs={'class':'form-control', 'id':'rentalday'}),
            'total_rental_price': forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'statas': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }
    
