# from rollyourown import seo
# from collections import OrderedDict as SortedDict

"""
http://django-seo.readthedocs.io/en/latest/reference/administrators.html
"""


class MyMetadata(seo.Metadata):
    title       = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords    = seo.KeywordTag()
    heading     = seo.Tag(name="h1")
