# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установить все зависимости
```
pip install -r requirements.txt
```
- Необходимо создать эксель файл с таблицей
### Пример файла Excel для загрузки данных 
| Категория      | Название              | Сорт              | Цена | Картинка                | Акция                  |
|----------------|-----------------------|-------------------|------|-------------------------|------------------------|
| Белые вина     | Белая леди            | Дамский пальчик   | 399  | belaya_ledi.png         | Выгодное предложение  |
| Напитки        | Коньяк классический   |                   | 350  | konyak_klassicheskyi.png|                        |
| Белые вина     | Ркацители             | Ркацители         | 499  | rkaciteli.png           |                        |
| Красные вина   | Черный лекарь         | Качич             | 399  | chernyi_lekar.png       |                        |


Картинки новые сохранять в папке `images`

- Запустите сайт командой, указав имя эксель файла 
```
py main.py -f wine.xlsx
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
