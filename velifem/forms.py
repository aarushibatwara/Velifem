from django import forms

from .models import SOS
from .models import Adoption
from .models import Donation
#from .models import Registration
# from .models import Login

class SOS(forms.ModelForm):
    class Meta:
        model = SOS
        fields = ['name', 'email', 'phone_number', 'issue_description', 'location', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email ID'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'issue_description': forms.TextInput(attrs={'placeholder': 'Describe the Issue'}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'photo': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class Adoption(forms.ModelForm):
    #animal_type = forms.ChoiceField(choices=(('1', 'Dog'), ('2', 'Cat'), ('3', 'Bird'), ('4', 'Hamster'), ('5', 'Fish')))
    #breed = forms.ChoiceField(choices=(('1','Golden Retreiver'),('2','Labrador'),('3','Shih Tzu'),('4','Indian Periah'),('5','Siberian Husky'),('6','British Shorthair'),('7','Persian Cat'),('8','Maine Coon'),('9','Scotish Fold'),('10','Siamese Cat'),('11','Syrian Hamster'),('12','Chinese Hamster'),('13','Budgerigar'),('14','Cockatiel'),('15','Black Moor'),('16','Golden Fish')))
    #annual_income = forms.ChoiceField(choices=(('1', '0 - 300,000'), ('2', '300,000 - 500,000'), ('3', '500,000 - 700,000'), ('4', '700,000 - 900,000'), ('5', '900,000 - 1,100,000'), ('6', '> 1,100,000')))
    class Meta:
        model = Adoption
        fields = ('first_name', 'last_name', 'email', 'country', 'state', 'city', 'country_code', 'contact_number', 'permanent_address', 'notes')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Last Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Email ID', 'required': True}),
            'country': forms.TextInput(attrs={'class': 'address', 'placeholder': 'Country', 'required': True}),
            'state': forms.TextInput(attrs={'class': 'address', 'placeholder': 'State', 'required': True}),
            'city': forms.TextInput(attrs={'class': 'address', 'placeholder': 'City', 'required': True}),
            'country_code': forms.TextInput(attrs={'id': 'myNum', 'placeholder': 'Country Code', 'maxlength': 3, 'required': True}),
            'contact_number': forms.TextInput(attrs={'id': 'myNumtwo', 'placeholder': 'Contact Number', 'maxlength': 10, 'required': True}),
            #'animal_type': forms.Select(attrs={'class': 'purpose', 'required': True}),
            #'breed': forms.Select(attrs={'class': 'type', 'required': True}),
            #'annual_income': forms.Select(attrs={'class': 'income', 'required': True}),
            'permanent_address': forms.Textarea(attrs={'id': 'comments', 'placeholder': 'Please write additional comments here (if any).', 'rows': 4, 'cols': 40, 'name': 'comments'}),
            'notes': forms.Textarea(attrs={'id': 'comments', 'placeholder': 'Please write additional comments here (if any).', 'rows': 4, 'cols': 40, 'name': 'comments'}),
        }

class Donation(forms.ModelForm):
    """purpose = forms.ChoiceField(choices=(('1', 'General Donation'),('2', 'To feed the animals'),('3', 'For veterinary care'),('4', 'For building homes for animals'),('5', 'Towards other specific cause')))
    donation_type = forms.ChoiceField(choices=(('1', 'One Time Donation'),('2', 'Monthly Donation'),('3', 'Quarterly Donation'),('4', 'Half-Yearly Donation'),('5', 'Yearly Donation')))
    currency = forms.ChoiceField(choices=(('1', 'USD'),('2', 'EUR'),('3', 'JPY'),('4', 'GBP'),('5', 'CHF'),('6', 'CAD'),('7', 'AUD'),('8', 'ZAR'),
        ('9', 'AED'),
        ('10', 'INR'),))
    payment_method = forms.ChoiceField(choices=(('credit_card', 'Credit / Debit Card'),
        ('e_wallet', 'E-Wallets'),
        ('upi', 'UPI'),
        ('money_order', 'Money Order / Demand Draft')))"""
    class Meta:
        model = Donation
        fields = ['first_name', 'last_name', 'email', 'country', 'state', 'city', 'country_code', 'contact_number','amount','notes']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'First Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'name', 'placeholder': 'Last Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Email ID', 'required': True}),
            'country': forms.TextInput(attrs={'class': 'address', 'placeholder': 'Country', 'required': True}),
            'state': forms.TextInput(attrs={'class': 'address', 'placeholder': 'State', 'required': True}),
            'city': forms.TextInput(attrs={'class': 'address', 'placeholder': 'City', 'required': True}),
            'country_code': forms.TextInput(attrs={'id': 'myNum', 'placeholder': 'Country Code', 'maxlength': '3', 'required': True}),
            'contact_number': forms.TextInput(attrs={'id': 'myNumtwo', 'placeholder': 'Contact Number', 'maxlength': '10', 'required': True}),
           """ 'purpose': forms.Select(attrs={'class': 'purpose', 'required': True}),
            'other_purpose': forms.TextInput(attrs={'class': 'others', 'placeholder': 'If Other specific cause, Please Mention'}),
            'donation_type': forms.Select(attrs={'class': 'type', 'required': True}),
            'currency': forms.Select(attrs={'class': 'currency', 'required': True}),
            'payment_method': forms.RadioSelect(attrs={'class': 'paymentmethod', 'required': True}),"""
            'amount': forms.TextInput(attrs={'class': 'others', 'placeholder': 'Amount', 'required': True}),
            'notes': forms.Textarea(attrs={'id': 'comments', 'placeholder': 'Please write additional comments here (if any).', 'rows': '4', 'cols': '40', 'name': 'comments'}),
        }
        


"""class Login(forms.Form):
    user_id = forms.CharField(max_length=30, label='User ID', widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'User ID'}))
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Enter Password'}))

class Meta:
    model = Login
    fields = ('user_id','password')

class Registration(UserCreationForm):
    email = forms.EmailField(max_length=254, label='Email ID', widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email ID'}), validators=[EmailValidator()])
    confirm_password = forms.CharField(max_length=30, label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Registration
        fields = ('user_id', 'email', 'password', 'confirm_password')"""