def pomodoro_timer_calculator(activity_hours, pomodoro_duration, break_duration):
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
    # Convertir horas a minutos
    total_minutes = activity_hours * 60

    #Calcular la cantidad
    pomodoro_operation = int(total_minutes // (pomodoro_duration + break_duration))
    return pomodoro_operation

def main():

    """Esta función solicita al usuario cantidad de:
    1. Horas que requiere la actividad
    2. La duración en minutos de cada pomodoro
    3. La duración en minutos de cada descando entre pomodoros."""

    while True:
        try:
            activity_hours = int(input("Ingresa la cantidad de horas que requiere tu acitvidad: "))
            if activity_hours <= 0:
                print("Por favor ingresa un número mayor que cero.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero")

    while True:
        try:
            pomodoro_duration = int(input("Ingresa la duración del pomodoro en minutos: "))
            if pomodoro_duration < 25:
                print("La duración mínima del pomodoro es de 25 minutos.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero.")

    while True:
        try:
            break_duration = int(input("Ingresa la duración del descanso en minutos: "))
            if break_duration < 5:
                print("La duración mínima del descanso es de 5 minutos.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número entero.")


    pomodoro = pomodoro_timer_calculator(activity_hours, pomodoro_duration, break_duration)

    print(f"Necesitarás de aproximadamente {pomodoro} pomodoros para completar tu actividad")

if __name__ == '__main__':
    main()
    