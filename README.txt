Bybit Monitor

Приложение для мониторинга цен на интересующие валютные пары по запросу с последуюзим сохранением в базу данных.

Стек технологий:
Backend: Python, SQLAlchemy, FastAPI
Database: PostgreSQL
Frontend: HTML - разметка
Infrastructure: Docker, Docker Compose
API: Bybit API (opened)

Возможности:
Получение цен на интересующую валютную пару
Сохранение цен в базе данных
Просмотр истории через вэб-интерфейс
Полная контейнеризация через Docker

Требования:
Python 3.10+
Docker
Docker Compose

Установка:
1. Клонировать репозиторий
git clone https://github.com/bdesertv-coder/bybit-monitor.git
cd bybit-monitor
2. Создать .env файл из шаблона и вставить свои ключи Bybit
cp .env.example .env
3. Запустить через Docker
docker compose up --build
4. Открыть в браузере
- API документация: http://localhost:8000/docs
- Веб-интерфейс: frontend/src/index.html

![Скриншот](https://github.com/user-attachments/assets/6a3e26a9-62bb-4869-ba68-992b5524554e)

Структура проекта:
bybit-monitor/
├── backend/          # Python FastAPI бэкенд
├── frontend/         # Веб-интерфейс
├── database/         # SQL миграции
└── docker-compose.yml

API эндпоинты
| GET | /api/price/{symbol} | Текущая цена пары |
| GET | /api/orderbook/{symbol} | Стакан заявок |
| GET | /api/history/{symbol} | История цен из БД |

