#! /usr/bin/env python3

from pygments import highlight
from pygments.lexers import Python3Lexer
from pygments.formatters import HtmlFormatter
from style import GruvboxStyle


def convert_text_to_html(text):
    """ Converts text to preprocessed html file"""
    temp = open(text, 'r').read()
    syntax_hg = highlight(temp, Python3Lexer(), HtmlFormatter(style="gruvbox-dark"))

    html = []
    for idx, line in enumerate(syntax_hg.split('\n')):
        if line == '':
            html.append(f"<p class=\"empty\" id={idx} style=\"\">&nbsp;</p>")
        else:
            # use <pre> to preserve tabs and leading whitespaces
            spaces = len(line) - len(line.lstrip())
            new_line = spaces * '&nbsp;' + line.lstrip()
            html.append(f"<p class=\"oneline\" id={idx} style=\"margin:0px;\">{new_line}</p>")

    html = ''.join(html)
    return html 

