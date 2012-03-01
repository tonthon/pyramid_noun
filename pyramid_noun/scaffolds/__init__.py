# -*- coding: utf-8 -*-
# * File Name : __init__.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 11-01-2012
# * Last Modified : jeu. 01 mars 2012 15:58:50 CET
#
# * Project :
#

from pyramid.scaffolds import PyramidTemplate

class NounExtensionTemplate(PyramidTemplate):
    _template_dir = 'noun'
    summary = "Majerti's pyramid scaffold"
