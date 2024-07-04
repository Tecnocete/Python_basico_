lista_campañas = [
    {
        'nombre': 'Rebajas de Enero',
        'presupuesto': 35000,
        'inicio': '2023-01-02',
        'fin': '2023-01-31',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Clientes regulares', 'Potenciales compradores'],
        'personas_alcanzadas': 50000,
        'tasa_conversion': 0.02
    },
    {
        'nombre': 'San Valentín',
        'presupuesto': 25000,
        'inicio': '2023-02-01',
        'fin': '2023-02-14',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad impresa'],
        'segmentos_objetivo': ['Parejas', 'Jóvenes'],
        'personas_alcanzadas': 30000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Día del Padre',
        'presupuesto': 20000,
        'inicio': '2023-06-01',
        'fin': '2023-06-15',
        'medios': ['Redes Sociales', 'Colaboraciones con influencers', 'Publicidad impresa'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 25000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Día de la Madre',
        'presupuesto': 22000,
        'inicio': '2023-04-20',
        'fin': '2023-05-10',
        'medios': ['Publicidad en línea', 'Redes Sociales', 'Email Marketing'],
        'segmentos_objetivo': ['Jóvenes', 'Familias'],
        'personas_alcanzadas': 28000,
        'tasa_conversion': 0.04
    },
    {
        'nombre': 'Día del Friki',
        'presupuesto': 18000,
        'inicio': '2023-05-20',
        'fin': '2023-05-25',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Colaboraciones con influencers'],
        'segmentos_objetivo': ['Jóvenes'],
        'personas_alcanzadas': 20000,
        'tasa_conversion': 0.05
    },
    {
        'nombre': 'Black Friday',
        'presupuesto': 50000,
        'inicio': '2023-11-21',
        'fin': '2023-11-30',
        'medios': ['Redes Sociales', 'Email Marketing', 'Publicidad en línea'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 100000,
        'tasa_conversion': 0.03
    },
    {
        'nombre': 'Navidad',
        'presupuesto': 60000,
        'inicio': '2023-12-01',
        'fin': '2023-12-24',
        'medios': ['Publicidad en tiendas físicas', 'Redes Sociales', 'Publicidad impresa'],
        'segmentos_objetivo': ['Todos los compradores'],
        'personas_alcanzadas': 120000,
        'tasa_conversion': 0.04
    }
]

# Nuevo diccionario de campaña
nueva_campaña = {
    'nombre': 'Oferta de Verano',
    'presupuesto': 0,
    'inicio': '2024-06-01',
    'fin': '2024-08-31',
    'medios': ['Redes Sociales', 'Publicidad en línea'],
    'segmentos_objetivo': ['Familias', 'Jóvenes'],
    'personas_alcanzadas': "0",   
}

lista_campañas.append(nueva_campaña)

for campaña in lista_campañas:
    try:
       int(campaña['personas_alcanzadas'])
    except ValueError:
        print(f"En la campaña {campaña['nombre']} el valor de personas_alcanzadas: {campaña['personas_alcanzadas']} no es válido")


'''
### Ejercicio 12:
### Descripción del ejercicio:

Queremos realizar una división entre el presupuesto y la cantidad de personas alcanzadas en cada campaña.
Sin embargo, puede ocurrir un error si la cantidad de personas alcanzadas es 0 o si no es un número válido.
'''

for campaña in lista_campañas:
    try:
        ratio_presupuesto_persona = campaña['presupuesto']/int(campaña['personas_alcanzadas'])
    except ZeroDivisionError:
        print (f"En la campaña {campaña['nombre']} el número de personas alcanzadas es 0")
    except ValueError:
        print(f"El valor de personas_alcanzadas para la campaña {campaña['nombre']} no es numérico")

