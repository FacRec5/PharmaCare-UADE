# PharmaCare - Sistema de Gestión de Medicamentos 

**Link al Repositorio de GitHub:** [https://github.com/FacuRecs5/PharmaCare-UADE](https://github.com/FacuRecs5/PharmaCare-UADE)

---

## Alcance del Programa (Fase 1)
El objetivo de **PharmaCare Central** en esta primera fase evolutiva es proveer un sistema interactivo mediante un menú de consola que cubra las siguientes reglas de negocio:

* **1. Registrar nuevo medicamento (Alta):** Permite ingresar medicamentos de manera manual (por teclado) o generar datos aleatorios de prueba. Valida que el código sea único y alfanumérico (entre 4 y 10 caracteres).
* **2. Eliminar medicamento (Baja):** Permite la eliminación de productos mediante su código único, solicitando confirmación del usuario y con la restricción estricta de que **solo se pueden eliminar medicamentos con stock igual a cero**.
* **3. Modificar stock o precio (Modificación):** Permite la búsqueda y actualización de existencias o del precio unitario seleccionando el producto por su código o por su nombre comercial.
* **4. Informe General - Visualización de los datos:** Muestra la tabla de todos los registros aplicando un ordenamiento de **menor a mayor según los días restantes para el vencimiento**, desempatando alfabéticamente por nombre en caso de igualdad.
* **5. Salir:** Finalización controlada del sistema.
