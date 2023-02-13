from django.contrib import admin
from django.utils import timezone
from django.utils.safestring import mark_safe

from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
from products.resources import ReviewResource

from .models import Product, Review, Category


#? Inline Structure: It is the structure that allows me to see the connected child structures from the parent under the parent structure.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2  # extra 2 empty review lines are given
    classes = ('collapse',)  # Ability to open and close

class ProductAdmin(admin.ModelAdmin):

    inlines = [ReviewInline]

    list_display = ('name', 'created_date', 'update_date', 'is_in_stock', 'added_days_ago', 'how_many_reviews', 'bring_img_to_list')  #I specify which field of the models I want to see, it works the same as the str method. It overrides the list_display str method.

    list_editable = ('is_in_stock',)  # It allows us to make changes on the main page without going into the details of the object.
    #!We cannot give the field we linked to editable.
    list_display_links = ('created_date',)  # When we press the field written here, we go to the detail of the object. By default, the first field is given.

    # list_filter = ('is_in_stock', 'created_date',)  # Filters by fields
    list_filter = ("is_in_stock", ("created_date", DateTimeRangeFilter))

    ordering = ('-name',)  # It operates according to the fields entered in the sorting process, it can be added to the beginning of '-' for reverse sorting.
    
    search_fields = ('name',)  # Searches according to the specified field. There is no need to search for the exact same.

    prepopulated_fields = {'slug':('name',)}  # fills the first typed field relative to the second typed field.

    list_per_page = 25  # Specifies the number of objects to be displayed on 1 page.

    date_hierarchy = "update_date"  # You get a nice drill-down menu at the top of the admin change list:When selecting a year, Django will filter the data to the selected year, and present a list of months for which there is data in that year.

    # fields = (('name', 'slug'), 'description', 'is_in_stock')  #? When we enter the details of the object, we determine which fields will be displayed. Fields written in separate parentheses are displayed side by side.
    #! Fields and fieldset are not used at the same time, they both have the same task. Fieldset is more detailed.
    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), 'is_in_stock'
            ),
        }),

        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields": (
                ('description', 'categories', "product_img", "bring_image")
            ),
            'description' : "You can use this section for optionals settings"
        }),
    )
    readonly_fields = ('bring_image',)  # Read-only fields

    filter_horizontal = ('categories',)  # Provides a more convenient interface for selecting product categories
    #? filter_vertical = ('categories',)  # Provides a more convenient interface for selecting product categories
    actions = ('is_in_stock',)

    def is_in_stock(self, request, queryset):  # The objects we choose from the admin panel come as a queryset.
        count = queryset.update(is_in_stock = True)
        self.message_user(request, f' {count} added to stock' )

    #? def is_in_stock To make this name more understandable;
    is_in_stock.short_description = "Add marked products to stock" 

    def added_days_ago(self, product):
        difference = timezone.now() - product.created_date
        return difference.days

    def how_many_reviews(self, obj):
        count = obj.reviews.count()
        return count
    
    def bring_image(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{obj.name} has not image </h3>")

    #? show image in list:
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")

    bring_img_to_list.short_description = "product_image"  # It is used to make it more understandable and legible so that the method name does not appear on the homepage.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_date", "is_released")
    list_per_page = 50
    row_id_fields = ('product',) 
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
    resource_class = ReviewResource



admin.site.site_title = 'Product Title'  # Changes the tab title.
admin.site.site_header = 'Product Admin Panel'  # Changes the main title of the admin panel.
admin.site.index_title = 'Welcome to Product Panel'  # Changes the second main title of the admin panel.
admin.site.register(Review, ReviewAdmin)  
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)