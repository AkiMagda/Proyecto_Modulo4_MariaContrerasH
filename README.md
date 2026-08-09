# Gestor Inteligente de Clientes

## Descripción del proyecto

El proyecto consiste en el desarrollo de un sistema de gestión de clientes utilizando Python y los principios de Programación Orientada a Objetos (POO).
El sistema permite registrar y administrar diferentes tipos de clientes: regulares, premium y corporativos. Cada tipo de cliente posee características específicas, manteniendo atributos comunes como identificador, nombre, correo electrónico, teléfono y dirección.
Además, el programa permite realizar operaciones de creación, búsqueda, edición y eliminación de clientes, exportar información a archivos TXT y CSV y mantener un registro de las actividades realizadas en el sistema.

---

## Objetivos

- Aplicar los principios fundamentales de Programación Orientada a Objetos.
- Implementar encapsulación, herencia y polimorfismo.
- Utilizar clases y objetos para representar distintos tipos de clientes.
- Implementar validaciones y manejo de excepciones.
- Gestionar la información de los clientes.
- Exportar información utilizando archivos TXT y CSV.
- Registrar las principales operaciones realizadas por el sistema.
- Representar la estructura del sistema mediante un diagrama de clases UML.

---

## Tipos de clientes

El sistema considera tres tipos de clientes:

### Cliente Regular

Corresponde a un cliente que posee puntos acumulados.

### Cliente Premium

Corresponde a un cliente que posee un nivel de membresía y un porcentaje de descuento.

### Cliente Corporativo

Corresponde a un cliente asociado a una empresa y que posee un límite de crédito.

---

## Programación Orientada a Objetos

El proyecto utiliza los siguientes conceptos:

### Encapsulación

Los atributos de los clientes se encuentran protegidos mediante atributos privados y se accede a ellos mediante métodos getter.

### Herencia

Las clases `ClienteRegular`, `ClientePremium` y `ClienteCorporativo` heredan los atributos y métodos generales de la clase padre `Cliente`.

### Polimorfismo

Cada tipo de cliente sobrescribe el método `obtener_datos()` para mostrar información específica según sus características.

### Uso de super()

Se utiliza `super()` para reutilizar los atributos y métodos definidos en la clase padre `Cliente`.

---

## Funcionalidades

El sistema permite:

- Crear clientes.
- Listar clientes registrados.
- Buscar clientes mediante su identificador.
- Editar información de clientes.
- Eliminar clientes.
- Validar datos ingresados.
- Evitar identificadores duplicados.
- Exportar los clientes a un archivo TXT.
- Exportar los clientes a un archivo CSV.
- Registrar las operaciones realizadas en un archivo de actividad.

---

## Manejo de archivos

El proyecto genera los siguientes archivos:

- `clientes.txt`: almacena información de los clientes en formato de texto.
- `clientes.csv`: almacena los datos de los clientes en formato CSV.
- `actividad.txt`: registra las principales operaciones realizadas en el sistema.

---

## Registro de actividad

El sistema cuenta con una clase `RegistroActividad`, encargada de registrar las operaciones realizadas.

Cada registro contiene la fecha, hora y descripción de la acción realizada.

Ejemplo:

Fecha: 08-08-2026 22:40:12 | Acción: Agregó cliente 1

---

## Estructura del proyecto

El proyecto está compuesto principalmente por:

- `Cliente.py`: contiene la clase padre `Cliente` y las clases `ClienteRegular`, `ClientePremium` y `ClienteCorporativo`.
- `Gestor_Clientes.py`: contiene las funciones de gestión de clientes y el registro de actividades.
- `README.md`: contiene la documentación general del proyecto.

Durante la ejecución también se pueden generar:

- `clientes.txt`
- `clientes.csv`
- `actividad.txt`

---

## Diagrama de clases UML

El proyecto cuenta con un diagrama UML que representa las clases y sus relaciones.

Las principales relaciones implementadas son:

- Herencia entre `Cliente` y los distintos tipos de clientes.
- Agregación entre `GestorClientes` y `Cliente`.
- Composición entre `GestorClientes` y `RegistroActividad`.

El diagrama fue desarrollado utilizando Draw.io.

---

## Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- Módulo CSV
- Manejo de archivos TXT
- Draw.io para el diseño del diagrama UML
- Git y GitHub para el control de versiones y publicación del proyecto

---

## Ejecución

Para ejecutar el proyecto se debe tener Python instalado.

Desde una terminal ubicada en la carpeta del proyecto ejecutar:

```bash
python Gestor_Clientes.py
