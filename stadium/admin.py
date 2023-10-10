from django.contrib import admin
from .models import FieldsModel,BronModel
from .forms import FieldsForm

class FieldAdmin(admin.ModelAdmin):
    form=FieldsForm
    list_display=('field_name',)
    search_fields=('field_name',)

admin.site.register(FieldsModel)
admin.site.register(BronModel)
