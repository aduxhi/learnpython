# -*- coding: UTF-8 -*-

import re
s = '1102231990xxxxxxxx'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{3})', s)

print(res.groupdict())