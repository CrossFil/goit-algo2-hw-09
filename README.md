# Local Search, Heuristics, and Simulated Annealing

## Task Description

Implement a program to **minimize the Sphere function**:

\[
f(x) = \sum_{i=1}^{n} x_i^2
\]

using three different local optimization approaches:

- **Hill Climbing**
- **Random Local Search**
- **Simulated Annealing**

---

## Technical Requirements

1. **Search domain**:  
   \[
   x_i \in [-5, 5] \quad \text{for each parameter } x_i
   \]

2. Each algorithm must return:
   - the approximate optimal point (a list of coordinates `x`),
   - the value of the objective function at that point.

3. Implement the following optimization methods:
   - `hill_climbing` — hill climbing algorithm,
   - `random_local_search` — random local search,
   - `simulated_annealing` — simulated annealing.

4. **Input parameters**:
   - `iterations` — the maximum number of iterations allowed,
   - `epsilon` — convergence threshold, defining sensitivity to small improvements.

5. **Stopping criteria**:
   - The algorithm terminates if the change in the objective function value or in the point's position between two successive iterations is less than `epsilon`.
   - For simulated annealing, the algorithm also terminates if the **temperature drops below `epsilon`**, indicating the search process is effectively exhausted.

6. All algorithms must operate **within the bounds** $x_i \in [-5, 5]$.

---

## Objective

The program should find an **approximation of the global minimum** of the Sphere function using local search heuristics.

---

## Output

The results of all three algorithms should be printed in **a clear and readable format**, for example:

