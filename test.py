from zizu import Tag, Template
from util import render


t = Template('root')
h = t.html
h.p(foo='bar')
h += 'hi there'
h += Template('test')

table = h.table(id='branched off')

for i in range(2):
    tr = table.tr
    for j in range(2):
        tr.td(Tag('something' + str(j)))


t['test'] = 'yes, hi indeed.'
print(render(h, True))

