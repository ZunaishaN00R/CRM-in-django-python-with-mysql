from django import forms 
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm


User=get_user_model()

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email' , 
            'username',
            'first_name',
            'last_name',
            
        )

# from django import forms
# from .models import Agent  # Import your Agent model

# class AgentModelForm(forms.ModelForm):
#     user = forms.ForeignKey(User, on_delete=models.CASCADE)  # Replace 'User' with the actual User model you have
#     # Other fields and form configurations go here

#     class Meta:
#         model = Agent
#         fields = '__all__'  # Example, you can specify the fields you want to include
