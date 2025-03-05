# Exercise 5

In class, we have seen two different ways to perform multiple measures with timeit:
The first uses the number parameters, as in:

`elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)`

The second uses the repeat function, as in:

`times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)`

1. These approaches are designed to deal with different types of
measurement noise. Think about what happens when we try to time
a program, and which types of issues may result in an incorrect
measurement. Reflect on how the two approaches (`timeit` and
`repeat`) attempt to address these issues. Discuss when it is
appropriate to use one or the other.

> One main issue of timing a program is there is often times code we need to execute before we reach the code segment we want to time. `timeit()` and `repeat()` solve this problem by defining this starting code as 'setup' and the code we want to measure as the main code. This 'setup' code isn't timed, so a more accurate time for the code to measure can be produced.
>
> Another issue is testing the performance several times. Both functions have different ways of solving this. `timeit()` can accept a number parameter which returns the total time it took to execute the code segment a number of times. `repeat()` introduces another parameter called repeat which returns an array of the times it took for the code segment to execute, with the array length being the repeat number.
>
> `timeit()`is better if we want a sum of the times for the code segment to execute a number of times. `repeat()` is better for giving out individual times of each run-through.

2. Typically, the output of `timeit` is post-processed to compute some sort of aggregate statistics. Let’s only consider three: `average`, `min`, and `max`. Which one is the appropriate statistic to apply to the output of `timeit.timeit()`? What is the appropriate statistics to apply to the output of `timeit.repeat()`? Discuss why.

> `average` is the most appropriate for `timeit.timeit()`. The `timeit()` function returns the total amount of time it takes to run the code segment a number of times, and it is pretty much impossible to precisely get the min and max times from it, therefore the average is the only thing we can pull from it.
>
> `min` is the most appropriate for `timeit.repeat()`. `timeit.repeat()` returns an array of the times for the code segment to execute. A max value may or may not be because of the program, but because of external factors outside of the program interfering with the performance. An average will also take into account these external factors. A min value will give the lower bound of how fast the code segment runs based on the specific machine.