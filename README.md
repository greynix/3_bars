# Ближайшие бары

Скрипт получает на вход json файл и выводит информацию о:
- Баре с наименьшим колличеством посадочных мест
- Баре с наибольшим колличеством посадочных мест
- Ближайшем к заданым координатам баре

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
{'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'AdmArea': 'Южный административный округ', 'SeatsCount': 450, 'system_object_id': '00138530', 'PublicPhone': [{'global_object_id': 169375059.0, 'PublicPhone': '(905) 795-15-84', 'system_object_id': '00138530 _1', 'global_id': 33761.0}], 'geoData': {'type': 'Point', 'coordinates': [37.638228501070095, 55.70111462948684]}, 'global_id': 169375059, 'District': 'Даниловский район', 'Longitude_WGS84': '37.6382285008039050', 'ID': '00138530', 'TypeObject': 'бар', 'Latitude_WGS84': '55.7011146292467670', 'Address': 'Автозаводская улица, дом 23, строение 1', 'SocialPrivileges': 'нет'}
```
В качестве аргументов принимаются:
```#!bash

-h       # вывод помощи 
-json_file # путь к json файлу, по умолчанию data.json
biggest  # для поиска бара с наибольшим колличеством посадочных мест
smallest # для поиска бара с наименьшим колличеством посадочных мест
closest  # для поиска ближайшего бара
    latitude  # широта
    longitude # долгота
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
