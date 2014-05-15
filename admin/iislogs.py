# -*- coding: utf-8 -*-

'import iis logs into mongodb'

__author__ = 'Ray.Tan'

import os
import sys

os.chdir(sys.path[0])
sys.path.append('..')

import os
import pymongo
import re
from datetime import datetime
import utils.logParser as logParser
from bson.code import Code

def __import(filepath):
    if os.path.isfile(filepath):
        connection = pymongo.Connection(host = 'localhost', port = 27017)
        db = connection.test

        with open(filepath, 'r') as file:
            for line in file:
                e = logParser.parse(line)

                if e:
                    print e
                    db.iis_logs.insert(e)

def import_logs(filepath, all=False):
    if not all:
        __import(filepath)
    else:
        datePattern = '\d+'
        dateSearch = re.compile(datePattern).search

        for filename in os.listdir(filepath):
            x = dateSearch(filename)
            if x and x.group(0) and x.group(0) != datetime.now().strftime('%y%m%d'):
                __import(os.path.join(filepath, filename))

__mapByDate = Code("function() {"
             "  var key = {url: this.url, year: this.date.getFullYear(), month: ('0' + (this.date.getMonth() + 1)).slice(-2), day: ('0' + this.date.getDate()).slice(-2)};"
             "  emit(key, {count: 1});"
             "}")


__reduce = Code("function(key, values) {"
                "  var sum = 0;"
                "  values.forEach(function(value){"
                "    sum += value['count'];"
                "  });"
                "  return {count: sum};"
                "}"
                )

def analysis(date):
    connection = pymongo.Connection(host = 'localhost', port = 27017)
    db = connection.test

    if date:
        db.iis_logs.map_reduce(__mapByDate, __reduce, out="hit_stats", full_response=True, query={"date": {"$gte": datetime(date.year, date.month, date.day)}})
    else:
        db.iis_logs.map_reduce(__mapByDate, __reduce, out="hits_stats", full_response=True)

if __name__ == '__main__':
    analysis()


