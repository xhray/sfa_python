# -*- coding = utf-8 -*-

'iis log parser'

__author__ = 'Ray.Tan'

from datetime import datetime, timedelta
import re

__logPattern = '(?P<date>[-0-9]+ [:0-9]+) (?P<ip>[.:0-9a-fA-F]+) (?P<method>\S+) (?P<url>\S+) - (?P<port>\d+) (?P<user>\S+) (?P<request_ip>[.:0-9a-fA-F]+) (?P<user_agent>\S+) (?P<response_status>\d+) (?P<sub_status>\d+) (?P<win32_status>\d+) (?P<time_taken>\d+)'
__search = re.compile(__logPattern).search

class IISLog:
    def __init__(self, date, method, url, ip, port, request_ip, user_agent, response_status, time_taken, user):
        self.date = (datetime.strptime(date, '%Y-%m-%d %H:%M:%S') + timedelta(hours = 8))
        self.method = method
        self.url = url
        self.ip = ip
        self.port = int(port)
        self.requestIP = request_ip
        self.userAgent = user_agent
        self.responseStatus = int(response_status)
        self.timeTaken = int(time_taken) / 1000.0
        self.user = user

def __object2dict(o):
    d = {}
    if o:
        d.update(o.__dict__)
        
    return d

def parse(t):
    if t:
        p = __search(t)

        if p:
            e = IISLog(p.group('date'), p.group('method'), p.group('url'), p.group('ip'), p.group('port'), p.group('request_ip'), p.group('user_agent'), p.group('response_status'), p.group('time_taken'), p.group('user'))
            return __object2dict(e)

    return None