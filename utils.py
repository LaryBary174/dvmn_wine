import pandas
import datetime


def get_year_word(age):
    '''Для правильного склонения "год" или "лет" '''
    if 11 <= age % 100 <= 19:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'


def get_age_of_company():
    """ Функция считает сколько уже работает компания с 1920 года"""
    year_for_foundation = 1920
    current_year = datetime.datetime.now().year
    age = current_year - year_for_foundation
    return age


def categorize_wine(file: str):
    """ Чтение Excel и вывод в формате dict """
    exel_wine_table = pandas.read_excel(file)
    exel_wine_table.rename(columns={
        'Категория': 'category',
        'Картинка': 'image',
        'Название': 'title',
        'Сорт': 'sort',
        'Цена': 'price',
        'Акция': 'sale'
    }, inplace=True)
    exel_wine_table.fillna('', inplace=True)
    columns = exel_wine_table.columns.ravel()
    categorized_wine = {}
    for category, wine in exel_wine_table.groupby(columns[0]):
        categorized_wine[category] = wine.to_dict(orient='records')

    return categorized_wine
