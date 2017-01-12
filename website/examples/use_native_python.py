from funkybomb import Template
from models import users

tmpl = Template()
table = tmpl.table
for user in users.get_all():
    row = table.tr
    row.td + user.name
    row.td + user.age
