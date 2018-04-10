This directory includes 

* `node.py`: which
  * defines a node class. 
    * contains a name, list of children, and a count that's initially zero
    * implements a `show(graph)` method recursively prints the nodes within graph  
  * An `increment(graph)` method that increments the counts of all nodes within graph. 
* `localDemo.py`: which creates a dag of nodes, which it prints, increments, and prints again.

Your tasks are
* to create 
  * a jsonrpc server that exports the `increment(graph)` function
  * a client that demonstrates the effect of `increment()` being remotely executed on the graph from localDemo.py.
  * a file named `request.json` containing a the manually genrated contents of jsonrpc request to `increment()`
   equivalent to the one produced by your client.   You should use nc to confirm that it's correct.
