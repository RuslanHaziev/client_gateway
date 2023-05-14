from typing import Union
from fastapi import FastAPI
# from read_file import config_reader


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/root}")  # "0.0.0.0/root
def root():
    return {"item_id": "hello"}


@app.get("/read_message}")  # "0.0.0.0/read_message
def read_message():
    # from jinja2 import Template
    #
    # html = open('foopkg/templates/0.hello.html').read()
    # template = Template(html)
    # print(template.render(name=u'Петя'))
    return render template "index.html"


