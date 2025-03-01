# отредачено
from django import forms
from .models import Recipe, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
        }

class RecipeForm2(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label="Новая категория",
        help_text="Введите название новой категории, если её нет в списке"
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'categories': forms.CheckboxSelectMultiple()
        }

    def save(self, commit=True):
        recipe = super().save(commit=False)

        # Создаём новую категорию, если она введена
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            new_category, created = Category.objects.get_or_create(name=new_category_name)
            recipe.categories.add(new_category)

        if commit:
            recipe.save()
            self.save_m2m()  # Сохраняем многие-ко-многим связи

        return recipe


