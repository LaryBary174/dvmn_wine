import argparse

from utils import get_year_word, categorize_wine, get_age_of_company
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape



def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='Путь к Excel файлу')

    return parser

def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    args = create_parser().parse_args()
    excel_wine = args.filename
    age = get_age_of_company()
    wines = categorize_wine(excel_wine)
    rendered_page = template.render(
        age=age,
        word_form=get_year_word(age),
        wines=wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
