<div align="center">
  <img src="https://github.com/rickert156/rickert156/blob/main/assets/sin_city.jpg" alt="Sin City">
</div>
# Lib Sin City 

Установка библиотеки
```sh
git clone https://github.com/rickert156/SinCity.git
```
Быстрая установка пакетов + очистка от мусора
```sh
cd SinCity && ./auto.sh
```

## Agent
С помощью модуля Agent.header можно быстро генерировать заголовки  
Сначал нужно достать agent.json из tmp
```sh
cp tmp/agent.json .
```
Для примера можно использовать скрипт
```sh
python3 -m case.template_headers
```

## Browser
Тут пара модулей - driver_chrome и scrolling  
Модули для инициализации chrome driver и для скроллинга в низ страницы сайта. Модули добавлены в библиотеку, так как на практике очень часто нужно их использовать.

## DataGenerate
По большей части это генератор текста. Используется в менеджере паролей [SinPass](https://github.com/rickert156/SinPass)   
Пример использования
```sh
python3 -m case.template_genarate_word
```

## OSINT
Набор модулей для информационной разведки из открытых источников.  
Проверка долгов по ИНН. Пример
```
python3 -m case.template_search_debt
```

## Web
Модуль whois относится к OSINT.   
Пример использования
```sh
python3 -m case.template_whois.py
```

## Scanners
Модуль с различными сканнерами.
- Сканнер портов - простейший прототип. Не брать во внимание
- Сканнер плагинов WordPress - рабочий инструмент, нужно пополнять библиотеку плагинов, что бы инструмент по ним искал. Пример использования
```sh
python3 -m case.template_scanner_plugin
```
Для него нужен файл с плагинами plugins.txt и agent.json(опционально) для улучшения запросов
