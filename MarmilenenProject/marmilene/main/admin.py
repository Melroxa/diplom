from django.contrib import admin
from .models import Service, Category, Master, CategoryMaster, MasterImage
from .forms import ServiceForm


from django.contrib import admin
from .models import Category, Service
from django import forms
from .forms import ServiceForm

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    class Media:
        css = {
            'all': ('admin_custom.css',)
        }

class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


class MasterImageInline(admin.TabularInline):
    model = MasterImage
    extra = 1


class MasterAdmin(admin.ModelAdmin):
    inlines = [MasterImageInline]
    list_display = ['title']


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]


class CategoryMasterAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(CategoryMaster, CategoryMasterAdmin)
