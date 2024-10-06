from xml.dom.minidom import Document


def tag(
    tag_name: str,
    tag_content: str | list | None = None,
    *args: list[str],
    **kwargs: dict[str, str],
) -> str:
    """Generate an HTML/SVG element with specific tag and attributes.

    Args:
        tag_name (str): The element tag name
        tag_content (str | list | None, optional): The content of the element. Can be a string, a list of strings, or None.
            If None, returns an element without a closing tag. Defaults to None.
        *args (str): Names of value-less attributes (e.g., 'defer', 'selected').
            Also useful for UnoCSS attributify mode.
        **kwargs (str): Key-value pairs of HTML attributes.
            - If value is a string, assigns `key="value"`.
            - If key ends with underscore (e.g., 'class_', 'for_'), the underscore is removed.
            - If value is an empty string, assigns a value-less attribute (e.g., 'defer', 'selected').
            - Underscores in keys are replaced with hyphens.

    Returns:
        str: An HTML/SVG element string with the specified tag and attributes.

    Examples:
        >>> tag('div')
        '<div />'

        >>> tag('div', 'Hello', id='greeting', class_='text-bold')
        '<div id="greeting" class="text-bold">Hello</div>'

        >>> tag('input', type='text', required='')
        '<input type="text" required />'

        >>> tag('ul', [tag('li', 'Item 1'), tag('li', 'Item 2')])
        '<ul><li>Item 1</li><li>Item 2</li></ul>'

        >>> tag('button', 'Click me', 'disabled', class_='btn')
        '<button disabled class="btn">Click me</button>'

        >>> tag('div', 'Content', 'data-custom', id='example', aria_hidden='true')
        '<div data-custom id="example" aria-hidden="true">Content</div>'
    """

    unique_args = sorted(map(str, set(args))) if args else []

    tag_attrs = " ".join([tag_name, *unique_args, *normalize(kwargs)])

    if tag_content is None:
        return f"<{tag_attrs} />"

    return f"<{tag_attrs}>{parse_content(tag_content)}</{tag_name}>"


def normalize(kwargs: dict[str, str]) -> list[str]:
    """normalize kwargs to list of strings"""
    if not kwargs:
        return []

    output = []
    for key, val in kwargs.items():
        if val is None:
            continue

        if key in ("class_", "for_"):
            key = key.removesuffix("_")

        key = key.replace("_", "-")

        if val == "":
            output.append(key)
            continue

        output.append(f'{key}="{val}"')

    return output


def parse_content(item: str | list) -> str:
    """recursively parse content"""
    if isinstance(item, list):
        return "".join(parse_content(subitem) for subitem in item)
    return str(item)


def comment(comment: str) -> str:
    """comment element

    Examples:
        >>> comment("hello")
        '<!--hello-->'
    """
    return Document().createComment(comment).toxml()


def doctype(kind: str = "html") -> str:
    """DOCTYPE element

    Examples:
        >>> doctype()
        '<!DOCTYPE html>'
    """
    return f"<!DOCTYPE {kind}>"
