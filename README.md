# Herramienta_Creditos

Aplicación web desarrollada con Flask y SQLite para registrar y gestionar créditos. Incluye una API con operaciones CRUD, una interfaz sencilla con HTML/CSS/JS y una gráfica interactiva del total de créditos otorgados. Proyecto realizado como examen práctico para Delta Data Consulting.

---

## 🧩 Tecnologías utilizadas

- Python 3.x  
- Flask  
- SQLite  
- HTML5 + CSS3  
- JavaScript  
- Chart.js
- Jinja2 (sistema de plantillas de Flask)  
- Bootstrap

---

## 📋 Funcionalidades

- Registrar nuevos créditos mediante un formulario.  
- Listar todos los créditos registrados en una tabla.  
- Editar y eliminar créditos existentes.  
- Visualizar una gráfica del total de créditos otorgados.  
- Validaciones básicas en el formulario.  

---

## 📁 Estructura del proyecto

```yaml
Herramientao_Creditos/
├── app.py # Archivo principal de la aplicación Flask
├── database/
│ └── creditos.db # Base de datos SQLite
├── static/
│ └── bootstrap.css # Estilos CSS
├── templates/
│ ├── editarCredito.html
│ ├── index.html
│ ├── listaCredito.html
│ └── registroCredito.html
├── Pipfile # Gestión de dependencias (Pipenv)
├── Pipfile.lock
└── README.md
```

---

## 🗃️ Base de datos

Se utiliza SQLite con una tabla llamada `creditos` con los siguientes campos:

| Campo            | Tipo     | Descripción                   |
|------------------|----------|-------------------------------|
| `id`             | entero   | Clave primaria, autoincremental |
| `cliente`        | texto    | Nombre del cliente             |
| `monto`          | real     | Monto del crédito              |
| `tasa_interes`   | real     | Tasa de interés                |
| `plazo`          | entero   | Plazo en meses                 |
| `fecha_otorgamiento` | texto | Fecha en formato `YYYY-MM-DD`  |

---

## Recuerda Instalas Python y SQLite

-Python https://www.python.org/downloads/ Ultima Version
-SQLite3 https://www.sqlite.org

---

## 🚀 Cómo ejecutar el proyecto

Clona el repositorio:
```bash
git clone https://github.com/Reset2412/Herramienta_Creditos.git
cd Herramientao_Creditos-main
```

Crea y activa un entorno virtual (opcional pero recomendado):
```bash
pip install pipenv
pipenv shell

python -m venv venv
pipenv install
```

Instala las dependencias:
```bash
pipenv install flask
pipenv install Flask-SQLAlchemy
pip install -r requirements.txt
```

Ejecuta la aplicación:
```bash
python app.py
```

---

## 📦 Requisitos
Python 3.8 o superior

---

## 📑 Criterios evaluados en el proyecto

Correcto funcionamiento de la aplicación.

- Calidad del código y estructura del proyecto.
- Uso adecuado de Flask y SQLite.
- Diseño claro y funcional de la interfaz.
- Explicación y entendimiento del código (mediante comentarios y este README).
- Implementación correcta de la gráfica con Chart.js.

---

## 📅 Fecha de entrega

13 de julio antes de las 11:59 pm

---
## 📮 Contacto

Este proyecto fue desarrollado como parte del proceso de selección para el puesto de Ingeniero de Software Jr. en Delta Data Consulting.