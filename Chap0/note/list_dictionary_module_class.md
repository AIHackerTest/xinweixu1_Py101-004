### What's a **list**?
A list is a type of data structure in the form of an ordered list of things that you want to store and access randomly or linearly by an index.



#### what are the things that you can do to a list?
* List can be processed by functions, for example:
`list.pop([i])` - it removes the element at the given position i in the list and return it; if no index is specified, the default is the last item in the list.         
* More methods on lists - see documentation [here](https://docs.python.org/2.7/tutorial/datastructures.html?highlight=list)

### What's a **dictionary**?
A dictionary is a way to store data just like a list, but the main distinction is that - instead of using numbers as an index to access things in a list, you can use almost anything as **keys** to access things(called **"values"**) in a dictionary. However, a big difference is that items in a dictionary **do not** have an order as that in a list.     
Nonetheless, an ordered dictionary can be compiled through `OrderedDict([items])`, and an ordered dictionary remembers its insertion order. More info see documentation [here](https://docs.python.org/2/library/collections.html#ordereddict-objects).

#### what are the things that you can do to a dictionary?
* When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method. For example:
`for state, abbrev in states.items()`.
* You can access a particular value of an item in a dictionary by the get() method. For example: `states.get('Texas')`, where "Texas" should be a key in the dictionary "states".


### What's a **module**?
Like a dictionary, a module is also a mapping of some items(e.g., keys) to other items (e.g., values). The main differences are 1) a module is a python file with some functions or variables and you need to import a module before using it; 2) instead of accessing items in a dictionary using a syntax like `dict['key']`, you access things in a module with the `.` (dot) operator, for example: `mystuff.apple()` means calling the item "apple" from the module "mystuff".  
See documentation for modules [here](https://docs.python.org/3/tutorial/modules.html).


### What's a **class**?
A class is a way to take a grouping of functions and data and place them inside a container so that you can access them with the `.`(dot) operator (similar to accessing a module).     
When a class gets "instantiated"(i.e., created), you get an **object**.
#### Phrase Drills:
 * `class X(Y)`: make a class named X that is-a Y (i.e., as an inheritance of Y)
 * `class X(object): def__init__(self, J)`: class X has-a \_\_init\_\_ that takes self and J parameters
 * `class X(object): def M(self, J)`: class X has-a function named M that takes self and J parameters
 * `foo=X()`: set foo to be an instance of class X
 * `foo.M(J)`: from foo, get function M and call it with paramters self, J
 * `foo.K=Q`: from foo, get the K attribute, and set it to  Q
