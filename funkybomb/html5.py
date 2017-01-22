from funkybomb.node import Tag


class HtmlTag(Tag):

    def __init__(self, *nodes, **attrs):
        super().__init__()
        self.append(*nodes)
        self.attrs = attrs


class a(HtmlTag):
    tag = 'a'


class abbr(HtmlTag):
    tag = 'abbr'


class acronym(HtmlTag):
    tag = 'acronym'


class address(HtmlTag):
    tag = 'address'


class applet(HtmlTag):
    tag = 'applet'


class area(HtmlTag):
    tag = 'area'
    is_void = True


class article(HtmlTag):
    tag = 'article'


class aside(HtmlTag):
    tag = 'aside'


class audio(HtmlTag):
    tag = 'audio'


class b(HtmlTag):
    tag = 'b'


class base(HtmlTag):
    tag = 'base'
    is_void = True


class basefont(HtmlTag):
    tag = 'basefont'


class bdi(HtmlTag):
    tag = 'bdi'


class bdo(HtmlTag):
    tag = 'bdo'


class bgsound(HtmlTag):
    tag = 'bgsound'


class big(HtmlTag):
    tag = 'big'


class blink(HtmlTag):
    tag = 'blink'


class blockquote(HtmlTag):
    tag = 'blockquote'


class body(HtmlTag):
    tag = 'body'


class br(HtmlTag):
    tag = 'br'
    is_void = True


class button(HtmlTag):
    tag = 'button'


class canvas(HtmlTag):
    tag = 'canvas'


class caption(HtmlTag):
    tag = 'caption'


class center(HtmlTag):
    tag = 'center'


class cite(HtmlTag):
    tag = 'cite'


class code(HtmlTag):
    tag = 'code'


class col(HtmlTag):
    tag = 'col'
    is_void = True


class colgroup(HtmlTag):
    tag = 'colgroup'


class command(HtmlTag):
    tag = 'command'


class content(HtmlTag):
    tag = 'content'


class data(HtmlTag):
    tag = 'data'


class datalist(HtmlTag):
    tag = 'datalist'


class dd(HtmlTag):
    tag = 'dd'


class _del(HtmlTag):
    tag = '_del'


class details(HtmlTag):
    tag = 'details'


class dfn(HtmlTag):
    tag = 'dfn'


class dialog(HtmlTag):
    tag = 'dialog'


class dir(HtmlTag):
    tag = 'dir'


class div(HtmlTag):
    tag = 'div'


class dl(HtmlTag):
    tag = 'dl'


class dt(HtmlTag):
    tag = 'dt'


class element(HtmlTag):
    tag = 'element'


class em(HtmlTag):
    tag = 'em'


class embed(HtmlTag):
    tag = 'embed'
    is_void = True


class fieldset(HtmlTag):
    tag = 'fieldset'


class figcaption(HtmlTag):
    tag = 'figcaption'


class figure(HtmlTag):
    tag = 'figure'


class font(HtmlTag):
    tag = 'font'


class footer(HtmlTag):
    tag = 'footer'


class form(HtmlTag):
    tag = 'form'


class frame(HtmlTag):
    tag = 'frame'


class frameset(HtmlTag):
    tag = 'frameset'


class h1(HtmlTag):
    tag = 'h1'


class h2(HtmlTag):
    tag = 'h2'


class h3(HtmlTag):
    tag = 'h3'


class h4(HtmlTag):
    tag = 'h4'


class h5(HtmlTag):
    tag = 'h5'


class h6(HtmlTag):
    tag = 'h6'


class head(HtmlTag):
    tag = 'head'


class header(HtmlTag):
    tag = 'header'


class hgroup(HtmlTag):
    tag = 'hgroup'


class hr(HtmlTag):
    tag = 'hr'
    is_void = True


class html(HtmlTag):
    tag = 'html'


class i(HtmlTag):
    tag = 'i'


class iframe(HtmlTag):
    tag = 'iframe'


class image(HtmlTag):
    tag = 'image'


class img(HtmlTag):
    tag = 'img'
    is_void = True


class input(HtmlTag):
    tag = 'input'
    is_void = True


class ins(HtmlTag):
    tag = 'ins'


class isindex(HtmlTag):
    tag = 'isindex'


class kbd(HtmlTag):
    tag = 'kbd'


class keygen(HtmlTag):
    tag = 'keygen'
    is_void = True


class label(HtmlTag):
    tag = 'label'


class legend(HtmlTag):
    tag = 'legend'


class li(HtmlTag):
    tag = 'li'


class link(HtmlTag):
    tag = 'link'
    is_void = True


class listing(HtmlTag):
    tag = 'listing'


class main(HtmlTag):
    tag = 'main'


class map(HtmlTag):
    tag = 'map'


class mark(HtmlTag):
    tag = 'mark'


class marquee(HtmlTag):
    tag = 'marquee'


class menu(HtmlTag):
    tag = 'menu'


class menuitem(HtmlTag):
    tag = 'menuitem'


class meta(HtmlTag):
    tag = 'meta'
    is_void = True


class meter(HtmlTag):
    tag = 'meter'


class multicol(HtmlTag):
    tag = 'multicol'


class nav(HtmlTag):
    tag = 'nav'


class nobr(HtmlTag):
    tag = 'nobr'


class noembed(HtmlTag):
    tag = 'noembed'


class noframes(HtmlTag):
    tag = 'noframes'


class noscript(HtmlTag):
    tag = 'noscript'


class object(HtmlTag):
    tag = 'object'


class ol(HtmlTag):
    tag = 'ol'


class optgroup(HtmlTag):
    tag = 'optgroup'


class option(HtmlTag):
    tag = 'option'


class output(HtmlTag):
    tag = 'output'


class p(HtmlTag):
    tag = 'p'


class param(HtmlTag):
    tag = 'param'
    is_void = True


class picture(HtmlTag):
    tag = 'picture'


class plaintext(HtmlTag):
    tag = 'plaintext'


class pre(HtmlTag):
    tag = 'pre'


class progress(HtmlTag):
    tag = 'progress'


class q(HtmlTag):
    tag = 'q'


class rp(HtmlTag):
    tag = 'rp'


class rt(HtmlTag):
    tag = 'rt'


class rtc(HtmlTag):
    tag = 'rtc'


class ruby(HtmlTag):
    tag = 'ruby'


class s(HtmlTag):
    tag = 's'


class samp(HtmlTag):
    tag = 'samp'


class script(HtmlTag):
    tag = 'script'
    is_raw_text = True


class section(HtmlTag):
    tag = 'section'


class select(HtmlTag):
    tag = 'select'


class shadow(HtmlTag):
    tag = 'shadow'


class slot(HtmlTag):
    tag = 'slot'


class small(HtmlTag):
    tag = 'small'


class source(HtmlTag):
    tag = 'source'
    is_void = True


class spacer(HtmlTag):
    tag = 'spacer'


class span(HtmlTag):
    tag = 'span'


class strike(HtmlTag):
    tag = 'strike'


class strong(HtmlTag):
    tag = 'strong'


class style(HtmlTag):
    tag = 'style'
    is_raw_text = True


class sub(HtmlTag):
    tag = 'sub'


class summary(HtmlTag):
    tag = 'summary'


class sup(HtmlTag):
    tag = 'sup'


class table(HtmlTag):
    tag = 'table'


class tbody(HtmlTag):
    tag = 'tbody'


class td(HtmlTag):
    tag = 'td'


class template(HtmlTag):
    tag = 'template'


class textarea(HtmlTag):
    tag = 'textarea'


class tfoot(HtmlTag):
    tag = 'tfoot'


class th(HtmlTag):
    tag = 'th'


class thead(HtmlTag):
    tag = 'thead'


class time(HtmlTag):
    tag = 'time'


class title(HtmlTag):
    tag = 'title'


class tr(HtmlTag):
    tag = 'tr'


class track(HtmlTag):
    tag = 'track'
    is_void = True


class tt(HtmlTag):
    tag = 'tt'


class u(HtmlTag):
    tag = 'u'


class ul(HtmlTag):
    tag = 'ul'


class var(HtmlTag):
    tag = 'var'


class video(HtmlTag):
    tag = 'video'


class wbr(HtmlTag):
    tag = 'wbr'
    is_void = True


class xmp(HtmlTag):
    tag = 'xmp'
