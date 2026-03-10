# Smart Beehive — система управления и мониторинга умного улья

IoT-платформа для мониторинга состояния пчелиных семей с применением машинного обучения.

## Стек

- **Backend**: Python 3.11 / FastAPI
- **Frontend**: TypeScript / React
- **БД**: PostgreSQL + TimescaleDB, InfluxDB
- **IoT**: ESP32, Raspberry Pi 4, MQTT (EMQX)
- **ML**: TensorFlow Lite, Scikit-learn
- **DevOps**: Docker, GitHub Actions, Timeweb Cloud

## Быстрый старт

```bash
docker compose up -d
```

Backend: http://localhost:8000  
Frontend: http://localhost:3000  
Grafana: http://localhost:3001  
EMQX: http://localhost:18083
