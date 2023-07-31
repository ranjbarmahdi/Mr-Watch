from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


# =======================================<< Brand Admin >>=======================================
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'persian_name', 'nationality']
    ordering = ['nationality', 'name']
    list_display_links = ['id']
    search_fields = ['name', 'nationality']
    # list_editable = ['name', 'nationality']
    list_filter = ['nationality']


# =======================================<< Color Admin >>=======================================
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'value']
    ordering = ['name']
    list_display_links = ['id']
    search_fields = ['name', 'value']
    list_editable = ['name', 'value']


# =======================================<< Product Admin >>=======================================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'sex', 'price', 'off', 'new_price', 'status']
    list_display_links = ['id', 'brand']
    list_filter = ['brand', 'status', ('publish', JDateFieldListFilter)]
    list_editable = ['price', 'off', 'status']
    ordering = ['-publish']
    raw_id_fields = ['strap_color', 'dial_color', 'case_color', 'brand']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['brand', 'model']}
    search_fields = ['brand', 'model']


# =======================================<< Comment Admin >>=======================================
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name', 'create', 'active']
    list_filter = ['active', ('create', JDateFieldListFilter), ('update', JDateFieldListFilter)]
    search_fields = ['name', 'body']
    list_editable = ['active']
    list_display_links = ['id', 'product']


# =====================================<< Ticket Admin >>=====================================
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'seen']
    list_display_links = ['id', 'name']
    # list_editable = ['seen']