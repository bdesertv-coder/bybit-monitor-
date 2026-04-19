<<<<<<< HEAD
# 📈 Bybit Monitor

Приложение для мониторинга цен на интересующие валютные пары с сохранением в базу данных.

## 🛠 Стек технологий

- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **Frontend:** HTML
- **Infrastructure:** Docker, Docker Compose
- **API:** Bybit API

## ⚙️ Возможности
=======
    Bybit Monitor

Приложение для мониторинга цен на интересующие валютные пары по запросу с последующим сохранением в базу данных.

  Стек технологий

- Backend: Python, FastAPI, SQLAlchemy
- Database: PostgreSQL
- Frontend: HTML
- Infrastructure: Docker, Docker Compose
- API: Bybit API

  Возможности
>>>>>>> 4e5c5db777b7b873bf2afafd6b75e09a7d0557df

- Получение цен на интересующую валютную пару
- Сохранение цен в базе данных
- Просмотр истории через веб-интерфейс
- Полная контейнеризация через Docker

<<<<<<< HEAD
## 📋 Требования
=======
  Требования
>>>>>>> 4e5c5db777b7b873bf2afafd6b75e09a7d0557df

- Docker
- Docker Compose

<<<<<<< HEAD
## 🚀 Установка

**1. Клонировать репозиторий**
```bash
git clone https://github.com/bdesertv-coder/bybit-monitor-.git
cd bybit-monitor
```

**2. Создать .env файл**
```bash
cp .env.example .env
```

**3. Запустить через Docker**
```bash
docker compose up --build
```

**4. Открыть в браузере**
- API документация: http://localhost:8000/docs
- Веб-интерфейс: `frontend/src/index.html`

## 📸 Скриншот

![Скриншот](https://github.com/user-attachments/assets/6a3e26a9-62bb-4869-ba68-992b5524554e)

## 📁 Структура проекта

```
=======
  Установка

1. Клонировать репозиторий
bash
git clone https://github.com/bdesertv-coder/bybit-monitor-.git
cd bybit-monitor


2. Создать .env файл и вставить свои ключи Bybit
bash
cp .env.example .env


3. Запустить через Docker
bash
docker compose up --build


4. Открыть в браузере
- API документация: http://localhost:8000/docs
- Веб-интерфейс: `frontend/src/index.html`

  Скриншот

![Скриншот](https://github.com/user-attachments/assets/6a3e26a9-62bb-4869-ba68-992b5524554e)

  Структура проекта


>>>>>>> 4e5c5db777b7b873bf2afafd6b75e09a7d0557df
bybit-monitor/
├── backend/           # Python FastAPI бэкенд
├── frontend/          # Веб-интерфейс
├── database/          # SQL миграции
└── docker-compose.yml
```

<<<<<<< HEAD
## 📡 API Эндпоинты

=======

  API Эндпоинты

>>>>>>> 4e5c5db777b7b873bf2afafd6b75e09a7d0557df
| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/api/price/{symbol}` | Текущая цена пары |
| GET | `/api/orderbook/{symbol}` | Стакан заявок |
<<<<<<< HEAD
| GET | `/api/history/{symbol}` | История цен из БД |
=======
| GET | `/api/history/{symbol}` | История цен из БД |
>>>>>>> 4e5c5db777b7b873bf2afafd6b75e09a7d0557df
