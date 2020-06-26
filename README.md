Two different code to generate numbers in a Fibonacci series.

fiboWithYield.py --> Uses Python's `yield` keyword to generate the numbers via a generator.

fiboWithReturn.py --> Uses `return` keyword to generate the numbers.

Analysis of time and memory shows the advantage of `yield` keyword. A sample output below:


With yield:

```
(base) Niteshs-MacBook-Pro:yield-python niteshsinha$ python fiboWithYield.py
Generating 1000000 Fibonacci numbers. Please wait!!
Memory used to generate 1000000 Fibonacci numbers: 1.83 MB
Time taken to generate 1000000 Fibonacci number: 9.638243 seconds
```

Without yield:

```
(base) Niteshs-MacBook-Pro:yield-python niteshsinha$ python fiboWithReturn.py
Generating 1000000 Fibonacci numbers. Please wait!!
Memory used to generate 1000000 Fibonacci numbers: 1210.18 MB
Time taken to generate 1000000 Fibonacci numbers: 37.687477 seconds
```


