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

---

## 📋 Funcionalidades

- Registrar nuevos créditos mediante un formulario.  
- Listar todos los créditos registrados en una tabla.  
- Editar y eliminar créditos existentes.  
- Visualizar una gráfica del total de créditos otorgados.  
- Validaciones básicas en el formulario.  

---

## 📁 Estructura del proyecto

Herramienta_Creditos/
├── app.py
├── database.py
├── models.py
├── templates/
│ ├── index.html
│ └── form.html
├── static/
│ ├── styles.css
│ └── chart.js
├── .gitignore
├── README.md
└── requirements.txt

yaml
Copiar
Editar

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

## 🚀 Cómo ejecutar el proyecto

Clona el repositorio:

```bash
git clone https://github.com/Reset2412/Herramienta_Creditos.git
cd Herramienta_Creditos
Crea y activa un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
python app.py
Abre tu navegador en:

arduino
Copiar
Editar
http://localhost:5000
📈 Visualización de créditos
Se utiliza Chart.js para mostrar una gráfica dinámica del total de créditos otorgados.
(Opcional: distribución por cliente o rangos de montos).

📦 Requisitos
Python 3.8 o superior

pip

📑 Criterios evaluados en el proyecto
✅ Correcto funcionamiento de la aplicación.

✅ Calidad del código y estructura del proyecto.

✅ Uso adecuado de Flask y SQLite.

✅ Diseño claro y funcional de la interfaz.

✅ Explicación y entendimiento del código (mediante comentarios y este README).

✅ Implementación correcta de la gráfica con Chart.js.

📅 Fecha de entrega
13 de julio antes de las 11:59 pm

📮 Contacto
Este proyecto fue desarrollado como parte del proceso de selección para el puesto de Ingeniero de Software Jr. en Delta Data Consulting.