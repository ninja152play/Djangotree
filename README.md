Древовидное меню для Django
=====
Гибкое меню с неограниченной вложенностью и автоматической подсветкой активных пунктов

# 🚀 Быстрый старт
1. Установка

Добавьте приложение menu в свой Django-проект:

```bash
# Скопируте папку 'menu' в свой проект
# Добавьте в INSTALLED_APPS (settings.py):
INSTALLED_APPS = [
    ...
    'menu',
]
```
2. Настройка базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Создание меню

Зайдите в админку (/admin/) → Menu items → добавьте пункты меню.

# 🌳 Как создать меню?
Через админку Django:

Укажите:

Название (например, "Главная")

URL (/ или именованный URL из urls.py)

Родительский пункт (оставьте пустым для корневого уровня)

Название меню (например, main_menu)

Пример структуры:

```text
- Главная (/)  
- Блог (/blog/)  
  - Новости (/blog/news/)  
  - Статьи (/blog/articles/)  
- О нас (/about/) 
``` 

# 💻 Использование в шаблонах
Загрузите тег в шаблоне:

```html
{% load draw_menu %}
```
Вставьте меню по его названию:
```html
{% draw_menu 'main_menu' %}
```
Результат для страницы /blog/news/:

<ul class="menu">
    <li><a href="/">Главная</a></li>
    <li class="active-parent">
        <a href="/blog/">Блог</a>
        <ul class="submenu">
            <li><a href="/blog/news/" class="active">→ Новости</a></li>
            <li><a href="/blog/articles/">→ Статьи</a></li>
        </ul>
    </li>
    <li><a href="/about/">О нас</a></li>
</ul>

# 🎨 Кастомизация

### CSS-стили

Добавьте в ваш base.css:

```css
.menu .active { 
    color: red;
    font-weight: bold;
}
.menu .active-parent > a {
    color: blue;
}
.submenu {
    margin-left: 20px;
    list-style: none;
}
```
### Изменение HTML

Редактируйте файл:

- menu/templates/menu/menu.html

# ⚙️ Технические детали
- 1 SQL-запрос на меню (оптимизированная работа)

- Поддержка именованных URL (name из urls.py)

- Автоматическая подсветка активных пунктов

- Несколько меню на одной странице

# ❓ Помощь
Если меню не отображается:

- Проверьте, что menu_name в админке совпадает с названием в теге

- Убедитесь, что пункты меню имеют parent = NULL для корневого уровня

- Перезапустите сервер: python manage.py runserver