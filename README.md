# tagit

[![ci-badge]][ci-url] [![pypi-badge]][pypi-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> HTML/SVG tag generator for minimalist

## Key Features

- all elements output are pure string, simple and easy to manipulate
- no classes or objects, only functions
- all standard html and svg elements are included
- create nested child elements with list of strings and elements
- able to create custom elements
- create value-less(boolean) attributes with positional argument
    - handy for using with [UnoCSS] attributify mode
- pure python, no external dependencies
- high test coverage

## Quick Start

- installation: `pip install tagit`
- basic signature
    - `element(tag_content: str | list | None = None, *args, **kwargs) -> str`

```python
# common elements
from tagit import div, img, p, ul, li, label, input_,

# empty tag
print(div())
# <div />

# None content is ignored
print(div(None))
# <div />

# empty string content creates closing tag
print(div(""))
# <div></div>

# tag as content
print(div(img(src="url"), id="bar"))  
# <div id="bar"><img src="url"/></div>

# content mix with strings and tags
print(div(["foo", img(src="url"), "bar")])
# <div>foo<img src="url"/>bar</div>
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
print(label("foo", for_="bar"))
# <label for="bar">foo</label>

print(input_(None, class_="foo", name="bar", type="checkbox", value="baz"))
# <input name="bar" type="checkbox" value="baz"/>
```

- position args -> value-less attribute.
    - boolean attribute: eg. `checked`, `disabled`, `selected`
    - assign tailwind classes with [UnoCSS] attributify mode

```python
print(div("foo", "clear-both", "m-2", "rounded", id="baz"))
# <div clear-both m-2 rounded id="baz">foo</div>
```

- keyword argument with value None is ignored

```python
tag = div(None, "m-2", "rounded", id="baz", style=None) 
print(tag)  
# <div m-2 rounded id="baz" />
```

- create custom element
- signature:
    - `tag(tag_name: str, tag_content: str | list | None = None, *args, **kwargs) -> str`

```python
from tagit import tag

tag('div')
# <div />'

tag('div', 'Hello', id='greeting', class_='text-bold')
# <div id="greeting" class="text-bold">Hello</div>

tag('input', type='text', required='')
# <input type="text" required="" />'

tag('ul', [tag('li', 'Item 1'), tag('li', 'Item 2')])
# <ul><li>Item 1</li><li>Item 2</li></ul>

tag('button', 'Click me', 'disabled', class_='btn')
# <button disabled class="btn">Click me</button>

tag('div', 'Content', 'data-custom', id='example', aria_hidden='true')
# <div data-custom id="example" aria-hidden="true">Content</div>

tag("MyElement", tag_content="foo", props="bar")
# <MyElement props="bar">foo</MyElement>
```

- see [demo.py] for a full demo
- more examples could be found in [tests] package

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

- [github issue]
- [x.com posts]
- [contact the author]

[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[ci-badge]: https://github.com/hoishing/tagit/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/hoishing/tagit/actions/workflows/ci.yml
[contact the author]: https://hoishing.github.io
[demo.py]: https://github.com/hoishing/tagit/blob/main/demo.py
[github issue]: https://github.com/hoishing/tagit/issues
[MIT-badge]: https://img.shields.io/github/license/hoishing/tagit
[MIT-url]: https://opensource.org/licenses/MIT
[pypi-badge]: https://img.shields.io/pypi/v/tagit
[pypi-url]: https://pypi.org/project/tagit/
[tests]: https://github.com/hoishing/tagit/blob/main/tests/test_main.py
[UnoCSS]: https://github.com/unocss/unocss
[x.com posts]: https://x.com/hoishing
