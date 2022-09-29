# py-chronos

## About this Project

Python utility tool that takes in a function and outputs symbolic $O$ runtime.

## How it works

In order to approximate asymptotic behavior, we use the second degree Taylor Expansion in order to estimate the trajectory of the runtime given the point. We retain a lookup table for the different asymptoics runtimes that we can expect (This included precomputing first and second derivatives). Following trajectories are known:

$$ O(1), O(n), O(n^2), O(n^3), O(\log{n}), O(n\log{n}), O(2^n)$$

We can compare the second degree Taylor expansion for the data for every trajector that we can expect. The formula for the second degree expansion is shown below.

$$T_2^f(x) = \sum_{n=0}^{2} \frac{f^{(n)}(x_0)}{n!} = g(x_0) + \frac{d}{dx}f(x_0)(x-x_0) + \frac{\frac{d^2}{dx^2}f(x_0)}{2}(x-x_0)^2$$

Where $g(x)$ is defined to be the measured runtime at timestep $x$.

We linearly scale the input to the function and record its runtime. This new update is incorporated at the next time step to get a better approximation of the trajectory. Our optimization problem is defined to be as follows.

$$ \argmin_{f \in F} \sum_i^{i=n}|T_n^f(i)-g(i)|$$

Where $F$ is defined to be the set of all known trajectories to us.

## Getting Started

### Prerequisites

You will need `numpy` in order to use py-chronos. These should install as dependencies by default.

```sh
pip install py-chronos numpy
```

## important links

- https://danielmuellerkomorowska.com/2020/06/02/smoothing-data-by-rolling-average-with-numpy/
- https://pythonnumericalmethods.berkeley.edu/notebooks/chapter16.05-Least-Square-Regression-for-Nonlinear-Functions.html