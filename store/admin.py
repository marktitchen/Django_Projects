from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Supplier, Review, Offer


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
        ('Product', {'fields': ['product']}),
        ('Quantity', {'fields': ['quantity']}),
        ('Price', {'fields': ['price']}),
    ]
    readonly_fields = ['product', 'quantity', 'price']
    can_delete = False
    max_num = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'billingName', 'emailAddress', 'created']
    list_display_links = ('id', 'billingName')
    search_fields = ['id', 'billingName', 'emailAddress']
    readonly_fields = ['id', 'token', 'total', 'emailAddress', 'created', 'billingName', 'billingAddress1',
                       'billingCity', 'billingPostcode', 'billingCountry', 'shippingName', 'shippingAddress1',
                       'shippingCity', 'shippingPostcode', 'shippingCountry']

    fieldsets = [
        ('ORDER INFORMATION', {'fields': ['id', 'token', 'total', 'created']}),
        ('BILLING INFORMATION', {
            'fields': ['billingName', 'billingAddress1', 'billingCity', 'billingPostcode', 'billingCountry',
                       'emailAddress']}),
        ('SHIPPING INFORMATION',
         {'fields': ['shippingName', 'shippingAddress1', 'shippingCity', 'shippingPostcode', 'shippingCountry']}),
    ]

    inlines = [
        OrderItemAdmin,
    ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Review)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'contact', 'emailAddress']
    list_editable = ['contact', 'emailAddress']


admin.site.register(Supplier, SupplierAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'product', 'discount']
    list_editable = ['product', 'discount']


admin.site.register(Offer, OfferAdmin)
