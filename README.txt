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
1) Копирование репозитория
git clone https://github.com/bdesertv-coder/bybit-monitor.git
cd bybit-monitor
2) Создание .env файла
Заменить your_key_here и your_key_secret_here на мвои ключи
(на сайте необходимо выбрать валютные пары, которые хотите мониторить)
3) Запуск
(создание окружения)
python -m venv .venv
.venv\Scripts\activate
(скачивание библиотек)
pip install -r requirements.txt
(запуск контейнера)
uvicorn app.main:app --reload
4) Открыть в браузере
API документация: http://localhost:8000/docs
Веб-интерфейс: открыть frontend/src/index.html

Скриншот приложения (https://github.com/user-attachments/assets/6a3e26a9-62bb-4869-ba68-992b5524554e)

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

