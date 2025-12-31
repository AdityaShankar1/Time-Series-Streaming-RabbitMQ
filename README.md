# Time-Series-Streaming-RabbitMQ

## 1. 🏭 Project Overview 
This project demonstrates a **time-series streaming pipeline** using RabbitMQ, MongoDB, Pandas, and Flask.  
It simulates how electricity grid data (consumption, production, energy mix) can be ingested, persisted, analyzed, and visualized — a workflow similar to downstream IoT data analytics.

The focus is on **systems engineering**: message brokers, persistence, analytics, and containerization.

---

## 2. 🔑 Key Features 
- **Message Broker Integration**: RabbitMQ streams simulated time-series data.  
- **Database Persistence**: MongoDB stores incoming messages for durability.  
- **Analytics Engine**: Pandas computes export/import hours, energy mix, and hourly consumption patterns.  
- **Visualization**: Matplotlib plots (daily averages, energy distribution pie, hourly consumption).  
- **Frontend**: Flask app with login (hardcoded credentials) and report page.  
- **Testing**: Pytest suite for routes and analytics functions.  
- **Containerization**: Docker + Docker Compose for reproducible deployment.

---

## 3. 🛠️ Technical Stack 
- **Language**: Python 3.14  
- **Libraries**: Flask, Pandas, Matplotlib, Pytest, Pika (RabbitMQ), PyMongo  
- **Message Broker**: RabbitMQ  
- **Database**: MongoDB  
- **Containerization**: Docker, Docker Compose  

---

## 4. 🏗️ Architecture 

[Producer] → RabbitMQ → [Consumer] → MongoDB → [Analytics (Pandas)] → Flask Dashboard

---

## 5. 🚀 How to Run
### Local
```bash
python app.py
```

---

## 6. 📷 Output Screenshots

### First Prototype:

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 3 14 31 AM" src="https://github.com/user-attachments/assets/29e93819-af5e-499d-a5f5-02090a6a96bb" />

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 3 15 12 AM" src="https://github.com/user-attachments/assets/89bb67d4-d7e3-4fbe-9be0-3ce997925324" />

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 3 15 25 AM" src="https://github.com/user-attachments/assets/cc368b64-9e5a-46ed-9035-f03ae791704a" />

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 3 15 31 AM" src="https://github.com/user-attachments/assets/caa47636-0e39-4daa-9672-e9ab5027593e" />

### Post WCAG Compliance Enhancements:

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 6 27 37 PM" src="https://github.com/user-attachments/assets/4c0b15f8-2eff-47b9-9dde-dbc11d8b34cc" />

<img width="1470" height="956" alt="Screenshot 2025-12-31 at 6 28 32 PM" src="https://github.com/user-attachments/assets/1025b87a-2072-4f3a-854a-2175f3f5e374" />
