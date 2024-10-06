# tagit

[![ci-badge]][ci-url] [![pypi-badge]][pypi-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> simple and pythonic way to write html/svg tags

## Key Features

- all elements output are pure string, simple and easy to manipulate
- only functions are exported, no classes or objects
- all html and svg elements are exported as functions
- custom element creation
- prettify elements to human readable format
- create value-less(boolean) attributes with empty string or positional argument
    - handy for using with [UnoCSS] attributify mode

## Installation

`pip install tagit`

## Quick Start

- import common html elements

```python
# all html/svg elements are available as functions
from tagit import div

div('hi', id='foo')
# <div id="foo" class="bar">hi</div>
```

- use trailing underscore to work around python keyword and built-in functions
- attributes:
    - `class_` -> `class`
    - `for_` -> `for`
- elements:
    - `del_` -> `del`
    - `input_` -> `input`
    - `map_` -> `map`
    - `object_` -> `object`

```python
from tagit import label, input_

label('username', for_='username') + input_(type="text", id="username", class_="bar")
# <label for="username">username</label><input type="text" id="username" class="bar"/>
```

- value-less(boolean) attributes. eg. `checked`, `disabled`, `selected`
- to denote value-less attribute:  
    - use empty string, eg. `checked=""`
    - use positional argument

```python
div(img(src='url'), class_='bar', checked="")
# <div class="bar" checked><img src="url"/></div>

input_(None, 'disabled', type='text')
# <input disabled type="text"/>
```

- create custom element

```python
from tagit import tag

tag('div')
# <div />'

tag('div', 'Hello', id='greeting', class_='text-bold')
# <div id="greeting" class="text-bold">Hello</div>

tag('input', type='text', required='')
# <input type="text" required />'

tag('ul', [tag('li', 'Item 1'), tag('li', 'Item 2')])
# <ul><li>Item 1</li><li>Item 2</li></ul>

tag('button', 'Click me', 'disabled', class_='btn')
# <button disabled class="btn">Click me</button>

tag('div', 'Content', 'data-custom', id='example', aria_hidden='true')
# <div data-custom id="example" aria-hidden="true">Content</div>

tag("MyElement", tag_content="foo", props="bar")
# <MyElement props="bar">foo</MyElement>
```

- prettify elements to human readable format

```python
html_str = prettify(div(img(src='url'), class_='bar'))
# <div class="bar"><img src="url"/></div>
```

- more examples available at [demo notebook] and [tests] package

## Motivation

When creating simple website, instead of separating python and template files like this:

```html
<ul id="navigation">
  {% for item in navigation %}
  <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
  {% endfor %}
</ul>
```

I prefer a pure python approach like this:

```python
ul(
    [
      li(
        a(item.caption, href=item.href)
      )
      for item in navigation
    ],
    id = "navigation"
)
```

It provides full intellisense, type checking, and all language features from the text editor, a much better DX.

## Need Help?

Open a [github issue] or ping me on [X ![x-icon]][X]

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[ci-badge]: https://github.com/hoishing/tagit/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/hoishing/tagit/actions/workflows/ci.yml
[demo notebook]: https://github.com/hoishing/tagit/blob/main/demo.ipynb
[github issue]: https://github.com/hoishing/tagit/issues
[MIT-badge]: https://img.shields.io/github/license/hoishing/tagit
[MIT-url]: https://opensource.org/licenses/MIT
[pypi-badge]: https://img.shields.io/pypi/v/tagit
[pypi-url]: https://pypi.org/project/tagit/
[tests]: https://github.com/hoishing/tagit/blob/main/tests/test_main.py
[UnoCSS]: https://github.com/unocss/unocss
[x-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[X]: https://x.com/hoishing
