import json

python_str = [{'id': '1', 'name': '菜鸟教程', 'url': 'www.runoob.com'}, {'id': '2', 'name': '菜鸟工具', 'url': 'c.runoob.com'}, {'id': '3', 'name': 'Google', 'url': 'www.google.com'}]

with open('data/test1.json', 'w') as fp:
    json.dump(python_str, fp, ensure_ascii=False)
