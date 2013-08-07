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

from zope.interface import implements

from Products.Zuul.infos.component import ComponentInfo
from Products.ZenUtils.Utils import convToUnits

from ZenPacks.CERIT_SC.Torque.interfaces import *

class TorqueNodeInfo(ComponentInfo):
    implements(ITorqueNodeInfo)

    @property
    def monitored(self):
        return False

    @property
    def status(self):
        if not hasattr(self._object, 'statusString'): return 'Unknown'
        else: return self._object.statusString()

    @property
    def np(self):
        return self._object.np

    @property
    def priority(self):
        return self._object.priority

    @property
    def note(self):
        return self._object.note

    @property
    def queue(self):
        return self._object.queue

    @property
    def properties(self):
        return self._object.properties

    @property
    def operStatus(self):
        if self.status not in ('Unknown','Offline','Down','Frozen'):
            return 'Up'
        else:
            return 'Down'

