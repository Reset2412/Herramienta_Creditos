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

```yaml
Herramienta_Creditos/
├── app.py
├── database.py
├── models.py
├── templates/
│   ├── index.html
│   └── form.html
├── static/
│   ├── styles.css
│   └── chart.js
├── .gitignore
├── README.md
└── requirements.txt
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