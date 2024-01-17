from jinja2 import Template
import os
import csv
import yaml
import re


with open("template.html") as f:
    template = Template(f.read())


def _read_context(path):
    with open(path) as f:
        if path.endswith(".csv"):
            reader = csv.DictReader(f)
            return list(reader)
        elif path.endswith(".yaml"):
            return yaml.load(f, Loader=yaml.Loader)
        else:
            return f.read()


context = {
    filename.split('.')[0]: _read_context(os.path.join("data", filename))
    for filename in os.listdir("data")
}
with open("index.html", 'w') as f:
    rendered = template.render(**context)
    clean = re.sub(r'\n\s*\n', '\n', rendered)
    f.write(clean)
