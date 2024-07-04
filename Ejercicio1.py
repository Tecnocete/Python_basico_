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
'''
### Ejercicio 1:
### Descripción del ejercicio:
Lo primero que nos piden es que veamos el nombre de cada campaña, 
su presupuesto, el número de personas alcanzadas y su tasa de conversión.
'''
elementos = ['nombre','presupuesto','personas_alcanzadas','tasa_conversion']

for campaña in lista_campañas:
    for elemento in campaña:
        if elemento in elementos:
            print(f'{elemento}: {campaña[elemento]}')
            if elemento == 'tasa_conversion':
                print("\n")
                
'''
### Ejercicio 2:
### Descripción del ejercicio:
Lo segundo que nos piden es que creemos un conjunto, un `set`,con todos medios donde se llevaron a cabo la campañas.
'''
mi_set = {medio for campaña in lista_campañas for medio in campaña['medios']}
print(mi_set)
'''
### Ejercicio 3:
### Descripción del ejercicio:
Nos piden que averiguemos cual es el medio más utilizado
'''
conteo_medios =  {}
for campaña in lista_campañas:
    for medio in campaña['medios']:
        if medio in conteo_medios:
            conteo_medios[medio] +=1
        else:
            conteo_medios[medio] = 1
medio_mas_usado= max(conteo_medios)
print(conteo_medios)
print(f'EL medio más usado es : {medio_mas_usado}')
'''### Ejercicio 4:
### Descripción del ejercicio:
Nos piden que calculemos el gasto total de todas las campañas del año pasado:
'''
gasto_total = 0
for campaña in lista_campañas:
    gasto_total += campaña['presupuesto']
print(f'El gasto total fue: {gasto_total}')
'''
### Ejercicio 5:
### Descripción del ejercicio:
Se nos pide calcular las conversiones de cada campaña multiplicando 
el número de personas alcanzadas por la tasa de conversión y luego imprimir 
el nombre de cada campaña junto con el número de conversiones.
'''
for campaña in lista_campañas:
    campaña['conversiones']=int(campaña['personas_alcanzadas']*campaña['tasa_conversion'])
print ([f"La tasa de conversiones en la campaña: {campaña['nombre']} fue {campaña['conversiones']}"for campaña in lista_campañas ])
'''
### Ejercicio 6:
### Descripción del ejercicio:
Nos piden que busquemos las campañas con mayor tasa de conversión
'''
mayor_tasa_conversion = 0
indice= 0
while indice < len(lista_campañas):
    tasa_actual = lista_campañas[indice]['tasa_conversion']
    if tasa_actual > mayor_tasa_conversion:
        mayor_tasa_conversion = tasa_actual
        campaña_buscada = [lista_campañas[indice]['nombre']]
    elif tasa_actual == mayor_tasa_conversion:
        campaña_buscada.append(lista_campañas[indice]['nombre'])
    indice += 1
print (f'La mayor tasa de conversion fue: {mayor_tasa_conversion} en la campaña{campaña_buscada}')

'''
### Ejercicio 7:
### Descripción del ejercicio:
Queremos identificar las campañas que tienen una tasa de conversión superior a 0.03 y un presupuesto inferior a 30000.
'''
campañas_seleccionadas = []
for campaña in lista_campañas:
    if campaña['tasa_conversion'] > 0.03 and campaña ['presupuesto'] < 30000:
        campañas_seleccionadas.append((campaña['nombre'],campaña['tasa_conversion'],campaña['presupuesto']))
print(f'Las campañas seleccionadas son: {campañas_seleccionadas}')

