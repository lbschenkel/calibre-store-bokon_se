# -*- coding: utf-8 -*-
from __future__ import (absolute_import, print_function, unicode_literals)

__license__   = 'GPL 3'
__copyright__ = '2017, Leonardo Brondani Schenkel <leonardo@schenkel.net>'
__docformat__ = 'restructuredtext en'

from calibre.customize import StoreBase

class BokonStore(StoreBase):
    name            = 'Bokon.se'
    version         = (0,1,0)
    description     = 'Köp e-böcker i Sveriges e-bokhandel'
    author          = 'Leonardo Brondani Schenkel <leonardo@schenkel.net>'
    actual_plugin   = 'calibre_plugins.lbschenkel_store_bokon_se.bokon:BokonStorePlugin'
    headquarters    = 'SE'
    formats         = ['EPUB', 'PDF']

