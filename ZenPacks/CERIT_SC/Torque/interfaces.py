###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010 Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/#
###########################################################################

from Products.Zuul.form import schema
from Products.Zuul.infos.component import IComponentInfo

class ITorqueNodeInfo(IComponentInfo):
    """
    Info adapter for ITorqueNodeInfo components.
    """
    status = schema.Text(title=u"Status", group="Overview", readonly=True)
    operStatus = schema.Text(title=u"Operational Status", group="Overview", readonly=True)
    np = schema.Int(title=u"Processors", group="Details", readonly=True)
    priority = schema.Int(title=u"Priority", group="Details", readonly=True)
    note = schema.Text(title=u"Note", group="Details", readonly=True)
    queue = schema.Text(title=u"Queue", group="Details", readonly=True)
    properties = schema.List(title=u"Properties", group="Details", readonly=True)
