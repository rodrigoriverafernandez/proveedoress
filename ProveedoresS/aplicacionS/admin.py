from django.contrib import admin

# Register your models here.


from .models import *

@admin.register(Proveedor)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion', 'telefono', 'email', 'ciudad')
    #  search_fields = ('nombre', 'direccion', 'telefono', 'email', 'ciudad')
    # list_editable = ('nombre','direccion')
    # list_display_links = ('nombre',)
    #list_filter = ('ciudad',)
    list_per_page = 3
    #exclude = ('direccion',)


# Register your models here.
#admin.site.register(Proveedor)
admin.site.register(Articulo)
admin.site.register(Precio)
admin.site.register(Pedido)