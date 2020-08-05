#!/usr/bin/env python3
import yaml
from jinja2 import Environment, FileSystemLoader
if __name__ == "__main__":
 # yaml = YAML()
 config_data = yaml.load(open('./config.yaml'))
 #print(config_data)
# Load templates file from templtes folder 
 env = Environment(loader = FileSystemLoader('/Users/yu-sung/Documents/gsp-generater/'),   trim_blocks=False, lstrip_blocks=False)
 template = env.get_template('site.yaml')
 print(template.render(config_data))