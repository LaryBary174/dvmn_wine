from utils import get_year_word, categorize_wine, get_age_of_company
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

age = get_age_of_company()
wines = categorize_wine('wine3.xlsx')
rendered_page = template.render(
    age=age,
    word_form=get_year_word(age),
    wines=wines
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
