import sys
sys.path.insert(0, '../core')

from collections import Queue

q = Queue(1, 2, 3, 4, 5)
q.print()
print('===============')

print(q.remove().val)
print(q.remove().val)
print(q.remove().val)
print(q.remove().val)
print(q.remove().val)
