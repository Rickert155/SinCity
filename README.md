# Lib Sin City 

<div align="center">
  <img src="https://github.com/rickert156/rickert156/blob/main/assets/sin_city.svg" alt="Sin City">
</div>

## Agent
В модуле доступна функция check_agent_list. Функция принимает один обязательный параметр agent_list, в него передается имя файла со списком user-agents:
```sh
check_agent_list(agent_list='file.txt')
```
## Web
### Whois
Простой скрипт для проверки whois

## OSINT
### Debt
Модуль для поиск долгов по ИНН

## DataGenerate
### Text Generator
Модуль для генерированания символов - пока что только из английского алфавита и цифр. Имеет два необязательных параметра:
```sh
#количество символов 
max_count_char
#количество итераций
max_word

#Значения по умолчанию
max_word:int=1, max_count_char:int=5
```

## Case
Тут находятся примеры использования модулей библиотеки

## tmp 
В этой директории хранятся примеры json и txt для user-agent

# LICENSE
Этот проект распространяется под лицензией [GNU GPLv3](./LICENSE).
Подробнее: <https://www.gnu.org/licenses/gpl-3.0.html>.
