'''
### Ejercicio 13:
### Descripción del ejercicio:

Nos han pedido que implementemos un programa en Python que permita al usuario establecer una nueva contraseña segura. 
La contraseña debe cumplir con los siguientes criterios para ser considerada segura:

### Pasos a seguir:

1. **Requisitos de la Contraseña:**
    - Debe contener al menos una letra mayúscula.
    - Debe contener al menos una letra minúscula.
    - Debe contener al menos un dígito numérico.

2. **Flujo del Programa:**
    - El programa solicitará repetidamente al usuario que ingrese una nueva contraseña hasta que se cumplan 
    todos los criterios de seguridad.
    - Una vez que se ingresa una contraseña que cumple con los criterios, se solicitará al usuario que la confirme.
    - Si la contraseña de confirmación coincide con la contraseña ingresada, se imprimirá un mensaje de éxito y el 
    programa terminará.
    - Si las contraseñas no coinciden, se solicitará al usuario que ingrese la contraseña nuevamente.

'''

while True: 
    contraseña = input("Ingrese su nueva contraseña:")
    if any (letra.isupper() for letra in contraseña) and any (letra.lower() for letra in contraseña) and any (letra.isdigit() for letra in contraseña): 
         contraseña_confirmada = input("Repite la contraseña: ")
         if contraseña_confirmada == contraseña:
             print("Enhorabuena, has creado una nueva contraseña") 
             break
         else:
            print("No coinciden las contraseñas, vuelva a introducir la contraseña de nuevo") 
             
    else:
        print("La contraseña debe contener al menos una minuscula una mayuscula y un digito")
               