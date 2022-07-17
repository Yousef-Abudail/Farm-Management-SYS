from django.contrib import admin
from .models import Land, Plant, Fertilizer, Sales,User, Farmers, Pesticides
from .models import Medicine, Disease, TCost

# Register your models here.

admin.site.register(Land)
admin.site.register(Plant)
admin.site.register(Fertilizer)
admin.site.register(User)
admin.site.register(Farmers)
admin.site.register(Pesticides)
admin.site.register(Disease)
admin.site.register(Medicine)
admin.site.register(TCost)
admin.site.register(Sales)