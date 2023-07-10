from django.core.validators import EmailValidator
from django.db import models



class SOS(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator(message='Invalid email format')])
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    issue_description = models.TextField()
    location = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='sos_photos/')

    def __str__(self):
        return self.name


class Adoption(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(validators=[EmailValidator(message='Invalid email format')])
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=10)
    #animal_type = models.CharField(max_length=20, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Hamster', 'Hamster'), ('Fish', 'Fish')])
    #breed = models.CharField(max_length=50, choices=[('Golden Retreiver','Golden Retreiver'),('Labrador','Labrador'),('Shih Tzu','Shih Tzu'),('Indian Periah','Indian Periah'),('Siberian Husky','Siberian Husky'),('British Shorthair','British Shorthair'),('Persian Cat','Persian Cat'),('Maine Coon','Maine Coon'),('Scotish Fold','Scotish Fold'),('Siamese Cat','Siamese Cat'),('Syrian Hamster','Syrian Hamster'),('Chinese Hamster','Chinese Hamster'),('Budgerigar','Budgerigar'),('Cockatiel','Cockatiel'),('Black Moor','Black Moor'),('Golden Fish','Golden Fish')])
    #annual_income = models.CharField(max_length=30, choices=[('0 - 300,000', '0 - 300,000'), ('300,000 - 500,000', '300,000 - 500,000'), ('500,000 - 700,000', '500,000 - 700,000'), ('700,000 - 900,000', '700,000 - 900,000'), ('900,000 - 1,100,000', '900,000 - 1,100,000'), ('> 1,100,000', '> 1,100,000')])
    permanent_address = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Donation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator(message='Invalid email format')])
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    contact_number = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    """PURPOSE_CHOICES = [
        ('general', 'General Donation'),
        ('feed', 'To feed the animals'),
        ('veterinary', 'For veterinary care'),
        ('building', 'For building homes for animals'),
        ('other', 'Towards other specific cause'),
    ]
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    other_purpose = models.CharField(max_length=100, blank=True)
    DONATION_TYPE_CHOICES = [
        ('one_time', 'One Time Donation'),
        ('monthly', 'Monthly Donation'),
        ('quarterly', 'Quarterly Donation'),
        ('half_yearly', 'Half-Yearly Donation'),
        ('yearly', 'Yearly Donation'),
    ]
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPE_CHOICES)
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('CHF', 'CHF'),
        ('CAD', 'CAD'),
        ('AUD', 'AUD'),
        ('ZAR', 'ZAR'),
        ('AED', 'AED'),
        ('INR', 'INR'),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit / Debit Card'),
        ('e_wallet', 'E-Wallets'),
        ('upi', 'UPI'),
        ('money_order', 'Money Order / Demand Draft'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)"""
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


"""class Registration(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator])
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_id

class Login(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id

    @staticmethod
    def authenticate(user_id, password):
        try:
            registration = Registration.objects.get(user_id=user_id)
        except Registration.DoesNotExist:
            return None

        if password == registration.password:
            return Login(user_id=user_id, password=password)
        else:
            return None
"""