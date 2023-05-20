# Documentación del código

---

# Calculadora de Pomodoros
### Platzi Master Review: (4/5)
_"Buena codificación. Buena eleccion de tema.
El uso de los ciclos y el input que toca realizar al que realiza la actividad"_

## Instrucciones

Este programa calcula la cantidad aproximada de pomodoros que se necesitan para completar una actividad, dadas las horas que se necesitan y la duración de los pomodoros y los descansos.

El usuario debe proporcionar la cantidad de horas que necesita para la actividad, la duración del pomodoro en minutos y la duración del descanso en minutos. Luego, el programa calculará la cantidad aproximada de pomodoros necesarios para completar la actividad.

## Explicación de Código

El programa consiste en dos funciones: **`pomodoro_timer_calculator()`** y **`main()`**. La función **`pomodoro_timer_calculator()`** realiza el cálculo para determinar la cantidad de pomodoros necesarios para completar la actividad.

La función **`main()`** solicita al usuario la información para calcular la cantidad de pomodoros necesarios y muestra la cantidad aproximada de pomodoros para terminar la actividad.

La función **`pomodoro_timer_calculator()`** toma tres argumentos: la cantidad de horas que se necesitan para la actividad, la duración del pomodoro en minutos y la duración del descanso en minutos.

```python
def pomodoro_timer_calculator(activity_hours, pomodoro_duration, break_duration):
```

La función **`pomodoro_timer_calculator()`** primero convierte las horas necesarias para la actividad a minutos. Luego, realiza el cálculo para determinar la cantidad de pomodoros necesarios para completar la actividad, utilizando la fórmula **`(total_minutes // (pomodoro_duration + break_duration))`**. La función devuelve la cantidad de pomodoros necesarios.

```python
# Convertir horas a minutos
    total_minutes = activity_hours * 60

    #Calcular la cantidad
    pomodoro_operation = int(total_minutes // (pomodoro_duration + break_duration))
    return pomodoro_operation
```

La función **`main()`** utiliza un bucle **`while`** para solicitar la información necesaria para realizar el cálculo. Primero, solicita la cantidad de horas necesarias para la actividad. Si se ingresa un número menor o igual a cero, el programa muestra un mensaje de error y solicita nuevamente la entrada.

```python
while True:
        try:
            activity_hours = int(input("Ingresa la cantidad de horas que requiere tu acitvidad: "))
            if activity_hours <= 0:
                print("Por favor ingresa un número mayor que cero.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero")
```

Luego, la función solicita la duración del pomodoro en minutos. Si se ingresa un número menor que 25, el programa muestra un mensaje de error y solicita nuevamente la entrada.

```python
while True:
        try:
            pomodoro_duration = int(input("Ingresa la duración del pomodoro en minutos: "))
            if pomodoro_duration < 25:
                print("La duración mínima del pomodoro es de 25 minutos.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero.")
```

Finalmente, la función solicita la duración del descanso en minutos. Si se ingresa un número menor que 5, el programa muestra un mensaje de error y solicita nuevamente la entrada.

```python
while True:
        try:
            break_duration = int(input("Ingresa la duración del descanso en minutos: "))
            if break_duration < 5:
                print("La duración mínima del descanso es de 5 minutos.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero.")
```

La función **`main()`** llama a la función **`pomodoro_timer_calculator()`** para realizar el cálculo y muestra la cantidad aproximada de pomodoros necesarios para completar la actividad.

```python
pomodoro = pomodoro_timer_calculator(activity_hours, pomodoro_duration, break_duration)

print(f"Necesitarás de aproximadamente {pomodoro} pomodoros para completar tu actividad")
```

## Docstring

La función `pomodoro_timer_calculator()` cuenta con un Docstring que explica el objetivo de la función y tiene una pequeña prueba con el módulo `doctest`:

```python
""" Calcula la cantidad de pomodoros necesarios para una actividad

    Args:
        activity_hours: int
        pomodoro_duration: int
        breal_duration: int

    Return:
        pomodoro: int

    >>> pomodoro_timer_calculator(10, 30, 5)
    17
"""
```

Para correr la prueba se debe usar la siguiente sentencia en la terminal:

```bash
python -m doctest pomodoro.py
```
