from django.contrib import admin

# Register your models here.
from .models import SOS, Adoption, Donation
 
@admin.register(SOS)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
SOS._meta.get_fields()]

@admin.register(Adoption)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Adoption._meta.get_fields()]

@admin.register(Donation)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Donation._meta.get_fields()]

"""@admin.register(Registration)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Registration._meta.get_fields()]

@admin.register(Login)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Login._meta.get_fields()]"""