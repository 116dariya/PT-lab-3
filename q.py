import re
e = re.compile("^\w+\.?\w+@((gmail\.com)|(mail\.ru)|(yandex\.ru)|(icloud\.com))$")
n = re.compile("^(8|+7)((700)|(70\d)|(747)|(750)|(751)|(76\d[0-4])|(771)|(775)|(776)|(777)|(778))\d{7}$")

c = re.compile("^(8|+7)7((1[0-8])|(2[1-9])|(36))\d{7}$")
m = re.compile("^\A[A-Z]\d\d\d((\A{2})|(\A{3}))$")
v = re.compile("^\d\d\d((\A{2})|(\A{3}))((0\d[1-9])|(1\d[0-6]))$")
i = re.compile("^\d\d((0\d[1-9])|(1\d[0-2]))((0\d[1-9])|(1\d[0-9])|(2\d[0-9])|(30|31))[1-6]$")

print(c.match('87171234567'))
