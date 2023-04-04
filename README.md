# test-task

Щоб встановити проект:
1. Склонувати з гіта
2. Відкрити в PyCharm вибравши в налаштуванях інтерпритатор venv
3. Активуємо середовище venv\Scripts\activate
4. Встановлюєм пакети pip install -r requirements.txt
5. Створюємо міграції python manage.py makemigrations CarsApp
6. Проводим міграції python manage.py migrate CarsApp python manage.py migrate
7. Заповнюм базу даних python manage.py generate_cars <count>, де count кількість автомобілів, які будуть згенеровані
8. Запускаєм сервер python manage.py runserver
