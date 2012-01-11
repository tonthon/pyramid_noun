# -*- coding: utf-8 -*-
# * File Name : __init__.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 11-01-2012
# * Last Modified : mer. 11 janv. 2012 22:20:05 CET
#
# * Project :
#

from pyramid.scaffolds import PyramidTemplate

class MajertiExtensionTemplate(PyramidTemplate):
    _template_dir = 'noun'
    summary = "Majerti's pyramid scaffold"
