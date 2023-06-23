

# Create your models here.
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    activo = models.BooleanField()
    categoria = models.CharField(max_length=100)
    calificacion = models.IntegerField()

    def __str__(self):
       # texto = "{0} {1} {2} {3} {4}"
       # return texto.format(self.nombre, self.direccion, self.telefono, self.email, self.ciudad)
        return self.nombre
        
class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    numero_parte = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Precio(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.proveedor} - {self.articulo}"

class Pedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.proveedor} - {self.articulo}"