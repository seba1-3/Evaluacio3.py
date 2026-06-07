especialistas_senior = 0
residentes_junior = 0

while True:
    try:
        cantidad_medicos = int(input("Ingresa la cantidad de médicos a registrar: "))
        if cantidad_medicos > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

for i in range(1, cantidad_medicos + 1):
    print("\n--- Registrando médico", i, "de", cantidad_medicos, "---")

    while True:
        nombre = input("Ingresa el nombre profesional del médico: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    while True:
        try:
            experiencia = int(input("Ingresa los años de experiencia clínica de " + nombre + ": "))
            if experiencia > 0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    if experiencia > 5:
        categoria = "Especialista Senior"
        especialistas_senior = especialistas_senior + 1
    else:
        categoria = "Residente Junior"
        residentes_junior = residentes_junior + 1

    print("Médico " + nombre + " registrado como " + categoria + ".")

print("\n¡El hospital cuenta con", especialistas_senior, "Especialistas Senior y", residentes_junior, "Residentes Junior! ¡Sistema listo para operar!")