# 🚗 Smart Parking System

## 📌 Description

Smart Parking est une application permettant de détecter et afficher en temps réel les places de parking disponibles, avec une couche d’intelligence artificielle pour l’analyse et la prédiction.

---

## 🧠 Architecture

```
Simulation capteurs (IISE)
        ↓
Backend API (IL)
        ↓
Base de données MySQL
        ↓
Frontend React (IL)
        ↓
Analyse & IA (ADIA)
```

---

## 📁 Structure du projet

```
smart-parking/
│── frontend-react/       # Interface utilisateur (React)
│── backend/              # API (Flask / PHP / Spring Boot)
│── simulation-iise/      # Simulation capteurs
│── ai-adia/              # IA & analyse des données
│── database/             # Scripts SQL
│── README.md
```

---

## 🌿 Branches

| Branche         | Description               |
| --------------- | ------------------------- |
| main            | Version finale intégrée   |
| frontend-il     | Interface React           |
| backend-il      | API                       |
| simulation-iise | Capteurs                  |
| ai-adia         | Intelligence artificielle |

---

## ⚙️ Technologies utilisées

* Frontend : React.js
* Backend : Flask / PHP / Spring Boot
* Base de données : MySQL
* Simulation : Python
* IA : Python (Machine Learning)
* Versioning : Git & GitHub

---

## 🤖 Partie IA (ADIA)

L’ADIA est responsable de :

* 📊 Analyse des données des capteurs
* 📈 Statistiques (taux d’occupation)
* 🔮 Prédiction des places libres
* 🧠 Modèles simples de Machine Learning

### Exemple d’analyses possibles :

* heures de pointe
* taux d’occupation par zone
* prédiction disponibilité

---

## 🚀 Installation et lancement

### 1. Cloner le projet

```bash
git clone https://github.com/USERNAME/smart-parking.git
cd smart-parking
```

---

### 2. Base de données

```bash
mysql -u root -p < database/schema.sql
```

---

### 3. Backend

```bash
cd backend
python app.py
```

---

### 4. Frontend

```bash
cd frontend-react
npm install
npm start
```

---

### 5. Simulation capteurs

```bash
cd simulation-iise
python simulate.py
```

---

### 6. IA / Analyse

```bash
cd ai-adia
python analysis.py
```

---

## 🔄 Fonctionnement

* IISE simule les capteurs
* IL développe backend + frontend
* ADIA analyse les données et ajoute l’intelligence
* Interface affiche :

  * 🟢 Libre
  * 🔴 Occupée

---

## 👥 Répartition du travail

| Filière | Rôle               |
| ------- | ------------------ |
| IL      | Frontend + Backend |
| IISE    | Capteurs           |
| ADIA    | IA + Analyse       |

---

## 📊 Améliorations possibles

* Dashboard intelligent
* Prédictions avancées
* Notifications en temps réel
* WebSocket

---

## 📎 Auteur

Projet Smart Parking – Travail en groupe (IL / IISE / ADIA)
