# -*- coding:utf-8 -*-
import mistune
import sys
import codecs
from pygments import cnblogs_code 
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return cnblogs_code (code, lexer, formatter)

def main(argv):
    name = argv[0]

    input_file = codecs.open(name, mode='r', encoding='utf-8')

    text = input_file.read()
    renderer = HighlightRenderer()
    markdown = mistune.Markdown(renderer=renderer)
    html = markdown(text)

    html_name = '%s.html' % (name[:-3])
    output_file = codecs.open(
        html_name, 'w', encoding='utf-8', errors='xmlcharrefreplace')

    output_file.write(html)

if __name__ == "__main__":
    main(sys.argv[1:])
