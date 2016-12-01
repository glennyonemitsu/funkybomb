from zizu import Tag
from util import render


h = Tag('html')
h.p(foo='bar')
h += 'hi there'

table = h.table(id='branched off')

for i in range(2):
    tr = table.tr
    for j in range(4):
        tr.td(Tag('something' + str(j)))


print(render(h, True))

