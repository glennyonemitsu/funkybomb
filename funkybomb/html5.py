from funkybomb.node import Tag


class a(Tag):
    tag = 'a'


class abbr(Tag):
    tag = 'abbr'


class acronym(Tag):
    tag = 'acronym'


class address(Tag):
    tag = 'address'


class applet(Tag):
    tag = 'applet'


class area(Tag):
    tag = 'area'
    is_void = True


class article(Tag):
    tag = 'article'


class aside(Tag):
    tag = 'aside'


class audio(Tag):
    tag = 'audio'


class b(Tag):
    tag = 'b'


class base(Tag):
    tag = 'base'
    is_void = True


class basefont(Tag):
    tag = 'basefont'


class bdi(Tag):
    tag = 'bdi'


class bdo(Tag):
    tag = 'bdo'


class bgsound(Tag):
    tag = 'bgsound'


class big(Tag):
    tag = 'big'


class blink(Tag):
    tag = 'blink'


class blockquote(Tag):
    tag = 'blockquote'


class body(Tag):
    tag = 'body'


class br(Tag):
    tag = 'br'
    is_void = True


class button(Tag):
    tag = 'button'


class canvas(Tag):
    tag = 'canvas'


class caption(Tag):
    tag = 'caption'


class center(Tag):
    tag = 'center'


class cite(Tag):
    tag = 'cite'


class code(Tag):
    tag = 'code'


class col(Tag):
    tag = 'col'
    is_void = True


class colgroup(Tag):
    tag = 'colgroup'


class command(Tag):
    tag = 'command'


class content(Tag):
    tag = 'content'


class data(Tag):
    tag = 'data'


class datalist(Tag):
    tag = 'datalist'


class dd(Tag):
    tag = 'dd'


class _del(Tag):
    tag = '_del'


class details(Tag):
    tag = 'details'


class dfn(Tag):
    tag = 'dfn'


class dialog(Tag):
    tag = 'dialog'


class dir(Tag):
    tag = 'dir'


class div(Tag):
    tag = 'div'


class dl(Tag):
    tag = 'dl'


class dt(Tag):
    tag = 'dt'


class element(Tag):
    tag = 'element'


class em(Tag):
    tag = 'em'


class embed(Tag):
    tag = 'embed'
    is_void = True


class fieldset(Tag):
    tag = 'fieldset'


class figcaption(Tag):
    tag = 'figcaption'


class figure(Tag):
    tag = 'figure'


class font(Tag):
    tag = 'font'


class footer(Tag):
    tag = 'footer'


class form(Tag):
    tag = 'form'


class frame(Tag):
    tag = 'frame'


class frameset(Tag):
    tag = 'frameset'


class h1(Tag):
    tag = 'h1'


class h2(Tag):
    tag = 'h2'


class h3(Tag):
    tag = 'h3'


class h4(Tag):
    tag = 'h4'


class h5(Tag):
    tag = 'h5'


class h6(Tag):
    tag = 'h6'


class head(Tag):
    tag = 'head'


class header(Tag):
    tag = 'header'


class hgroup(Tag):
    tag = 'hgroup'


class hr(Tag):
    tag = 'hr'
    is_void = True


class html(Tag):
    tag = 'html'


class i(Tag):
    tag = 'i'


class iframe(Tag):
    tag = 'iframe'


class image(Tag):
    tag = 'image'


class img(Tag):
    tag = 'img'
    is_void = True


class input(Tag):
    tag = 'input'
    is_void = True


class ins(Tag):
    tag = 'ins'


class isindex(Tag):
    tag = 'isindex'


class kbd(Tag):
    tag = 'kbd'


class keygen(Tag):
    tag = 'keygen'
    is_void = True


class label(Tag):
    tag = 'label'


class legend(Tag):
    tag = 'legend'


class li(Tag):
    tag = 'li'


class link(Tag):
    tag = 'link'
    is_void = True


class listing(Tag):
    tag = 'listing'


class main(Tag):
    tag = 'main'


class map(Tag):
    tag = 'map'


class mark(Tag):
    tag = 'mark'


class marquee(Tag):
    tag = 'marquee'


class menu(Tag):
    tag = 'menu'


class menuitem(Tag):
    tag = 'menuitem'


class meta(Tag):
    tag = 'meta'
    is_void = True


class meter(Tag):
    tag = 'meter'


class multicol(Tag):
    tag = 'multicol'


class nav(Tag):
    tag = 'nav'


class nobr(Tag):
    tag = 'nobr'


class noembed(Tag):
    tag = 'noembed'


class noframes(Tag):
    tag = 'noframes'


class noscript(Tag):
    tag = 'noscript'


class object(Tag):
    tag = 'object'


class ol(Tag):
    tag = 'ol'


class optgroup(Tag):
    tag = 'optgroup'


class option(Tag):
    tag = 'option'


class output(Tag):
    tag = 'output'


class p(Tag):
    tag = 'p'


class param(Tag):
    tag = 'param'
    is_void = True


class picture(Tag):
    tag = 'picture'


class plaintext(Tag):
    tag = 'plaintext'


class pre(Tag):
    tag = 'pre'


class progress(Tag):
    tag = 'progress'


class q(Tag):
    tag = 'q'


class rp(Tag):
    tag = 'rp'


class rt(Tag):
    tag = 'rt'


class rtc(Tag):
    tag = 'rtc'


class ruby(Tag):
    tag = 'ruby'


class s(Tag):
    tag = 's'


class samp(Tag):
    tag = 'samp'


class script(Tag):
    tag = 'script'
    is_raw_text = True


class section(Tag):
    tag = 'section'


class select(Tag):
    tag = 'select'


class shadow(Tag):
    tag = 'shadow'


class slot(Tag):
    tag = 'slot'


class small(Tag):
    tag = 'small'


class source(Tag):
    tag = 'source'
    is_void = True


class spacer(Tag):
    tag = 'spacer'


class span(Tag):
    tag = 'span'


class strike(Tag):
    tag = 'strike'


class strong(Tag):
    tag = 'strong'


class style(Tag):
    tag = 'style'
    is_raw_text = True


class sub(Tag):
    tag = 'sub'


class summary(Tag):
    tag = 'summary'


class sup(Tag):
    tag = 'sup'


class table(Tag):
    tag = 'table'


class tbody(Tag):
    tag = 'tbody'


class td(Tag):
    tag = 'td'


class template(Tag):
    tag = 'template'


class textarea(Tag):
    tag = 'textarea'


class tfoot(Tag):
    tag = 'tfoot'


class th(Tag):
    tag = 'th'


class thead(Tag):
    tag = 'thead'


class time(Tag):
    tag = 'time'


class title(Tag):
    tag = 'title'


class tr(Tag):
    tag = 'tr'


class track(Tag):
    tag = 'track'
    is_void = True


class tt(Tag):
    tag = 'tt'


class u(Tag):
    tag = 'u'


class ul(Tag):
    tag = 'ul'


class var(Tag):
    tag = 'var'


class video(Tag):
    tag = 'video'


class wbr(Tag):
    tag = 'wbr'
    is_void = True


class xmp(Tag):
    tag = 'xmp'
