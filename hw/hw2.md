# Homework -- Week 2

## Homewok 2.0: Convenience functions (due 6/22 before the class)

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

* C++: `std::vector<int> rand_int(unsigned int size, int min, int max)`
* Java: `public static int[] rand_int(int size, int min, int max)`
* Python: `def rand_int(size, min, max)` (though you shouldn't be writing this
sort of a function if you are using Python and know what you are doing)


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

* C++: `void print(const std::vector<int>& vec)`
* Java: `public static void print(int[] arr)`
* Python: seriously unnecessary


### Sorted array test

Create a function that checks if the input array is sorted. This will be of
great help when you want to quickly confirm that your sorting algorithm did its
job (especially for larger inputs).

Signature for integer version:

* C++: `bool is_sorted(const std::vector<int>& vec)`
* Java: `public static boolean is_sorted(int[] arr)`
* Python: `def is_sorted(arr)`


### Resources

* [StackOverflow: random integers in C++ the modern way][randint-cpp-so]
* [The \<random\> header in C++][randint-cpp]
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

* Constants c and d (where c < d)
* A function g(n)
* A positive number n<sub>0</sub>

... then the function f(n) is:

* O(g(n)) if f(n) ≤ c∙g(n) for all n > n<sub>0</sub>
    * "Big-O of g(n)" ∼ Worst case performance
    * In plain words: "No worse than g(n)"
* o(g(n)) if f(n) < c∙g(n) for all n > n<sub>0</sub>
    * "Little-O of g(n)" ∼ Upper bound of worst performance
    * In plain words: "Better than g(n)"
* Θ(g(n)) if c∙g(n) ≤ f(n) ≤ d∙g(n) for all n > n<sub>0</sub>
    * "Theta of g(n)" ∼ Exact class of performance
    * In plain words: "Proportional to N"
* ω(g(n)) if f(n) > c∙g(n) for all n > n<sub>0</sub>
    * "Little-Omega of g(n)" ∼ Lower bound of best performance
    * In plain words: "Worse than g(n)"
* Ω(g(n)) if f(n) ≥ c∙g(n) for all n > n<sub>0</sub>
    * "Big-Omega of g(n)" ∼ Best case performance
    * In plain words: "No better than g(n)"

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
