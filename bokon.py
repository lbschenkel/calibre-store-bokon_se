# -*- coding: utf-8 ts=4 sw=4 sts=4 et -*-
from __future__ import (absolute_import, print_function, unicode_literals)

__license__   = 'GPL 3'
__copyright__ = '2017, Leonardo Brondani Schenkel <leonardo@schenkel.net>'
__docformat__ = 'restructuredtext en'

from six.moves import urllib

from calibre.gui2.store import StorePlugin
from calibre.gui2.store.search_result import SearchResult

if __name__ == '__main__':
    from lib import GenericStore, xpath, text
else:
    from calibre_plugins.lbschenkel_store_bokon_se.lib import GenericStore, xpath, text

class BokonStore(GenericStore):
    url                = 'https://bokon.se'
    search_url         = '{0}/search/{1}/?book_type=text'
    words_drm_locked   = ['drm']
    words_drm_unlocked = ['vattenmärkt', 'unprotected']

    def quote(self, query):
        return urllib.parse.quote(query)

    def find_search_results(self, doc):
        return xpath(doc, '//*', 'book ')

    def parse_search_result(self, node):
        r = SearchResult()
        r.detail_item = text(node, '(.//a)[1]', '', '/@href')
        r.title       = text(node, './/*', 'book__title', '/text()')
        r.author      = text(node, './/*', 'book__authorname')
        r.price       = text(node, './/*', 'book__price')
        r.cover_url   = text(node, './/*', 'book__cover', '//img/@src')
        return r

    def parse_book_details(self, node):
        r = SearchResult()
        r.title     = text(node, './/*[@itemprop="name"]')
        r.author    = text(node, './/*', 'bookdetails__authorname')
        r.price     = text(node, './/*', 'bookdetails__price_type_current bookdetails__price_value')
        r.cover_url = text(node, './/img[@itemprop="image"]', '', '/@src')
        r.formats   = text(node, './/*', 'book_info__format', '/span[2]/text()')
        r.drm       = text(node, './/*', 'book_info__drm', '/span[2]/text()')
        return r

class BokonStorePlugin(StorePlugin):
    store = BokonStore()

    def search(self, query, max_results, timeout):
        return self.store.search(query, max_results, timeout)

    def get_details(self, result, timeout):
        return self.store.get_details(result, timeout)

    def open(self, parent, item, external):
        return self.store.open(self.name, self.gui, parent, item, external)

    def create_browser(self):
        return self.store.create_browser()


if __name__ == '__main__':
    import sys
    query   = ' '.join(sys.argv[1:])
    max     = 3
    timeout = 10

    store = BokonStore()
    for r in store.search(query, max, timeout):
        store.get_details(r, timeout)
        print(r)
