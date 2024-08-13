import os
import json
from datetime import datetime, time

class Habitacion:
    def __init__(self, numero, tipo, reservada, precio):
        self.numero = numero
        self.tipo = tipo
        self.reservada = reservada
        self.precio = precio
        self.descripcion = self.generardescripcion()
        self.reserva = {}

    def generardescripcion(self):
        descripciones = {
            "Simples": "Dispone con 1 cama para una sola persona.",
            "Dobles": "Dispone de una cama matrimonial, con televisor y balcón.",
            "Familiar": "Dispone de una cama matrimonial y dos camas extras, con televisor y balcón.",
            "Suite": "Dispone de 4 cuartos, una sala de videojuegos y recreación, servicio de cine y servicio a la habitación 24/7 y con vista al paisaje."
        }
        return descripciones.get(self.tipo, "Descripción no disponible")

class Hotel:
    def __init__(self, id, nombre, direccion, habitaciones, descripcion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = habitaciones
        self.descripcion = descripcion

def inicializar_habitaciones(num_habitaciones):
    tipo_habitaciones = ["Simples", "Dobles", "Familiar", "Suite"]
    precios_habitaciones = [300.00, 500.00, 700.00, 1100.00]
    habitaciones = []

    for i in range(num_habitaciones):
        tipo = tipo_habitaciones[i % len(tipo_habitaciones)]
        precio = precios_habitaciones[i % len(precios_habitaciones)]
        habitaciones.append(Habitacion(numero=i + 1, tipo=tipo, reservada=False, precio=precio))
    return habitaciones

def inicializar_hoteles():
    hoteles = {
        "Estados Unidos": [
            Hotel(id=1, nombre="Hotel California", direccion="Los Angeles, California", habitaciones=inicializar_habitaciones(20), descripcion="Un hotel icónico con vistas impresionantes y una historia legendaria."),
            Hotel(id=2, nombre="The Plaza", direccion="New York, New York", habitaciones=inicializar_habitaciones(20), descripcion="Lujo clásico en el corazón de Nueva York."),
            Hotel(id=3, nombre="Four Seasons", direccion="Chicago, Illinois", habitaciones=inicializar_habitaciones(20), descripcion="Elegancia moderna con vistas al lago Michigan.")
        ],
        "México": [
            Hotel(id=4, nombre="Gran Hotel Ciudad de México", direccion="Ciudad de México, Ciudad de México", habitaciones=inicializar_habitaciones(20), descripcion="Arquitectura impresionante en el corazón de la ciudad."),
            Hotel(id=5, nombre="Hotel Xcaret México", direccion="Playa del Carmen, Quintana Roo", habitaciones=inicializar_habitaciones(20), descripcion="Resort todo incluido con acceso a parques naturales."),
            Hotel(id=6, nombre="Las Alcobas", direccion="Ciudad de México, Ciudad de México", habitaciones=inicializar_habitaciones(20), descripcion="Boutique hotel con servicios personalizados y diseño contemporáneo.")
        ],
        "Ecuador": [
            Hotel(id=7, nombre="Mashpi Lodge", direccion="Pacto, Pichincha", habitaciones=inicializar_habitaciones(20), descripcion="Lujosa eco-lodge en el corazón del bosque nublado."),
            Hotel(id=8, nombre="Hotel Plaza Grande", direccion="Quito, Pichincha", habitaciones=inicializar_habitaciones(20), descripcion="Elegancia histórica en la Plaza de la Independencia."),
            Hotel(id=9, nombre="Casa Gangotena", direccion="Quito, Ecuador", habitaciones=inicializar_habitaciones(20), descripcion="Mansión restaurada con vistas panorámicas del casco antiguo.")
        ],
        "Argentina": [
            Hotel(id=10, nombre="HTL Urbano Buenos Aires Hotel", direccion="Buenos Aires, Provincia de Buenos Aires", habitaciones=inicializar_habitaciones(20), descripcion="Hotel moderno en el centro de Buenos Aires."),
            Hotel(id=11, nombre="Alvear Palace Hotel", direccion="Buenos Aires, Argentina", habitaciones=inicializar_habitaciones(20), descripcion="Lujo y sofisticación en el barrio de la Recoleta."),
            Hotel(id=12, nombre="Llao Llao Hotel & Resort", direccion="Bariloche, Argentina", habitaciones=inicializar_habitaciones(20), descripcion="Resort de montaña con vistas espectaculares del lago.")
        ],
        "Colombia": [
            Hotel(id=13, nombre="Hilton Cartagena", direccion="Cartagena, Colombia", habitaciones=inicializar_habitaciones(20), descripcion="Resort de playa con instalaciones de lujo."),
            Hotel(id=14, nombre="Sofitel Legend Santa Clara", direccion="Cartagena, Colombia", habitaciones=inicializar_habitaciones(20), descripcion="Convento restaurado en el centro histórico."),
            Hotel(id=15, nombre="Hotel Movich Buró 26", direccion="Bogotá, Colombia", habitaciones=inicializar_habitaciones(20), descripcion="Hotel de negocios moderno cerca del aeropuerto.")
        ],
        "Perú": [
            Hotel(id=16, nombre="Selina Miraflores Lima", direccion="Lima, Perú", habitaciones=inicializar_habitaciones(20), descripcion="Hotel vibrante y moderno en el barrio de Miraflores."),
            Hotel(id=17, nombre="Belmond Hotel Monasterio", direccion="Cusco, Perú", habitaciones=inicializar_habitaciones(20), descripcion="Antiguo monasterio convertido en hotel de lujo."),
            Hotel(id=18, nombre="JW Marriott El Convento Cusco", direccion="Cusco, Perú", habitaciones=inicializar_habitaciones(20), descripcion="Convento del siglo XVI restaurado con comodidades modernas.")
        ],
        "España": [
            Hotel(id=19, nombre="Hotel Ritz", direccion="Madrid, España", habitaciones=inicializar_habitaciones(20), descripcion="Elegancia clásica en el corazón de Madrid."),
            Hotel(id=20, nombre="W Barcelona", direccion="Barcelona, España", habitaciones=inicializar_habitaciones(20), descripcion="Hotel moderno con vistas al mar."),
            Hotel(id=21, nombre="Gran Hotel La Florida", direccion="Barcelona, España", habitaciones=inicializar_habitaciones(20), descripcion="Hotel boutique con vistas panorámicas de la ciudad.")
        ],
        "Reino Unido": [
            Hotel(id=22, nombre="The Savoy", direccion="Londres, Reino Unido", habitaciones=inicializar_habitaciones(20), descripcion="Histórico hotel de lujo en el corazón de Londres."),
            Hotel(id=23, nombre="The Ritz London", direccion="Londres, Reino Unido", habitaciones=inicializar_habitaciones(20), descripcion="Símbolo de lujo y elegancia en Piccadilly."),
            Hotel(id=24, nombre="Claridge's", direccion="Londres, Reino Unido", habitaciones=inicializar_habitaciones(20), descripcion="Famoso por su glamour art deco y hospitalidad.")
        ],
        "Francia": [
            Hotel(id=25, nombre="Hotel Le Meurice", direccion="París, Francia", habitaciones=inicializar_habitaciones(20), descripcion="Lujo parisino con vistas al jardín de las Tullerías."),
            Hotel(id=26, nombre="Shangri-La Hotel", direccion="París, Francia", habitaciones=inicializar_habitaciones(20), descripcion="Elegancia asiática en un palacio histórico."),
            Hotel(id=27, nombre="Hotel Plaza Athénée", direccion="París, Francia", habitaciones=inicializar_habitaciones(20), descripcion="Hotel de alta costura en la avenida Montaigne.")
        ],
        "China": [
            Hotel(id=28, nombre="The Peninsula Beijing", direccion="Pekín, China", habitaciones=inicializar_habitaciones(20), descripcion="Lujo contemporáneo en el corazón de Pekín."),
            Hotel(id=29, nombre="Mandarin Oriental Pudong", direccion="Shanghái, China", habitaciones=inicializar_habitaciones(20), descripcion="Resort urbano en la vibrante zona de Pudong."),
            Hotel(id=30, nombre="The Ritz-Carlton Shanghai", direccion="Shanghái, China", habitaciones=inicializar_habitaciones(20), descripcion="Elegancia moderna con vistas impresionantes del río Huangpu.")
        ]
    }
    return hoteles

def seleccionar_pais():
    paises = [
        "Estados Unidos", "México", "Ecuador", "Argentina", 
        "Colombia", "Perú", "España", "Reino Unido", 
        "Francia", "China"
    ]
    
    while True:
        print("\t\t\t ╔══════════════════════════════╗")
        print("\t\t\t ║        Seleccione un País    ║")
        print("\t\t\t ╚══════════════════════════════╝")
        for i, pais in enumerate(paises, 1):
            print(f"\t\t\t {i}. {pais}")
        print("\t\t\t 0. Regresar")
        
        pais_id = int(input("\nIngrese el número del país: "))
        if pais_id == 0:
            return None
        elif 1 <= pais_id <= len(paises):
            return paises[pais_id - 1]
        else:
            print("\nPaís no válido. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

def mostrar_hoteles_por_pais(hoteles, pais):
    while True:
        if pais in hoteles:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\t\t\t ╔══════════════════════════════╗")
            print(f"\t\t\t ║   Hoteles en {pais}         ║")
            print(f"\t\t\t ╚══════════════════════════════╝")
            print("\t\t\t {:<5} {:<30} {:<30}".format('ID', 'Nombre', 'Dirección'))
            print("\t\t\t ────────────────────────────────────────────────────────")

            for idx, hotel in enumerate(hoteles[pais], 1):
                print(f"\t\t\t {idx:<5} {hotel.nombre:<30} {hotel.direccion:<30}")
            print("\t\t\t 0. Regresar")

            hotel_id = int(input("\nIngrese el ID del hotel: "))
            if hotel_id == 0:
                return True
            elif 1 <= hotel_id <= len(hoteles[pais]):
                hotel_seleccionado = hoteles[pais][hotel_id - 1]
                if mostrar_habitaciones(hotel_seleccionado):
                    return True
            else:
                print("\nHotel no encontrado. Intente de nuevo.")
                input('\nPresione Enter para continuar...')
        else:
            print("\nNo hay hoteles disponibles en este país.")
            input('\nPresione Enter para continuar...')
            return True

def mostrar_habitaciones(hotel):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\t\t\t ╔══════════════════════════════════════════════════════════╗")
        print(f"\t\t\t ║      Habitaciones Disponibles en {hotel.nombre}          ║")
        print(f"\t\t\t ╚══════════════════════════════════════════════════════════╝")
        print(f"\t\t\t Dirección: {hotel.direccion}")
        print(f"\t\t\t Descripción: {hotel.descripcion}")
        print("\t\t\t {:<10} {:<15} {:<10}".format('Numero', 'Tipo', 'Precio'))
        print("\t\t\t ─────────────────────────────────────────")

        for habitacion in hotel.habitaciones:
            if not habitacion.reservada:
                print(f"\t\t\t {habitacion.numero:<10} {habitacion.tipo:<15} ${habitacion.precio:<10}")
        print("\t\t\t 0. Regresar")

        numero_habi = int(input("\nIngrese el número de la habitación: "))
        if numero_habi == 0:
            return True
        habitacion_seleccionada = next((hab for hab in hotel.habitaciones if hab.numero == numero_habi), None)
        if habitacion_seleccionada:
            if detalhabi(habitacion_seleccionada):
                return True
        else:
            print("\nHabitación no encontrada. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

def confirmar_reserva(habitacion):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t\t ╔══════════════════════════════╗")
    print("\t\t\t ║       Confirmar Reserva      ║")
    print("\t\t\t ╚══════════════════════════════╝")
    print(f"\t\t\tHabitación Número: {habitacion.numero}")
    print(f"\t\t\tTipo: {habitacion.tipo}")
    print(f"\t\t\tPrecio: ${habitacion.precio:.2f}")

    while True:
        fecha_entrada = input("\t\t\tIngrese la fecha de entrada (YYYY-MM-DD): ")
        hora_entrada = input("\t\t\tIngrese la hora de entrada (HH:MM, formato 24 horas): ")
        fecha_salida = input("\t\t\tIngrese la fecha de salida (YYYY-MM-DD): ")
        hora_salida = input("\t\t\tIngrese la hora de salida (HH:MM, formato 24 horas): ")

        try:
            fecha_entrada_dt = datetime.strptime(fecha_entrada, "%Y-%m-%d")
            fecha_salida_dt = datetime.strptime(fecha_salida, "%Y-%m-%d")
            hora_entrada_dt = datetime.strptime(hora_entrada, "%H:%M").time()
            hora_salida_dt = datetime.strptime(hora_salida, "%H:%M").time()
            fecha_entrada_dt = datetime.combine(fecha_entrada_dt, hora_entrada_dt)
            fecha_salida_dt = datetime.combine(fecha_salida_dt, hora_salida_dt)
            today = datetime.now()

            if fecha_entrada_dt < today or fecha_salida_dt < today:
                print("\n\t\t\tError: Las fechas deben ser actuales o futuras. Intente de nuevo.")
                input('\n\t\t\tPresione Enter para continuar...')
                continue

            if fecha_salida_dt <= fecha_entrada_dt:
                print("\n\t\t\tError: La fecha de salida debe ser después de la fecha de entrada. Intente de nuevo.")
                input('\n\t\t\tPresione Enter para continuar...')
                continue

            break

        except ValueError:
            print("\n\t\t\tFecha u hora no válidas. Intente de nuevo.")
            input('\n\t\t\tPresione Enter para continuar...')

    print("\n\t\t\tSeleccione el método de pago")
    print("\t\t\t[1] Tarjeta de Crédito")
    print("\t\t\t[2] Efectivo")

    metodo_pago = input("\n\t\t\tSeleccione una opción: ")
    if metodo_pago == '1':
        tarjeta = input("\t\t\tIngrese el número de tarjeta de crédito: ")
        if len(tarjeta) < 13 or len(tarjeta) > 19 or not tarjeta.isdigit():
            print("\n\t\t\tNúmero de tarjeta no válido. Intente de nuevo.")
            input('\n\t\t\tPresione Enter para continuar...')
            return False
    elif metodo_pago == '2':
        print("\n\t\t\tPuede pagar en efectivo al llegar al hotel.")
    else:
        print("\n\t\t\tOpción no válida. Intente de nuevo.")
        input('\n\t\t\tPresione Enter para continuar...')
        return False

    habitacion.reservada = True
    habitacion.reserva['fecha_entrada'] = fecha_entrada_dt
    habitacion.reserva['fecha_salida'] = fecha_salida_dt
    habitacion.reserva['metodo_pago'] = metodo_pago

    print("\n\t\t\tReserva confirmada. ¡Disfrute de su estancia!")
    input('\n\t\t\tPresione Enter para continuar...')
    return True

def detalhabi(habitacion):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t\t ╔═════════════════════════════════════╗")
        print("\t\t\t ║     Descripción de la Habitación    ║")
        print("\t\t\t ╚═════════════════════════════════════╝")
        print(f"\t\t\tNúmero: {habitacion.numero}")
        print(f"\t\t\tTipo: {habitacion.tipo}")
        print(f"\t\t\tPrecio: ${habitacion.precio:.2f}")
        print(f"\t\t\tDescripción: {habitacion.descripcion}")
        print(f"\t\t\tReservada: {'Sí' if habitacion.reservada else 'No'}")

        print("\n\t\t\t[1] Confirmar reserva")
        print("\t\t\t[2] Favoritos")
        print("\t\t\t[0] Regresar")

        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            if confirmar_reserva(habitacion):
                return True
        elif opcion == "2":
            agregar_a_favoritos(habitacion)
            print("\n\t\t\tHabitación en favoritos.")
            input('\n\t\t\tPresione Enter para continuar...')
        elif opcion == "0":
            return True
        else:
            print("\n\t\t\tOpción no válida. Intente de nuevo.")
            input('\n\t\t\tPresione Enter para continuar...')

def opciones_modificacion(habitacion):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t\t ╔════════════════════════════════╗")
        print("\t\t\t ║   Opciones de Modificación     ║")
        print("\t\t\t ╚════════════════════════════════╝")
        
        print(f"\nHabitación Número: {habitacion.numero}")
        print(f"Tipo: {habitacion.tipo}")
        fecha_entrada = habitacion.reserva['fecha_entrada']
        fecha_salida = habitacion.reserva['fecha_salida']
        print(f"Fecha y Hora de Entrada: {fecha_entrada.strftime('%Y-%m-%d %H:%M')}")
        print(f"Fecha y Hora de Salida: {fecha_salida.strftime('%Y-%m-%d %H:%M')}")
        metodo_pago = "Tarjeta de Crédito" if habitacion.reserva['metodo_pago'] == "1" else "Efectivo"
        print(f"Método de Pago: {metodo_pago}")
        
        print("\n1. Modificar Fecha y Hora de Entrada")
        print("2. Modificar Fecha y Hora de Salida")
        print("3. Eliminar Reserva")
        print("0. Regresar")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            return False
        elif opcion == "1":
            while True:
                try:
                    fecha_entrada_str = input("Ingrese la nueva fecha de entrada (YYYY-MM-DD): ")
                    fecha_entrada = datetime.strptime(fecha_entrada_str, "%Y-%m-%d")
                    hora_entrada_str = input("Ingrese la nueva hora de entrada (HH:MM, formato 24 horas): ")
                    hora_entrada = datetime.strptime(hora_entrada_str, "%H:%M").time()
                    fecha_hora_entrada = datetime.combine(fecha_entrada, hora_entrada)
                    
                    if fecha_hora_entrada >= habitacion.reserva['fecha_salida']:
                        print("\nLa nueva fecha y hora de entrada no puede ser posterior a la fecha y hora de salida. Intente de nuevo.")
                        input('\nPresione Enter para continuar...')
                        continue
                    
                    habitacion.reserva['fecha_entrada'] = fecha_hora_entrada
                    print("\nFecha y hora de entrada modificadas con éxito.")
                    input('\nPresione Enter para continuar...')
                    return True
                except ValueError:
                    print("\nFecha u hora no válidas. Intente de nuevo.")
                    input('\nPresione Enter para continuar...')
        elif opcion == "2":
            while True:
                try:
                    fecha_salida_str = input("Ingrese la nueva fecha de salida (YYYY-MM-DD): ")
                    fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d")
                    hora_salida_str = input("Ingrese la nueva hora de salida (HH:MM, formato 24 horas): ")
                    hora_salida = datetime.strptime(hora_salida_str, "%H:%M").time()
                    fecha_hora_salida = datetime.combine(fecha_salida, hora_salida)
                    
                    if fecha_hora_salida <= habitacion.reserva['fecha_entrada']:
                        print("\nLa nueva fecha y hora de salida no puede ser anterior a la fecha y hora de entrada. Intente de nuevo.")
                        input('\nPresione Enter para continuar...')
                        continue
                    
                    habitacion.reserva['fecha_salida'] = fecha_hora_salida
                    print("\nFecha y hora de salida modificadas con éxito.")
                    input('\nPresione Enter para continuar...')
                    return True
                except ValueError:
                    print("\nFecha u hora no válidas. Intente de nuevo.")
                    input('\nPresione Enter para continuar...')
        elif opcion == "3":
            habitacion.reservada = False
            habitacion.reserva = {}
            print("\nReserva eliminada con éxito.")
            input('\nPresione Enter para continuar...')
            return True
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

def modificar_reserva(hoteles):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t\t ╔════════════════════════════════╗")
        print("\t\t\t ║     Modificar Reserva          ║")
        print("\t\t\t ╚════════════════════════════════╝")
        
        habitaciones_reservadas = []
        
        for pais, hoteles_pais in hoteles.items():
            for hotel in hoteles_pais:
                if hasattr(hotel, 'habitaciones'):
                    for habitacion in hotel.habitaciones:
                        if habitacion.reservada:
                            habitaciones_reservadas.append((habitacion, hotel))
                else:
                    print(f"Error: {hotel} no tiene atributo 'habitaciones'.")
        
        if not habitaciones_reservadas:
            print("\nNo hay habitaciones reservadas.")
            input('\nPresione Enter para continuar...')
            return

        for idx, (habitacion, hotel) in enumerate(habitaciones_reservadas, 1):
            print(f"\n{idx}. {hotel.nombre} - Habitación {habitacion.numero} ({habitacion.tipo})")
            fecha_entrada = habitacion.reserva['fecha_entrada']
            fecha_salida = habitacion.reserva['fecha_salida']
            print(f"   Fecha y Hora de Entrada: {fecha_entrada.strftime('%Y-%m-%d %H:%M')}")
            print(f"   Fecha y Hora de Salida: {fecha_salida.strftime('%Y-%m-%d %H:%M')}")
            print(f"   Método de Pago: {'Tarjeta de Crédito' if habitacion.reserva['metodo_pago'] == '1' else 'Efectivo'}")
        
        print("\n0. Regresar")
        seleccion = int(input("\nSeleccione una reserva para modificar o eliminar: "))
        
        if seleccion == 0:
            return
        elif 1 <= seleccion <= len(habitaciones_reservadas):
            habitacion, hotel = habitaciones_reservadas[seleccion - 1]
            if opciones_modificacion(habitacion):
                return
        else:
            print("\nSelección no válida. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

def modificar_detalles_reserva(habitacion):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        fecha_entrada = habitacion.reserva['fecha_entrada']
        fecha_salida = habitacion.reserva['fecha_salida']
        
        print("\n\t\t\t╔══════════════════════════════════╗")
        print(f"\t\t\t║     Modificar Reserva: {habitacion.numero}         ║")
        print("\t\t\t╚══════════════════════════════════╝")
        print(f"\n\t\t\tHabitación Número: {habitacion.numero}")
        print(f"\t\t\tTipo: {habitacion.tipo}")
        print(f"\t\t\tFecha y Hora de Entrada: {fecha_entrada.strftime('%Y-%m-%d %H:%M')}")
        print(f"\t\t\tFecha y Hora de Salida: {fecha_salida.strftime('%Y-%m-%d %H:%M')}")
        metodo_pago = "Tarjeta de Crédito" if habitacion.reserva['metodo_pago'] == "1" else "Efectivo"
        print(f"\t\t\tMétodo de Pago: {metodo_pago}")
        
        print("\n\t\t\t╔═══════════════════════════════════════════╗")
        print("\t\t\t║ 1. Modificar Fecha y Hora de Entrada      ║")
        print("\t\t\t║ 2. Modificar Fecha y Hora de Salida       ║")
        print("\t\t\t║ 3. Eliminar Reserva                       ║")
        print("\t\t\t║ 0. Regresar                               ║")
        print("\t\t\t╚═══════════════════════════════════════════╝")
        
        opcion = input("\n\t\t\tSeleccione una opción: ")
        
        if opcion == "0":
            return False
        elif opcion == "1":
            while True:
                try:
                    fecha_entrada_str = input("\t\t\tIngrese la nueva fecha de entrada (YYYY-MM-DD): ")
                    hora_entrada_str = input("\t\t\tIngrese la nueva hora de entrada (HH:MM, formato 24 horas): ")
                    
                    fecha_entrada = datetime.strptime(fecha_entrada_str, "%Y-%m-%d")
                    hora_entrada = datetime.strptime(hora_entrada_str, "%H:%M").time()
                    fecha_hora_entrada = datetime.combine(fecha_entrada, hora_entrada)
                    today = datetime.now()  # Obtener la fecha y hora actuales

                    # Comparar la fecha de entrada con la fecha y hora actuales
                    if fecha_hora_entrada < today:
                        print("\n\t\t\tError: La nueva fecha y hora de entrada no pueden ser anteriores a la fecha y hora actuales.")
                        input('\n\t\t\tPresione Enter para continuar...')
                        continue
                    
                    if fecha_hora_entrada >= habitacion.reserva['fecha_salida']:
                        print("\n\t\t\tError: La nueva fecha y hora de entrada no pueden ser posteriores a la fecha y hora de salida.")
                        input('\n\t\t\tPresione Enter para continuar...')
                        continue
                    
                    habitacion.reserva['fecha_entrada'] = fecha_hora_entrada
                    print("\n\t\t\tFecha y hora de entrada modificadas con éxito.")
                    input('\n\t\t\tPresione Enter para continuar...')
                    return True
                except ValueError:
                    print("\n\t\t\tFecha u hora no válidas. Asegúrese de usar el formato YYYY-MM-DD para la fecha y HH:MM para la hora.")
                    input('\n\t\t\tPresione Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "2":
            while True:
                try:
                    fecha_salida_str = input("\t\t\tIngrese la nueva fecha de salida (YYYY-MM-DD): ")
                    hora_salida_str = input("\t\t\tIngrese la nueva hora de salida (HH:MM, formato 24 horas): ")
                    
                    fecha_salida = datetime.strptime(fecha_salida_str, "%Y-%m-%d")
                    hora_salida = datetime.strptime(hora_salida_str, "%H:%M").time()
                    fecha_hora_salida = datetime.combine(fecha_salida, hora_salida)
                    today = datetime.now()

                    if fecha_hora_salida < today:
                        print("\n\t\t\tError: La nueva fecha y hora de salida no pueden ser anteriores a la fecha y hora actuales.")
                        input('\n\t\t\tPresione Enter para continuar...')
                        continue
                    
                    if fecha_hora_salida <= habitacion.reserva['fecha_entrada']:
                        print("\n\t\t\tError: La nueva fecha y hora de salida no pueden ser anteriores a la fecha y hora de entrada.")
                        input('\n\t\t\tPresione Enter para continuar...')
                        continue
                    
                    habitacion.reserva['fecha_salida'] = fecha_hora_salida
                    print("\n\t\t\tFecha y hora de salida modificadas con éxito.")
                    input('\n\t\t\tPresione Enter para continuar...')
                    return True
                except ValueError:
                    print("\n\t\t\tFecha u hora no válidas. Asegúrese de usar el formato YYYY-MM-DD para la fecha y HH:MM para la hora.")
                    input('\n\t\t\tPresione Enter para continuar...')
                    os.system('cls' if os.name == 'nt' else 'clear')
        elif opcion == "3":
            habitacion.reservada = False
            habitacion.reserva = {}
            print("\n\t\t\tReserva eliminada con éxito.")
            input('\n\t\t\tPresione Enter para continuar...')
            return True
        else:
            print("\n\t\t\tOpción no válida. Intente de nuevo.")
            input('\n\t\t\tPresione Enter para continuar...')

def mostrar_reservas(hoteles):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t\t ╔══════════════════════════════╗")
    print("\t\t\t ║         Ver Reservas         ║")
    print("\t\t\t ╚══════════════════════════════╝")
    for hoteles_pais in hoteles.values():
        for hotel in hoteles_pais:
            for habitacion in hotel.habitaciones:
                if habitacion.reservada:
                    print(f"\nHotel: {hotel.nombre}")
                    print(f"Habitación Número: {habitacion.numero}")
                    print(f"Tipo: {habitacion.tipo}")
                    if 'fecha_entrada' in habitacion.reserva:
                        fecha_entrada = habitacion.reserva['fecha_entrada']
                        fecha_salida = habitacion.reserva['fecha_salida']
                        print(f"Fecha y Hora de Entrada: {fecha_entrada.strftime('%Y-%m-%d %H')}")
                        print(f"Fecha y Hora de Salida: {fecha_salida.strftime('%Y-%m-%d %H')}")
                        print(f"Método de Pago: {'Tarjeta de Crédito' if habitacion.reserva['metodo_pago'] == '1' else 'Efectivo'}")
                        print("-" * 40)
                    else:
                        print("Error: Fecha de entrada no encontrada.")
                        print("-" * 40)
    input('\nPresione Enter para continuar...')

def mostrar_menu_principal():
    print("\n\t\t\t     ╔══════════════════════════╗")
    print("\t\t\t     ║        ReservaHUB        ║")
    print("\t\t\t     ║   Tu sistema de gestión  ║")
    print("\t\t\t     ╚══════════════════════════╝")
    print("───────────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t| 1. ¿A donde quieres ir?        |")
    print("\t\t\t| 2. Modificar reserva           |")
    print("\t\t\t| 3. Mostrar todas las reservas  |")
    print("\t\t\t| 4. Favoritos                   |")
    print("\t\t\t| 0. Salir                       |")
    print("───────────────────────────────────────────────────────────────────────────────────────")

archivo_usuarios = 'usuarios.json'

def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON."""
    if os.path.exists(archivo_usuarios):
        with open(archivo_usuarios, 'r') as archivo:
            return json.load(archivo)
    return []

def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON."""
    with open(archivo_usuarios, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

usuarios_registrados = cargar_usuarios()

def mostrar_menu_login_registro():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\t\t\t╔══════════════════════════════════════════╗")
        print("\t\t\t║          Bienvenido a ReservaHUB         ║")
        print("\t\t\t║    Seleccione una opción para continuar  ║")
        print("\t\t\t╚══════════════════════════════════════════╝")
        print("\n\t\t\t╔════════════════════════════════════════════╗")
        print("\t\t\t║ 1. Iniciar Sesión                          ║")
        print("\t\t\t║ 2. Registrarse                             ║")
        print("\t\t\t║ 0. Salir                                   ║")
        print("\t\t\t╚════════════════════════════════════════════╝")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "0":
            return False
        elif opcion == "1":
            if iniciar_sesion():
                return True
        elif opcion == "2":
            if registrar_usuario():
                return True
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

def iniciar_sesion():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\t\t\t╔════════════════════════════════════╗")
        print("\t\t\t║          Iniciar Sesión            ║")
        print("\t\t\t╚════════════════════════════════════╝")
        correo = input("\t\t\tIngrese su correo electrónico: ")
        contrasena = input("\t\t\tIngrese su contraseña: ")
        
        for usuario in usuarios_registrados:
            if usuario['correo'] == correo and usuario['contrasena'] == contrasena:
                print("\nInicio de sesión exitoso.")
                input('\nPresione Enter para continuar...')
                return True
        
        print("\nCredenciales incorrectas. Intente de nuevo.")
        input('\nPresione Enter para continuar...')

def registrar_usuario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n\t\t\t╔════════════════════════════════════════╗")
        print("\t\t\t║          Registro de Usuario            ║")
        print("\t\t\t╚════════════════════════════════════════╝")
        nombres = input("\t\t\tIngrese sus nombres completos: ")
        correo = input("\t\t\tIngrese su correo electrónico: ")
        numero = input("\t\t\tIngrese su número de teléfono: ")
        contrasena = input("\t\t\tIngrese su contraseña: ")
        direccion = input("\t\t\tIngrese su dirección: ")
        
        for usuario in usuarios_registrados:
            if usuario['correo'] == correo:
                print("\nEl correo electrónico ya está registrado.")
                input('\nPresione Enter para continuar...')
                return False
        
        usuarios_registrados.append({
            'nombres': nombres,
            'correo': correo,
            'numero': numero,
            'contrasena': contrasena,
            'direccion': direccion
        })
        guardar_usuarios(usuarios_registrados)
        print("\nRegistro exitoso. Ahora puede iniciar sesión.")
        input('\nPresione Enter para continuar...')
        return True

favoritos = []

def agregar_a_favoritos(habitacion):
    """Agrega una habitación a la lista de favoritos."""
    if habitacion not in favoritos:
        favoritos.append(habitacion)
        print("\n\t\t\tHabitación agregada a favoritos.")
    else:
        print("\n\t\t\tLa habitación ya está en favoritos.")
    
def mostrar_habitaciones_favoritas():
    """Muestra la lista de habitaciones favoritas y permite seleccionar una para confirmar la reserva."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t\t\t ╔═════════════════════════════════════╗")
    print("\t\t\t ║       Habitaciones Favoritas        ║")
    print("\t\t\t ╚═════════════════════════════════════╝")
    
    if not favoritos:
        print("\n\t\t\tNo hay habitaciones en favoritos.")
    else:
        for idx, habitacion in enumerate(favoritos, 1):
            print(f"\n\t\t\t{idx}. Habitación {habitacion.numero} ({habitacion.tipo})")
            print(f"\t\t\t   Precio: ${habitacion.precio:.2f}")
            print(f"\t\t\t   Descripción: {habitacion.descripcion}")

        print("\n\t\t\tSeleccione una habitación para confirmar la reserva (0 para regresar):")
        seleccion = input("\n\t\t\tIngrese el número de la opción: ")
        
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(favoritos):
                habitacion_seleccionada = favoritos[seleccion - 1]
                confirmar_reserva(habitacion_seleccionada)
            elif seleccion == 0:
                return
            else:
                print("\n\t\t\tSelección no válida. Intente de nuevo.")
                input('\n\t\t\tPresione Enter para continuar...')
        else:
            print("\n\t\t\tEntrada no válida. Intente de nuevo.")
            input('\n\t\t\tPresione Enter para continuar...')

def main():
    hoteles = inicializar_hoteles()
    
    while not mostrar_menu_login_registro():
        print("Debe iniciar sesión o registrarse para continuar.")
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu_principal()
        reserhabi = input("\t\t\tIngrese una opción: ")
        if reserhabi == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            pais = seleccionar_pais()
            if pais and mostrar_hoteles_por_pais(hoteles, pais):
                continue
        elif reserhabi == "2":
            modificar_reserva(hoteles)
        elif reserhabi == "3":
            mostrar_reservas(hoteles)
        elif reserhabi == "4":
            mostrar_habitaciones_favoritas()
        elif reserhabi == "0":
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input('\nPresione Enter para continuar...')

if __name__ == "__main__":
    main()