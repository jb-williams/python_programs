import yaml

data = {
    "name": "Mike",
    "age": 25,
    "languages": ["Bash,", "Python", "Perl"],
    "address": {
        "city": "NYC",
        "ZIP": "239823",
        "country": "US"
    }
}
with open("somefile.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)