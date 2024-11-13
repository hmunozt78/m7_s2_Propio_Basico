from django import forms

from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'fecha_vencimiento', 'categoria']
        
        widgets = {
            'nombre' : forms.TextInput(attrs={"class": 'form-control', 'maxlenght': 50}),
            'descripcion' : forms.Textarea(attrs={"class": 'form-control', "rows":4}),
            'precio' : forms.NumberInput(attrs={"class": 'form-control', "min":1, "max":999999999}),
            'stock' : forms.NumberInput(attrs={"class": 'form-control', "min":0}),
            'fecha_vencimiento' : forms.DateInput(attrs={"class":'form-control', 'type':'date', 'min': '2024-11-14'}),
            'categoria' : forms.Select(attrs={"class": 'form-control'}),
        }

            
# nombre = models.CharField(max_length=50)
# descripcion = models.CharField(max_length=255, blank=True, null=True)
# precio = models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)
# stock = models.IntegerField(blank=True, null=True)
# fecha_vencimiento = models.DateField(blank=True, null=True)
# categoria = models.ForeignKey(Categoria, models.DO_NOTHING)