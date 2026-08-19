# Soporte de tickets

Sistema interactivo para gestionar tickets usando una cola con prioridad: los tickets se atienden primero por prioridad y en dado caso que sean de la misma categoría se toma la hora de llegada. El programa corre en un bucle interactivo, manteniendo los tickets en memoria mientras este corriendo.

## Tecnologías

- Python 3.12
- Estructura de datos: Cola de prioridad (implementación propia)

## Instalación 

1. Clona el repositorio:

​```bash
git clone https://github.com/sdiego-s/soporte-tickets.git
cd soporte-tickets
​```

2. Corre el programa:

​```bash
python main.py
​```

## Uso

Al correr el programa, se abre un menú interactivo con 4 comandos: `agregar`, `atender`, `ver`, `salir`.

Ejemplo de sesión:

```
> agregar
Descripción del problema: Servidor caído
Prioridad (alta/media/baja): alta
Canal (presencial/telefono/internet): telefono
Ticket agregado

> ver
  [1] alta - Servidor caído

> atender
Atendiste: [1] Servidor caído

> salir
Cerrando el sistema
```

## Decisiones técnicas

**¿Por qué una cola de prioridad y no una lista simple?**

Con una lista simple tendría que revisar los tickets uno por uno cada vez que quiero saber a quién atender, sin ninguna garantía de encontrar rápido al de mayor prioridad. La cola de prioridad resuelve esto directamente ya que siempre entrega el ticket de mayor importancia sin importar en qué orden llegaron.

**¿Cómo funciona el desempate?**

Al comparar los tickets, si dos tienen la misma prioridad, se usa la hora de llegada para desempatar y decidir cuál se atiende primero.

**¿Por qué un REPL y no un CLI de un solo comando (como argparse)?**

No use argparse porque al terminar cada ejecución los tickets se perderían, al no tener una base de datos que los guarde. Por eso elegí un REPL ya que mantiene el programa corriendo hasta que el usuario decide cerrarlo, así los tickets no se pierden mientras está abierto. Sigue siendo una decisión poco práctica para un caso real, pero la tomé para enfocarme en la estructura de datos y su lógica.

**¿Por qué no usa base de datos?**

Fue una decisión consciente para enfocar el proyecto en la lógica de la estructura de datos (comparación, prioridad, desempate) en lugar de la complejidad de persistencia.

## Nota sobre el desarrollo

Construí este proyecto con ayuda de Claude como tutor. Elegí este tema porque estructuras de datos no me quedó del todo claro cuando lo vimos en la universidad, así que usé este proyecto para reforzarlo con un caso práctico. Claude me explicó los conceptos, señaló mis errores y me guio en la estructura a seguir, pero todo el código lo escribí, depuré y probé yo mismo, línea por línea.
