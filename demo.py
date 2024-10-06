# standard elements
from tagit import html, div, img, body, head, title, script, select, option

# for creating custom element
from tagit import tag

# special elements
from tagit import doctype, comment


html_str = (
    doctype()
    + comment("this is a demo showing how to use `tagit`")
    + html(
        # use list to enclose multiple elements
        [
            head(
                [
                    title("testing html template"),
                    script(
                        "",  # empty string content ensures closing tag
                        "defer",  # positional argument will be converted to value-less(boolean) attribute
                        src="https://cdn.jsdelivr.net/npm/@unocss/runtime/attributify.global.js",
                    ),
                ]
            ),
            body(
                [
                    # if you don't provide content, element without closing tag will be created
                    img(src="https://picsum.photos/200/300"),
                    # class_ attribute will convert to `class`
                    div("pls select the direction:", class_="text-xl"),
                    select(
                        [
                            # attr with None will be ommitted,
                            # and empty string will be converted to boolean attribute
                            option(d, selected=("" if d == "S" else None))
                            for d in "ESWN"
                        ],
                        # underscore will convert to hyphen, eg. `data-type`
                        data_type="direction",
                    ),
                    # create custom element
                    tag("MyElement", props="some-props"),
                ],
            ),
        ]
    )
)

with open("demo.html", "w") as f:
    f.write(html_str)
