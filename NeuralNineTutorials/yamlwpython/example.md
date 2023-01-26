# requires pip3 install pyyaml

import yaml

with open("example.yml", "r") as f:
    #data = yaml.load(f)
    # or
    data = yaml.safe_load(f)

print(data)