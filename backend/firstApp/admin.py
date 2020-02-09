from django.contrib import admin

# Register your models here.
    
from .models import firstApp # add this
    
class firstAppAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'halal') # add this
        
# Register your models here.
admin.site.register(firstApp, firstAppAdmin) # add this
