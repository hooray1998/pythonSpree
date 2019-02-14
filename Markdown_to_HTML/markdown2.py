# -*- coding:utf-8 -*-
import markdown2
import codecs
import sys


def main(argv):
    md_name = argv[0]

    with codecs.open(md_name, mode='r', encoding='utf-8') as mdfile:
        with codecs.open("friendly.css", mode='r', encoding='utf-8') as cssfile:
            md_text = mdfile.read()
            css_text = cssfile.read()

            extras = ['code-friendly', 'fenced-code-blocks', 'footnotes']
            html_text = markdown2.markdown(md_text, extras=extras)

            html_name = '%s.html' % (md_name[:-3])
            with codecs.open(html_name, 'w', encoding='utf-8', errors='xmlcharrefreplace') as output_file:
                output_file.write(css_text + html_text)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1:])
    else:
        print("Error:please specify markdown file path")
