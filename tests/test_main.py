from tagit import tag, div, ul, li, prettify, comment, doctype, input_, label
from textwrap import dedent


def test_tag():
    assert tag("div") == "<div />"
    assert tag("a", "b") == "<a>b</a>"


def test_none_content():
    assert tag("a") == "<a />"
    assert tag("a", None) == "<a />"
    assert div() == "<div />"
    assert div(None) == "<div />"


def test_empty_string_content():
    assert tag("a", "") == "<a></a>"
    assert div("") == "<div></div>"


def test_boolean_attr():
    assert tag("a", "b", "c") == "<a c>b</a>"
    assert tag("a", "b", "c", yo="", id="e") == '<a c yo id="e">b</a>'


def test_underscore_attr():
    assert tag("a", "b", class_="c") == '<a class="c">b</a>'
    assert tag("a", del_="c", hi_="hi", map_a="") == '<a del-="c" hi-="hi" map-a />'
    assert (
        label("May", for_="d")
        + input_(None, "checked", type="radio", name="username", id="d")
        == '<label for="d">May</label><input checked type="radio" name="username" id="d" />'
    )


def test_nested_content():
    assert tag("a", ["b", "c"]) == "<a>bc</a>"
    assert tag("a", ["b", tag("i", "c")]) == "<a>b<i>c</i></a>"
    assert (
        div(["hello", ul([li("yo"), li("yo", id="main")])])
        == '<div>hello<ul><li>yo</li><li id="main">yo</li></ul></div>'
    )


def test_prettify():
    output = dedent(
        """\
        <ul>
            <li>yo</li>
            <li id="main">yo</li>
        </ul>
        """
    )
    assert prettify(ul([li("yo"), li("yo", id="main")])) == output


def test_comment():
    assert comment("hello") == "<!--hello-->"


def test_doctype():
    assert doctype() == "<!DOCTYPE html>"
