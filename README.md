# 🗃️ SQLAlchemy Login System with Streamlit

## 📌 Project Overview

This project demonstrates a simple and secure login interface using **Streamlit** for the frontend and **SQLAlchemy** as the ORM (Object Relational Mapper) for database management. It includes user creation, authentication, password encryption, and basic CRUD operations, all integrated into a minimalist web interface.

---

## 📂 Features

### 🔐 Login Interface
- Developed using **Streamlit**.
- Secure password input and login logic.
- Stores session state for logged-in users.
- User feedback on login success or failure.

### 🗃️ Database and ORM (SQLAlchemy)
- SQLite database (`bd_usuarios.sqlite`) for user storage.
- Uses **SQLAlchemy ORM** for:
  - Table and column definition.
  - CRUD operations.
- Passwords are encrypted using **Werkzeug**'s hashing utilities.

### 🧑‍💼 User Model
- Attributes: `id`, `nome`, `senha` (hashed), `email`, `acesso_gestor`.
- Methods:
  - `define_senha(senha)`: Hashes the password.
  - `verifica_senha(senha)`: Verifies password input.

### 🔁 CRUD Operations
- `cria_usuarios`: Creates a new user and hashes the password.
- `ler_todos_usuarios`: Fetches all users.
- `ler_usario_id`: Fetches a user by ID.
- `modifica_usuario`: Updates user attributes, including hashed password.
- `deleta_usuario`: Deletes user by ID.

---

## 🛠️ Technologies Used
- Python
- Streamlit
- SQLAlchemy
- SQLite
- Werkzeug (for secure password hashing)

---

## 🚀 How to Run
1. Make sure you have `streamlit` and `sqlalchemy` installed:
   ```bash
   pip install streamlit sqlalchemy werkzeug 
   streamlit run tela_login.py

