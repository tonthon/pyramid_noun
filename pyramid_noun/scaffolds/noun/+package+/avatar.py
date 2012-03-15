# -*- coding: utf-8 -*-
# * File Name : avatar.py
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

log = logging.getLogger(__name__)

def build_avatar(login, request):
    """
        Stores the avatar object in the session
    """
    log.debug("# Building avatar")
    from {{package}}.models import DBSESSION
    from {{package}}.models.model import User
    avatar = DBSESSION.query(Account).filter_by(account_lid=login).first()
    request.session['user'] = avatar
    if avatar:
        return []
