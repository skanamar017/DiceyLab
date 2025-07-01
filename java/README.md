# Kris-Tof Dice Toss

Create a Dice class that acts like a set of N random-tossed dies.

```java
Dice dice = new Dice(2); // for craps
Dice dice = new Dice(5); // for yatzee

Integer toss = dice.tossAndSum();
```
make a couple unit tests for the Dice class. 

Create a tracking class Bins that can be used to track these results.

```java
Bins results = new Bins(2, 12); // for bins from 2..12
Integer numberOfTens = results.getBin(10); // returns the number of tens in the 10 bin
results.incrementBin(10); // should increment bin # 10

```
make a couple unit tests for the Bins class.

Create a Simulation class whose Constructor takes arguments:
    numberOfDies to throw
    numberOfTosses to run

Create a simulation where two dies are thrown one million times. Keep track of all results.

```java
Simulation sim = new Simulation(2, 10000);

sim.runSimulation();

sim.printResults();
```
You can use a main() to run the simulations.

In your pull requests, create a new file with your name as the filename.
Paul's would be PaulResults.md

Paste a copy of your text results into that file and then submit your pull request.

the results of the sim.printResults() should be an output string that looks like this:

```java
***
Simulation of 2 dice tossed for 1000000 times.
***

 2 :    27917: 0.03 **
 3 :    55422: 0.06 *****
 4 :    83457: 0.08 ********
 5 :   110961: 0.11 ***********
 6 :   139098: 0.14 *************
 7 :   166977: 0.17 ****************
 8 :   138386: 0.14 *************
 9 :   111102: 0.11 ***********
10 :    83367: 0.08 ********
11 :    55799: 0.06 *****
12 :    27514: 0.03 **
```

**Hey**, that looks like a _normal distribution_.

## What's a normal distribution?

A _normal distribution_ is a probability distribution that is commonly used in statistics to describe real-world phenomena that tend to cluster around a mean value. It is also known as a Gaussian distribution or a **bell curve**.

In a normal distribution, the data is symmetrically distributed around the mean value, with the majority of the data falling within one standard deviation of the mean. The distribution is characterized by two parameters: the mean (μ) and the standard deviation (σ). The mean represents the center of the distribution, while the standard deviation represents the spread of the data.

The normal distribution is important in statistics because many natural phenomena, such as human height and IQ scores, tend to follow a normal distribution. It is also used in hypothesis testing and confidence interval calculations, as well as in machine learning algorithms such as linear regression and neural networks.

The normal distribution has several key properties, including:

- It is symmetric around the mean.
- The mean, median, and mode are all equal.
- The total area under the curve is equal to 1.
- Approximately 68% of the data falls within one standard deviation of the mean, 95% falls within two standard deviations, and 99.7% falls within three standard deviations.

So a normal distribution is a probability distribution that is commonly used to describe real-world phenomena that tend to cluster around a mean value. It is characterized by its symmetry, mean, and standard deviation, and is important in statistics and machine learning.

## Why do two rolls of a die tend toward a normal distribution?

Two rolls of a die do not give a normal distribution of values. In fact, the distribution of values obtained from rolling a single die is uniform, meaning that each possible value (1 through 6) has an equal probability of occurring.

However, if you roll two dice and add the values together, the resulting distribution of values will approach a normal distribution as the number of rolls increases. This is due to the central limit theorem, which states that the sum of a large number of independent and identically distributed random variables will approach a normal distribution.

In the case of rolling two dice, the sum of the values obtained is the random variable of interest. As the number of rolls increases, the distribution of the sum of the values will approach a normal distribution, with a mean of 7 (the expected value of the sum of two dice) and a standard deviation of approximately 2.42.

It's worth noting that the distribution of the sum of two dice is not exactly normal, as it is a discrete distribution with a finite number of possible values. However, for practical purposes, the normal distribution is often used as an approximation.
