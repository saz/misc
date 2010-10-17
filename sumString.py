#!/usr/bin/python

s = '123x456x789'

c = 0
t = 0
while c < len(s):
  if s[c] == 'x':
    s = s.replace('x', '', 1)
    c -= 2
  else:
    t += int(s[c])
    c += 1

print t
