from node import *

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print "graph before increment"
root.show()

# do this increment remotely:
increment(root)

print "graph after increment"
root.show()

