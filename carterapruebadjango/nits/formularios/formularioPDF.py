from django import forms
class FormularioPDF(forms.Form):
    NIT=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Fecha_de_Corte=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    AÑO=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    Tipo_empresa=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    Ingresos_Operacionales=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
         max_length=50
    )
    Costos_de_ventas_y_de_prestación_de_servicios=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    Otros_ingresos=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    Gastos_Operacionales_de_admon=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_gastos=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otras_ganancias_pérdidas=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Ingresos_financieros=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Costos_financieros=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Impuesto_de_renta_y_complementarios=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Gastos_Operacionales_de_venta=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Efectivo_y_equivalentes_al_efectivo=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Clientes_CP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Inventarios_CP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_activos_financieros=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Propiedad_planta_y_equipo=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Deudores_LP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Proveedores_CP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Obligaciones_Financieras_CP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Proveedores_LP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Obligaciones_Financieras_LP=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50  
    )
    Capital_Social=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Prima_de_emisión=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Reservas=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Ganancias_acumuladas=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_Activos_Corrientes=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Activo_Corriente=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_Activos_No_Corrientes=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Activo_No_Corriente=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Activo=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_Pasivos_Corrientes=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Pasivo_Corriente=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_pasivos_no_Corrientes=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Pasivo_No_Corriente=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Pasivo=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_Patrimonio=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_patrimonio=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Total_Pasivo_mas_Patrimonio=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Utilidad_Bruta=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Utilidad_Operacional=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Otros_ingresos_o_egresos=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    ) 
    Utilidad_antes_de_impuestos=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )
    Ganancias_y_pérdidas=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=50
    )