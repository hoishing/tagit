"""
Modules exported by this package:

- `main`: element generation methods.
- `elements`: pre generated common tagged elements, eg. a, em, br, div, img, span ... etc
- `gen_elements`: generate `elements.py`
"""

from tagit.main import tag, comment, doctype
from tagit.elements import *
from tagit.gen_elements import Element

del element
