# 🌐 UVDomJudge - Core API Module

This repository contains the **API module** of the UVDomJudge system. It acts as the **backend brain**, handling course creation, user actions, and coordination with the Docker-based execution module.

---

## 🧩 Role in the System

The API serves as the **intermediary between the frontend and the Docker execution engine**. It exposes endpoints to:

- 📚 Create new courses
- 👤 Associate users (teachers/students) with courses
- 💬 Receive language selection and user actions
- 🐳 Trigger the creation of containers based on selected languages

---

## 🚀 Features

- 🛠️ RESTful API design
- 📦 Course management (create, read, update)
- 🔗 Communication with Docker execution engine
- 🧠 Language-based container orchestration

---

## 🔧 Technologies Used

- 🐍 Python (FastAPI / Flask)
- 🐳 Docker SDK or subprocess interface
- 📄 JSON-based communication
