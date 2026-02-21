# Relativity 4

## Example 2: How Good is the Approximation?

**The Question:**  

Remember that the expansion of the gamma function that was used was 
$$
\begin{align*}
\gamma &=\frac{1}{\sqrt{{1-\beta^2}}} \\
\text{ the approximation is: } \gamma &\approx 1+\dfrac{1}{2}\beta^2
\end{align*}
$$
How far out in speed must we go with the approximate expansion of the gamma function to deviate from the real value by 0.1?


------

**The Answer:** 

Let's look at some values of $\beta$ and use the interactive $\gamma$ in the text and compare to the calculated approximation. For example:

for $\beta = 0.2$, 


$$
\gamma \approx 1+ \frac{1}{2} (0.2)^2 = 1.02 \nonumber
$$

Here's a collection of comparisons:

| $\beta$ |  actual $\gamma$    | approx. $\gamma$     |
| ------- | ---- | ---- |
|   0.2      |  1.021    |  1.02    |
|      0.3   |  1.048    |  1.045    |
|         0.4|  1.091    |  1.08    |
|    0.5     |  1.155    |  1.125  |
|    0.6     |   1.25   |  1.18    |

So by the time the speed has reached 60% of the speed of light, the approximation is no longer valid by about 0.1. One would then add another term in the expansion which would make the approximation:
$$
\gamma \approx 1+ \frac{1}{2} \beta^2 + \frac{3}{8}\beta^4 \nonumber
$$
which would add 0.049 to the value in the table. 

