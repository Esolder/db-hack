# db-hack

Проект содержит скрипт для редактирования оценок и замечаний в [электронном дневнике](https://github.com/devmanorg/e-diary/tree/master).
Архив с базой данных доступен по [ссылке](https://dvmn.org/filer/canonical/1562234129/166/).

## Использование скрипта

1. Поместить файл `scripts.py` в корневую папку проекта.
2. В shell вставить импорт из файла `scripts.py` (строки 1, 2).
3. В shell импортировать функции из файла:
 ```python
from scripts import find_schoolkid, fix_marks, delete_chastisements, create_commendation
```
4. Чтобы определить ученика: 
```python
schoolkid = find_schoolkid('Имя ученика')
```
5. Для исправления на пятёрки оценок ниже четвёрки: 
```python
fix_marks(schoolkid)
```
6. Для удаления замечаний: 
```python
delete_chastisements(schoolkid)
```
7. Для добавления похвалы: 
```python
create_commendation(schoolkid, 'Название предмета')
```
   
При желании можно добавить варианты похвалы в переменной `texts` функции `create_commendation` (строка 45)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).
