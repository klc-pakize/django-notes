from django.contrib import admin
from django.utils import timezone

from .models import Product, Review


#? Inline Structure: It is the structure that allows me to see the connected child structures from the parent under the parent structure.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 2  # extra 2 empty review lines are given
    classes = ('collapse',)  # Ability to open and close

class ProductAdmin(admin.ModelAdmin):

    inlines = [ReviewInline]

    list_display = ('name', 'created_date', 'update_date', 'is_in_stock', 'added_days_ago', 'how_many_reviews')  #I specify which field of the models I want to see, it works the same as the str method. It overrides the list_display str method.

    list_editable = ('is_in_stock',)  # It allows us to make changes on the main page without going into the details of the object.
    #!We cannot give the field we linked to editable.
    list_display_links = ('created_date',)  # When we press the field written here, we go to the detail of the object. By default, the first field is given.

    list_filter = ('is_in_stock', 'created_date',)  # Filters by fields

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
                ('description',)
            ),
            'description' : "You can use this section for optionals settings"
        }),
    )
    
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
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created_date", "is_released")
    list_per_page = 50
    row_id_fields = ('product',)  



admin.site.site_title = 'Product Title'  # Changes the tab title.
admin.site.site_header = 'Product Admin Panel'  # Changes the main title of the admin panel.
admin.site.index_title = 'Welcome to Product Panel'  # Changes the second main title of the admin panel.
admin.site.register(Product, ProductAdmin)  
admin.site.register(Review, ReviewAdmin)  