from zizu import Tag, Template
from util import render


t = Template('root')
h = t.html
h.p += Template('test')
t['test'] = 'yes, hi indeed.'

table = h.table
for i in range(2):
    tr = table.tr
    for j in range(3):
        td = tr.td(foo='bar-'+str(i)+'-'+str(j))
        td += Template('tmpl-'+str(i)+str(j))

t['tmpl-00'] = 'zero zero'
t['tmpl-01'] = 'zero one'
t['tmpl-02'] = 'zero two'
t['tmpl-10'] = 'one zero'
t['tmpl-11'] = 'one one'
t['tmpl-12'] = 'one two'

print(render(h, True))

