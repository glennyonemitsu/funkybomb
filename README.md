# Funkybomb - quick DOM like tree building

Funkybomb uses Python's magic methods to help you quickly build a DOM like tree
for HTML.

Start with an empty template, add the first element, and render it:

```python
>>> tmpl = Template()
>>> tmpl.html  # node is added
>>> render(tmpl)

<html></html>
```

Elements can have attributes:

```python
>>> tmpl = Template()
>>> tmpl.p(foo='bar')
>>> render(tmpl)

<p foo="bar"></p>
```

Add text:

```python
>>> tmpl = Template()
>>> tmpl.p + 'hi'
>>> render(tmpl)

<p>hi</p>
```

You cannot reference previously made children nodes (at least not easily), so
you can use references:

```python
>>> tmpl = Template()
>>> html = tmpl.html
>>> html.p + 'First paragraph'
>>> html.p + 'Second paragraph'
>>> render(tmpl, pretty=True)

<html>
    <p>
        First paragraph
    </p>
    <p>
        Second paragraph
    </p>
</html>
```

You can also have content placeholders:

```python
>>> tmpl = Template()
>>> sub_tmpl = Template('my-placeholder')
>>> sub_tmpl + 'default text'
>>> tmpl.div + sub_tmpl
>>> render(tmpl)

<div>default text</div>

>>> tmpl['my-placeholder'] = 'updated text'
>>> render(tmpl)

<div>updated text</div>
```

Some a more advanced example:

```python
>>> from funkybomb.node import Tag
>>> tmpl = Template()
>>> p = tmpl.p
>>> p + ('this ', 'is ', 'a ', (Tag('em') + 'test'))
>>> tmpl.foo(foo='bar') + 'this is another'
>>> render(tmpl, pretty=True)

<p>
    this is a <em>test</em>
</p>
<foo foo="bar">
    this is another
</foo>
```

Since templates are meant to be reused and mutability can make these change,
you can also lock the node tree in place.

```python
>>> from funkybomb.util import freeze
>>> tmpl = Template()
>>> sub_tmpl = Template('my-placeholder')
>>> sub_tmpl + 'default text'
>>> tmpl.div + sub_tmpl
>>> freeze(tmpl)
>>> tmpl.p + 'this cannot happen'

exception thrown here

>>> render(tmpl)

<div>default text</div>

>>> # template placeholders are still mutable
>>> tmpl['my-placeholder'] = 'updated text'
>>> render(tmpl)

<div>updated text</div>
```
