from django.contrib import admin
from django.shortcuts import render
from .models import Portfolio,Category,About,Contact,Services
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('image','description')
    readonly_fields = ['id']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('img',)
    readonly_fields = ['id']

    def img(self, obj):
        return format_html('<img width="100" height="100" src="{}" style="border-radius: 50%;" />', obj.image.url)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'message')
    readonly_fields = ['id']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    readonly_fields = ['id']


