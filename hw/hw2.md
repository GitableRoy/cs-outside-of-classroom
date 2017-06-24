# Homework -- Week 2

## Homework 2.0: Convenience functions (due 6/22 before the class)

If you have not done so during the class, write the following functions for
your own convenience. Use standard language practices where possible and take
appropriate shortcuts. Utilize safe, standard containers:

* C++: `std::vector`
* Java: `int[]` or `ArrayList`
* Python: lists or NumPy arrays

### Random array generator

This function should return an array of random numbers. Aside from creating a
convenient utility for testing purposes, you'll also review how random number
generation works in your language.

This function should accept three parameters:
1. `size`: number of elements to generate
2. `min`: smallest possible random value
3. `max`: largest possible random value

...and, appropriately, return the generated array.

You should also consider writing at least two versions of this function -- one
for integers and one for floating-point numbers (`double`).

The signature for the integer version of this function should be something
along the lines of:

* C++:  
```c++
std::vector<int> rand_int(unsigned int size, int min, int max)
{
    ...
}
```
* Java:  
```java
public static int[] rand_int(int size, int min, int max) {
    ...
}
```
* Python:  
```python
def rand_int(size, min, max):
    ...
```
(though you shouldn't be writing this sort of a function if you are using
Python and know what you are doing)


### Array/container printer

As the title suggests, this function should print the elements of the arrays or
containers that you work with. Do not go too crazy with it -- there are many
ways to "nicely" print an array. Keep it basic, e.g. if your array has elements
1, 2, and 3, then both `1 2 3` and `{1, 2, 3}` formats will work. If you are
using C++ and are familiar with operator overloading and templates, you can
make it even easier for yourself by creating a templated overload of the
`operator<<` for `std::vector`. That being said, the simplest way to go is to
just make a function `print` that returns nothing and accepts the container as
the only argument.

Once again, here's what the signature for the integer version of this function
should look like:

* C++:  
```c++
void print(const std::vector<int>& vec)
{
    ...
}
```
* Java:  
```java
public static void print(int[] arr) {
    ...
}
```
* Python: seriously unnecessary


### Sorted array test

Create a function that checks if the input array is sorted. This will be of
great help when you want to quickly confirm that your sorting algorithm did its
job (especially for larger inputs).

Signature for integer version:

* C++:  
```c++
bool is_sorted(const std::vector<int>& vec)
{
    ...
}
```
* Java:  
```java
public static boolean is_sorted(int[] arr) {
    ...
}
```
* Python:  
```python
def is_sorted(arr):
    ...
```


### Resources

* [StackOverflow: random integers in C++ the modern way][randint-cpp-so]
* [The `<random>` header in C++][randint-cpp]
* [StackOverflow: generating random integers in Java][randint-java-so]
* [Random NumPy array generation in Python][randint-numpy]

### Why is this useful?

You will have a set of tools to quickly test the algorithms and data structures
that you write. You won't need to go through the overhead of generating random
arrays every time you need to test something.


## Homework 2.1: Asymptotic notation

Understand the meaning of different types of asymptotic notation (Big-O,
little-o, Theta, Big-Omega, little-omega). If this is your first time seeing it
and/or you do not understand the formal definition, don't worry -- you will
learn about it more extensively in your Data Structures and Algorithms classes.
For now, (_at the very least_) understand **why** this notation exists and how
it is used in analysis.

An (extremely broad) overview with an example:

* We can express the number of operations a procedure will perform with respect
to the input size N as a function f(N). For example, if the procedure iterates
over an array that contains N items and performs 3 operations each iteration,
then we could say that f(N) = 3N, i.e. the procedure will perform 3N operations
for an input of size N. If we also suppose that we perform one more operation
before the loop (let's say assignment) and one operation after, then we add
those two operations to our function, so f(N) = 3N + 2.
* As the input size grows, the term 2 starts having little to no effect on
f(N). For example, if N = 10000, then f(N) = 30002, which means that the term 2
only makes up 0.006% of the performed operations. The larger we make the input
size N, the more and more negligible that 2 becomes. Therefore, we simply drop
it from the notation. **In general, we drop everything but one "dominant" term
if the runtime function contains summation.**. Because 3N is the dominant term
in our case, the function becomes f(N) = 3N.
* We can also observe that the factor 3 next to N only _scales_ the term. This
scaling is not important when we want to know how the change in size of input
relates to the performance of the procedure. Whether the factor is 3 or 100000,
if we double the input size N, then the number of operations will also double.
**In general, we drop constants no matter how big or small they are, because we
only care about the shape of the runtime function, not its steepness.**
Therefore, we are left with f(N) = N. In this particular case, N is both the
best and the worst runtime complexity of our procedure (because we iterate over
the entire array of size N no matter what). We can therefore say that the
complexity of this procedure is O(N) ("big-O of N").


In general, if we have:

* Constants **c** and **d** (where **c** < **d**)
* A function **g(n)**
* A positive integer **n<sub>0</sub>**

... then the function **f(n)** is:

* **O(g(n))** if f(n) ≤ c∙g(n) for all n > n<sub>0</sub>
    * "Big-O of g(n)" ∼ Worst case performance
    * In plain words: "No worse than g(n)"
* **o(g(n))** if f(n) < c∙g(n) for all n > n<sub>0</sub>
    * "Little-O of g(n)" ∼ Upper bound of worst performance
    * In plain words: "Better than g(n)"
* **Θ(g(n))** if c∙g(n) ≤ f(n) ≤ d∙g(n) for all n > n<sub>0</sub>
    * "Theta of g(n)" ∼ Exact class of performance
    * In plain words: "Proportional to N"
* **ω(g(n))** if f(n) > c∙g(n) for all n > n<sub>0</sub>
    * "Little-Omega of g(n)" ∼ Lower bound of best performance
    * In plain words: "Worse than g(n)"
* **Ω(g(n))** if f(n) ≥ c∙g(n) for all n > n<sub>0</sub>
    * "Big-Omega of g(n)" ∼ Best case performance
    * In plain words: "No better than g(n)"

For example, if the runtime of some procedure is f(n) = 5n<sup>2</sup> - 2n + 5
, then f(n) = O(n<sup>2</sup>). We can prove it by picking the right values for
**c** and **n<sub>0</sub>**:

* We already picked **g(n)** = n<sup>2</sup>
* Let **c** = 6
* Let **n<sub>0</sub>** = 1
* Then f(n) ≤ c∙g(n) for all n > n<sub>0</sub>, because...  
5n<sup>2</sup> - 2n + 5 ≤ 6n<sup>2</sup> for all n > 1, which means that...  
f(n) is O(n<sup>2</sup>).

There are several major complexity classes. From best to worst:

1. O(1) -- constant
2. O(log(n)) -- logarithmic (usually log base 2, but it can vary)
3. O(n) -- linear
4. O(n<sup>a</sup>) -- polynomial, e.g. O(n<sup>2</sup>)
5. O(a<sup>n</sup>) -- exponential, e.g. O(2<sup>n</sup>)
6. O(n!) -- factorial

### Resources

_Note_: I could post hundreds of links here. I am only giving a sample of a few
that explain it well. You should search "Asymptotic notation" or "big O
notation" on your own and find a resource that suits you.

* [Learn X in Y minutes: Asymptotic notation][xiny-asym]
* [Khan Academy: Asymptotic notation][khan-asym]
* [Big-O explained by the author of "Cracking the coding interview"][big-o-hr]
* [What is a plain English explanation of “Big O” notation?][big-o-so]
* [What is the difference between Theta(N) and O(N)?][theta-o-so]

### Why is this useful?

Why would this _not_ be useful?


## Homework 2.2: Implementing Data Structures and their Operations (due 6/27)

Complete up to the level of your preference. If you are doing levels above 1,
make sure you complete the levels before them first. The higher levels
intentionally require a lot more work so that the higher level students get to
challenge themselves.

If you have not written classes in your language before, read the tutorials on
how to do it ([c++][cpp-class], [java][java-class]) and limit yourself to
levels 1 or 2.

For simplicity, the element type within these data structures should be
integer (unless you are doing level 5). Before implementing _any_ of them, read
the wiki pages (or other tutorials/articles you like) and understand how they
function conceptually. Draw the structures out on a notebook if you need to.
And as usual, ask questions on the Slack channel if anything confuses you.

Every single one of the structures must have these interface methods (along
with the other ones listed):

* _size()_ -- Return the number of elements.
* _empty()_ -- Check whether the container is empty.
* _print()_ -- Print the entire container.

### Level 1

Write implementations for **LinkedList** and **Array** structures. Implement
the LinkedList as a doubly-linked list. Both structures should have the
following interface methods:

* _insert(index, element)_ -- Insert _element_ at the position _index_.
* _prepend(element)_ -- Insert the _element_ at the front.
* _append(element)_ -- Insert the _element_ at the end.
* _get(index)_ -- Return the element at position _index_ (if within bounds).
* _front()_ -- Return the element at the front (if there is one).
* _back()_ -- Return the element at the end (if there is one).
* _search(element)_ -- Return the position of _element_ (if found).
* _remove(index)_ -- Remove the element at position _index_ (if within bounds).
* _popfront()_ -- Remove the element at the front (if there is one).
* _popback()_ -- Remove the element at the end (if there is one).

Compare the runtime complexity of each of these operations between the array
and linked list. Note where they perform well and where they perform poorly.

### Level 2

Use the classes above to write implementations for **Stack**, **Queue**,
**Deque** structures (i.e. use Arrays or Linked Lists as the underlying
containers to store the information and utilize the appropriate operations
within them to interact with the data).

Stack interface:

* _push(element)_ -- Insert _element_ at the end.
* _peek()_ -- Return the element at the end (if there is one).
* _pop()_ -- Remove the element at the end (if there is one).

Queue interface:

* _enqueue(element)_ -- Insert _element_ at the end.
* _peek()_ -- Return the element at the front (if there is one).
* _dequeue()_ -- Remove the element at the front.

Deque interface:

* _pushback(element)_ -- Insert the _element_ at the end.
* _pushfront(element)_ -- Insert the _element_ at the front.
* _popback()_ -- Remove the element at the end.
* _popfront()_ -- Remove the element at the front.

Once again, compare the runtime complexity of each of these operations between
the array and the linked list version.

### Level 3

Write implementations for **BinarySearchTree** (unbalanced) and
**PriorityQueue** structures. Implement **PriorityQueue** as a binary max-heap.
Binary search tree print method should print all of the elements in order. Heap
print method should print elements of the underlying array structure (except
for the dummy element at the index 0). Figure out how to deal with duplicates
in both of these structures.

Binary Search Tree (no balancing) interface:

* _insert(element)_ -- Insert the _element_ into the tree.
* _remove(element)_ -- Remove the _element_ from the tree (if found).
* _search(element)_ -- Check if the element is in the tree.

Priority Queue (Binary Heap) interface:

* _enqueue(element)_ -- Insert the _element_ into the heap.
* _peek()_ -- Return the element at the root of the heap (if there is one).
* _dequeue()_ -- Remove the element at the root of the heap (if there is one).

Analyze the worst-case runtime complexity for each of these operations. Ask
yourself where you think things could be improved.

### Level 4

Write implementations for **HashMap** and **AVLTree** structures. For the
**HashMap**, the key type should be string and the value type should be either
int or string (up to you). Each bucket in the underlying array should be a
linked list and the collision resolution method used should be Separate
Chaining with Linked Lists. Hash Map print method should print all of the
key-value pairs. AVL Tree print method should print all of the elements in
order. Just like in Level 3, figure out how to deal with duplicates.

Hash Map interface:

* _put(key, value)_ -- Insert the _value_ associated with _key_ into the map.
* _get(key)_ -- Return the value associated with the _key_ (if found).
* _exists(key)_ -- Check whether a value associated with the _key_ exists.
* _search(value)_ -- Return the key which the _value_ is associated with (if
  found).
* _remove(key)_ -- Remove the _value_ associated with the _key_ (if found).

AVL Tree interface:

* _insert(element)_ -- Insert the _element_ into the tree.
* _remove(element)_ -- Remove the _element_ from the tree (if found).
* _search(element)_ -- Check if the element is in the tree.

Analyze worst-case runtime complexity for each of these operations. Point out
where things can go wrong with Hash Maps.


### Level 5

Write all of the structures above using templates/generics instead of integers.
For Hash Maps, you do not need to make the key type generic (keep it string).


### Level 6

Implement standard library-like features for all of the structures above. For
example, if you are using C++, then you should try implementing:

* Iterators (in such way that the structures can be used with range-based for
loops). Make sure to consider forward vs backward iterators. Also make sure to
consider const vs non-const (regular) iterators.
* Overloaded operators that make sense, e.g. `<<` (printing to a stream), `==`
(comparing two instances for equal contents), `+` (union of two instances) etc.
* Move constructors and move assignment operators
* A [hash][hash-spec-cpp] specialization

... and if you are using Java, implement:

* Iterators (for the use with range-based for loops)
* toString method overload (for printing)
* equals method overload 
* hashCode method overload

(toString, equals, and hashCode methods are defined in [Object][obj-java] class
that is the parent to all custom classes by default)

### Resources

Wikipedia:
* [Data Structure][ds-wiki]
* [Linked List][ll-wiki]
* [Stack][stack-wiki]
* [Queue][queue-wiki]
* [Deque (Double-ended Queue)][deque-wiki]
* [Binary Search Tree][bst-wiki]
* [Heap][heap-wiki]
* [Hash Map (Hash Table)][hashmap-wiki]
* [AVL Tree][avl-wiki]

Geeksforgeeks:
* [Search, Insert, Delete in an unsorted Array][arr-g4g]
* [Linked Lists][ll-g4g]
* [Intro to Stacks][stack-g4g]
* [Queues (and deques)][queue-g4g]
* [Binary Trees][bt-g4g]
* [Binary Search Trees][bst-g4g]
* [Heaps][heap-g4g]
* [Hashing][hash-g4g]
* AVL Tree: [Insertion][avl-i-g4g], [Deletion][avl-d-g4g]

Other:
* [Hash Tables -- Princeton Algorithms, 4th edition][hash-alg4]
* [How does a Hash Table work? -- StackOverflow][hash-so]


[quicksort]: http://me.dt.in.th/page/Quicksort/
[khan-algo]: https://www.khanacademy.org/computing/computer-science/algorithms
[vis-algo]: https://bost.ocks.org/mike/algorithms/
[big-o-cheat]: http://bigocheatsheet.com/
[fizz]: https://blog.codinghorror.com/why-cant-programmers-program/
[randint-cpp]: http://en.cppreference.com/w/cpp/numeric/random
[randint-cpp-so]: https://stackoverflow.com/a/19728404
[randint-java-so]: https://stackoverflow.com/a/363692
[randint-numpy]: https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html
[xiny-asym]: https://learnxinyminutes.com/docs/asymptotic-notation/
[khan-asym]: https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation
[big-o-hr]: https://www.youtube.com/watch?v=v4cd1O4zkGw
[big-o-so]: https://stackoverflow.com/questions/487258/what-is-a-plain-english-explanation-of-big-o-notation
[theta-o-so]: https://stackoverflow.com/questions/471199/what-is-the-difference-between-%CE%98n-and-on
[cpp-class]: http://www.learncpp.com/cpp-tutorial/81-welcome-to-object-oriented-programming/
[java-class]: https://docs.oracle.com/javase/tutorial/java/javaOO/
[ds-wiki]: https://en.wikipedia.org/wiki/Data_structure
[ll-wiki]: https://en.wikipedia.org/wiki/Linked_list#Doubly_linked_list
[stack-wiki]: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
[queue-wiki]: https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
[deque-wiki]: https://en.wikipedia.org/wiki/Double-ended_queue
[bst-wiki]: https://en.wikipedia.org/wiki/Binary_search_tree
[heap-wiki]: https://en.wikipedia.org/wiki/Heap_(data_structure)
[hashmap-wiki]: https://en.wikipedia.org/wiki/Hash_table
[avl-wiki]: https://en.wikipedia.org/wiki/AVL_tree
[arr-g4g]: http://www.geeksforgeeks.org/search-insert-and-delete-in-an-unsorted-array/
[ll-g4g]: http://www.geeksforgeeks.org/data-structures/linked-list/
[stack-g4g]: http://www.geeksforgeeks.org/stack-data-structure-introduction-program/
[queue-g4g]: http://www.geeksforgeeks.org/queue-data-structure/
[bt-g4g]: http://www.geeksforgeeks.org/binary-tree-data-structure/
[bst-g4g]: http://www.geeksforgeeks.org/binary-search-tree-data-structure/
[heap-g4g]: http://www.geeksforgeeks.org/heap-data-structure/
[hash-g4g]: http://www.geeksforgeeks.org/hashing-data-structure/
[avl-i-g4g]: http://www.geeksforgeeks.org/avl-tree-set-1-insertion/
[avl-d-g4g]: http://www.geeksforgeeks.org/avl-tree-set-2-deletion/
[hash-alg4]: http://algs4.cs.princeton.edu/34hash/
[hash-so]: https://stackoverflow.com/questions/730620/how-does-a-hash-table-work
[hash-spec-cpp]: http://en.cppreference.com/w/cpp/utility/hash
[obj-java]: https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html
