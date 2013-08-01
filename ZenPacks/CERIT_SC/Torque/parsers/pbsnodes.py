import re

from xml.dom.minidom import parseString
from Products.ZenRRD.CommandParser import CommandParser
from Products.ZenUtils.Utils import prepId as globalPrepId

class pbsnodes(CommandParser):
    componentScanValue = 'id'

    def prepId(self, id, subchar='_'):
        return globalPrepId(id, subchar)

    def dataForParser(self, context, dp):
        # This runs in the zenhub service, so it has access to the actual ZODB object
        return dict(componentScanValue = getattr(context, self.componentScanValue))

    def processResults(self, cmd, result):
        """
        Process the results of "pbsnodes -x"
        """
        ifs = {}
        for dp in cmd.points:
            dp.component = dp.data['componentScanValue']
            points = ifs.setdefault(dp.component, {})
            points[dp.id] = dp

        dom = parseString(cmd.result.output)
        for n in dom.getElementsByTagName('Node'):
            component = self.prepId(n.getElementsByTagName('name')[0].firstChild.data)
            points = ifs.get(component, None)
            if points:
                for p in n.childNodes:
                    key=p.nodeName

                    # ignore status, e.g.:
                    # set node node1.torque status = rectime=1375286252
                    # set node node1.torque status += varattr=
                    # set node node1.torque status += jobs=
                    # 
                    # and rename state to status, e.g.:
                    # set node node1.torque state = free
                    if key == 'status':
                        continue
                    elif key == 'state':
                        key = 'status'

                    dp = points.get(key, None)
                    if dp is not None:
                        try:
                            value=p.firstChild.data
                            match=re.match('^(?P<value>[\d\.]+)(?P<unit>kb|mb|gb)',value)
                            if match:
                                value = float(match.group('value'))
                                if match.group('unit') == 'kb':
                                    value *= 1024
                                elif match.group('unit') == 'mb':
                                    value *= 1048576
                                elif match.group('unit') == 'gb':
                                    value *= 1073741824
                                else:
                                    value = None
                            elif key == 'status':
                                value = value.lower()
                                if 'offline' in value:
                                    value = 3
                                elif value == 'free':
                                    value = 2
                                elif value == 'down':
                                    value = 4
                                elif value == 'reserve':
                                    value = 5
                                elif value == 'job-exclusive':
                                    value = 6
                                elif value == 'job-sharing':
                                    value = 7
                                elif value == 'busy':
                                    value = 8
                                elif value == 'frozen':
                                    value = 9
                                elif value == 'time-shared':
                                    value = 10
                                else:
                                    value = 1
                            elif value in ('-',''):
                                value = 0

                            result.values.append((dp, float(value)))
                        except:
                            pass

        print result
        return result
