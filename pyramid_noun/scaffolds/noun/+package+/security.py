# -*- coding: utf-8 -*-
# * File Name : security.py
#
# * Copyright (C) 2010 Gaston TJEBBES <g.t@majerti.fr>
# * Company : Majerti ( http://www.majerti.fr )
#
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 02-03-2012
# * Last Modified :
#
# * Project : {{package}}
#
import logging

from pyramid.security import Allow
from pyramid.security import Everyone
from pyramid.security import Authenticated

log = logging.getLogger(__name__)

class RootFactory(object):
    """
         See the url dispatch description to understand what I'm supposed to do
    """
    __acl__ = [(Allow, Authenticated, 'view'),
                 ]
    def __init__(self, request):
        self.request = request
