from contextlib import contextmanager


class HTML:
    def __init__(self):
        self.result = ''
        self.opened = []

    def __del__(self):
        pass

    @staticmethod
    def get_opening_tag(tag: str):
        return f'<{tag}>'

    @staticmethod
    def get_closing_tag(tag: str):
        return f'</{tag}>'

    def add_to_result(self, *tags):
        self.result += ''.join(tags)

    def indent(self):
        return ' ' * len(self.opened)

    @contextmanager
    def body(self):
        self.add_to_result(self.get_opening_tag('body'), '\n')
        yield
        self.add_to_result(self.get_closing_tag('body'), '\n')

    @contextmanager
    def div(self):
        self.add_to_result(f'{self.indent()}{self.get_opening_tag("div")}\n')
        self.opened.append('div')
        yield
        self.opened.remove('div')
        self.add_to_result(f'{self.indent()}{self.get_closing_tag("div")}\n')

    def p(self, line: str):
        self.add_to_result(f'{self.indent()}{self.get_opening_tag("p")}{line}{self.get_closing_tag("p")}\n')

    def __enter__(self):
        return self

    def __exit__(self):
        pass


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.result)


