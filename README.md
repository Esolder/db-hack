# db-hack

Проект содержит скрипт для редактирования оценок и замечаний в [электронном дневнике](https://github.com/devmanorg/e-diary/tree/master).
Архив с базой данных доступен по [ссылке](https://dvmn.org/filer/canonical/1562234129/166/).

## Использование скрипта

1. Поместить файл `scripts.py` в корневую папку проекта
2. В shell вставить импорт из файла `scripts.py` (строки 1, 3)
3. В shell импортировать функции и список похвал из файла:
```from scripts import COMMENDATION_TEXTS, create_commendation, delete_chastisements, find_schoolkid, fix_marks```
4. Чтобы определить ученика:
```schoolkid = find_schoolkid('Имя ученика')```
5. Для исправления на пятёрки оценок ниже четвёрки: 
```fix_marks(schoolkid)```
6. Для удаления замечаний: 
```delete_chastisements(schoolkid)```
7. Для добавления похвалы: 
```create_commendation(schoolkid, 'Название предмета')```
   
При желании можно добавить варианты похвалы в переменной `texts` функции `create_commendation` (строка 45)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).