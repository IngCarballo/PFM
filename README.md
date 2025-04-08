# 💰 Personal Finance Manager

Este proyecto es una plataforma de control financiero personal, donde los usuarios pueden registrar ingresos y egresos, visualizar su historial y mantener un control detallado de su economía. Además, cuenta con un panel de administración para gestión de usuarios.

## 🚀 Tecnologías utilizadas

- ⚙️ **Backend:** Django + Django REST Framework
- 💾 **Base de Datos:** MySQL
- 🌐 **Frontend:** React.js
- 🔐 **Autenticación y Sesiones:** Django Rest Framework Sessions + CSRF Token

---

## 📦 Características

### 👥 Usuarios

- **Usuarios comunes:**
  - Registro y login
  - Registrar ingresos y egresos
  - Ver su propio historial de movimientos

- **Administrador:**
  - Ver todos los movimientos del sistema
  - Crear, editar y eliminar usuarios
  - Acceso a todos los movimientos y datos de la base

### 💸 Movimiento de dinero

Cada movimiento (ingreso o egreso) contiene:

- `monto`: número decimal
- `descripción`: texto libre
- `forma de pago`: (efectivo, tarjeta, transferencia, etc.)
- `link`: URL opcional asociado (ej: link al comprobante)
- `icono`: representación visual opcional
- `fecha`: fecha y hora del movimiento

---

## 🏗️ Estructura del Proyecto

```
backend/
│   manage.py
│
├── finance/               # Proyecto Django principal
│
├── transactions/          # App encargada de los movimientos
│
└── users/                 # App encargada de usuarios y autenticación

frontend/
│
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/          # Manejo de llamadas a la API
│   ├── App.js
│   └── index.js
```

---

## 🛠️ Requisitos

- Python 3.10+
- Node.js 18+
- MySQL 8.x
- pipenv o venv
- npm o yarn

---

## ⚙️ Configuración inicial

### 🔧 Backend

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/finance-manager.git
cd backend
```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Crear base de datos en MySQL:
```sql
CREATE DATABASE finance_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

4. Configurar `.env` con credenciales de base de datos.

5. Migrar modelos:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Ejecutar servidor:
```bash
python manage.py runserver
```

---

### ⚛️ Frontend

1. Desde la raíz:
```bash
cd frontend
npm install
```

2. Ejecutar frontend:
```bash
npm start
```

---

## 📡 Comunicación Frontend <-> Backend

- Todas las comunicaciones se realizan vía **REST API**.
- Formato de datos: `JSON`.
- Control de sesión mediante **SessionAuthentication** (con CSRF token).

---

## ✅ Próximos pasos

- [ ] Crear las apps `transactions` y `users` en Django
- [ ] Configurar JWT o Session Auth para usuarios
- [ ] Definir los endpoints de la API
- [ ] Crear modelos de usuarios y movimientos
- [ ] Implementar frontend con React + llamadas a la API
- [ ] Tests automatizados

---

## ✨ Contribuciones

¡Se aceptan PRs, sugerencias y mejoras! Cualquier colaboración es bienvenida 🚀

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.