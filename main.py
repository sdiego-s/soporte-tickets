from datetime import datetime
from cola_prioridad import ColaPrioridad


def main():
    cola = ColaPrioridad()

    while True:
        comando = input("\n> ").strip().lower()

        if comando == "salir":
            print("Cerrando el sistema")
            break
        elif comando == "agregar":
            desc = input("Descripición del problema: ")
            if desc.strip() == "":
                print("La descripción no puede estar vacía")
                continue
            prioridad = input("Prioridad (alta/media/baja): ")
            if prioridad.lower().strip() not in ["alta", "media", "baja"]:
                print("Error: la prioridad debe ser alta, media o baja")
                continue
            canal = input("Canal (presencial/telefono/internet): ")
            if canal.lower().strip() not in ["presencial", "telefono", "internet"]:
                print("Error: el canal debe ser presencial, telefono o internet")
                continue
            hora = datetime.now().strftime("%H:%M")
            cola.agregar_ticket(desc, prioridad, canal, hora)
            print("Ticket agregado")
        elif comando == "atender":
            try:
                siguiente = cola.atender_siguiente()
                print(f"Atendiste: [{siguiente.identificador}] {siguiente.descripcion}")
            except ValueError as error:
                print(error)
        elif comando == "ver":
            tickets = cola.ver_cola()
            if not tickets:
                print("No hay tickets en cola")
            else:
                for t in tickets:
                    print(f" [{t.identificador}] {t.prioridad} - {t.descripcion}")
        else:
            print("Comando no reconocible. Usa:agregar,atender,ver,salir")


if __name__ == "__main__":
    main()
