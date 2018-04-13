# -*- coding: utf-8 -*-
"""
    flask.ext.babel._compat
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Armin Ronacher, Daniel Neuhäuser.
    :license: BSD, see LICENSE for more details.
"""
import sys


PY2 = sys.version_info[0] == 2


if PY2:
    def text_type(v):
        try:
            return unicode(v)
        except Exception:
            return unicode(v, "utf-8", errors="ignore")
    string_types = (str, unicode)

else:
    text_type = str
    string_types = (str, )
