from funkybomb import Template, Text

from application.util import route
from templates import documentation
from templates.util import (
    header, p, show_html, show_python, show_text, template
)


@route('/docs/basics')
@template(documentation.tmpl)
async def docs_basics_home(req):
    t = Template()
    t + p('Coming soon.')

    return {
        'content': t,
        'headline': Text('Basics')
    }


@route('/docs/basics/installation')
@template(documentation.tmpl)
async def docs_basics_installation(req):
    t = Template()
    t + p('Funky Bomb is available via PyPi and install is simple')
    t + show_text('pip install funky-bomb')

    return {
        'content': t,
        'headline': Text('Installation')
    }


@route('/docs/basics/syntax')
@template(documentation.tmpl)
async def docs_basics_syntax(req):
    t = Template()

    t + header('Creating the HMTL tree')
    t + p(
        'Funky Bomb aims to recreate the HTML tree with Python syntax. '
        'Starting with an empty template.'
    )
    t + show_python(
        '''
        from funkybomb import Template

        tmpl = Template()
        '''
    )

    t + p(
        'Currently there is no tag inside this template. To start adding '
        'HTML tags, just use attributes like you would in Python. Once you '
        'create an attribute, the tag is part of the HMTL tree. We can see the '
        'output of the HTML using the render function.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template

        tmpl = Template()
        tmpl.p
        render(tmpl)  # output: <p></p>
        '''
    )

    t + p('To add text to a tag, we "add a string" to it.')
    t + show_python(
        '''
        from funkybomb import render, Template
        tmpl = Template()
        tmpl.p  # continuing from previous code sample
        tmpl.p + 'Hello, World!'
        render(tmpl)  # output: <p></p><p>Hello, World!</p>
        '''
    )

    t + header('Controlling where the HTML tags are made')
    t + p(
        'You might notice is there is a second <p> tag. This is because funky '
        'bomb always appends tags with new attribute access . But if '
        'we want to manipulate tags at all levels we can use variables to move '
        'around in the tag tree. This is possible because creating tags with '
        'attributes also returns the tag node object.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template
        tmpl = Template()
        ul = tmpl.ul
        for line in ('foo', 'bar', 'baz'):
            ul.li + line
        render(tmpl)
        '''
    )
    t + p('The HTML output')
    t + show_html(
        '''
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
        '''
    )
    t + p(
        'Note even though we call render on the tmpl node, it held '
        'references to the ul node. Adding tags to ul adds to the tree in tmpl.'
    )

    t + header('Tag attributes', 3)
    t + p(
        'To add HTML attributes to your tag just "call" your attribute on '
        'creation time with the key/value pairs. To create "class" attributes '
        'use the special "_class" key. This is to get around "class" being a '
        'Python keyword.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template
        tmpl = Template()
        tmpl.p(_class='greeting', foo='bar') + 'Hello, World!'
        render(tmpl)

        # output: <p class='greeting' foo='bar'>Hello, World!</p>
        '''
    )

    t + header('Explicit Text Nodes', 3)
    t + p(
        'Using the "+ \'string value\'" notation is a convenient way to add '
        'text to your HTML. Under the hood this creates a Text node similar to '
        'the HTML DOM. You can create these explicitly as well.'
    )
    t + show_python(
        '''
        from funkybomb import Template, Text
        tmpl = Template()
        tmpl.p + 'Hello, World!'
        tmpl.p + Text('Hello, World!')  # functionally the same
        '''
    )

    t + header('Explicit Tag Nodes', 3)
    t + p(
        'Tag creation using the Python dot attribute name syntax also is a '
        'convenience shortcut that creates Tag objects. Just like the Text '
        'nodes you can create these explicitly along with tag attributes.'
    )
    t + show_python(
        '''
        from funkybomb import Tag, Template
        greeting = Tag('p', _class='greeting') + 'Hello, World!'
        tmpl = Template()
        tmpl + greeting
        '''
    )
    t + p('Using the Tag objects allows you to embed tags inside the tree.')
    t + show_python(
        '''from funkybomb import Tag\n'''
        '''greeting = Tag('p', _class='greeting') + '''
        ''''Hello, ' + (Tag('em') + 'World!')'''
    )
    t + p(
        'This might be a bit confusing, so let\'s unravel this step by step.'
    )
    t + show_python(
        '''
        from funkybomb import Tag
        greeting = Tag('p', _class='greeting')
        greeting + 'Hello, '
        subject = Tag('em') + 'World!'  # this is encapsulated inside the ()
        greeting + subject
        '''
    )

    return {
        'content': t,
        'headline': Text('Syntax')
    }


@route('/docs/basics/templating')
@template(documentation.tmpl)
async def docs_basics_templating(req):
    t = Template()

    t + p(
        'Template nodes are important building blocks to make websites quickly '
        'and efficiently. Functionally you can think of them as any other HTML '
        'node but that doesn\'t have any output during rendering.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template

        tmpl = Template()
        tmpl + Template()
        # ...
        tmpl + Template()
        render(tmpl)  # outputs nothing
        '''
    )

    t + p(
        'Since they have no output side effects, one basic way to use them is '
        'as a node tree container.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template

        tmpl = Template()
        container = tmpl.div
        greeting = Template()
        greeting.p + 'Hello, World!'
        question = Template()
        question.p + 'How are you feeling today?'
        answer = Template()
        answer.p + 'I am feeling alright'
        greeting + question
        greeting + answer
        container + greeting
        render(tmpl)
        '''
    )
    t + p('The HTML output')
    t + show_html(
        '''
        <div>
            <p>Hello, World!</p>
            <p>How are you feeling today?</p>
            <p>I am feeling alright</p>
        </div>
        '''
    )

    t + header('Template blocks', 2)
    t + p(
        'All good templating systems need a way to inject data into specific '
        'sections of the output. We can assign names to the Template node '
        'objects on creation time. These template nodes\' children are treated '
        'as the default content.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template, Tag

        tmpl = Template()
        default = Template('replace me')
        default.p + 'This is the default content'
        tmpl + default
        render(tmpl)  # <p>This is the default content</p>

        context = {'replace me': Tag('h1') + 'Hello'}
        render(tmpl, context=context)  # <h1>Hello</h1>
        '''
    )
    t + p(
        'Named Template nodes can be nested and replaced with the single '
        'context object.'
    )
    t + show_python(
        '''
        from funkybomb import render, Template, Tag

        tmpl = Template()
        default = Template('replace me')
        default.p + 'This is the default content'
        inner_tmpl = Template('inner template')
        inner_tmpl.p + 'Another template to replace'
        default + inner_tmpl  # nesting template
        tmpl + default
        context = {'inner template': Tag('h1') + 'Hello'}
        render(tmpl, context=context)
        '''
    )
    t + show_html(
        '''
        <p>This is the default content</p>
        <h1>Hello</h1>
        '''
    )

    t + header('Freezing templates', 2)
    t + p(
        'Using templates can be a bit dangerous because in Python, any changes '
        'to a node object will remain intact. This means templates can change '
        'over the running lifetime of a webserver.',

        'Funky Bomb allows you to "freeze" your base templates so you can '
        'reuse them with different render contexts without side effects.'
    )
    t + show_python(
        '''
        from funkybomb import freeze, Template

        tmpl = Template()
        tmpl.p + 'Hello, World!'
        freeze(tmpl)
        tmpl.p + 'This will not be allowed'
        '''
    )

    t + header('Replacing templates', 2)
    t + p(
        'Sometimes freezing might not be enough. In some cases base templates '
        'are just building blocks for other templates where freezing and using '
        'contexts are not enough. To permanently replace templates use the '
        'dictionary style item assignment syntax.',

        'A common pattern for reuse is to do a deepcopy of the templates, then '
        'replacing anything inside. More details on this is available in the '
        'common patterns section.'
    )
    t + show_python(
        '''
        from copy import deepcopy
        from funkybomb import render, Template, Text

        base_tmpl = Template()
        base_tmpl.h1 + Template('base content')
        tmpl = deepcopy(base_tmpl)
        tmpl['base content'] = Text('headline')
        render(tmpl)  # output: <h1>headline</h1>
        tmpl['base content'] = Text('another headline')
        render(tmpl)  # output (notice no change): <h1>headline</h1>
        '''
    )

    return {
        'content': t,
        'headline': Text('Templating')
    }


@route('/docs/basics/utilities')
@template(documentation.tmpl)
async def docs_basics_utilities(req):
    t = Template()
    t + p('Coming soon.')

    return {
        'content': t,
        'headline': Text('Utilities')
    }
