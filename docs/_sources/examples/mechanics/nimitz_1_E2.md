# The Big Mo, Force and Momentum 

## Example 2: a very big aircraft carrier. so big.

**The Question:** The Nimitz class aircraft carriers (10 of them) are among the largest naval vessels ever produced. (The new Gerald Ford class are more modern but about the same size.) Here are some details, approximates used for easy calculations.

* Mass: 80 Million kg, $80 \times 10^6$ kg.
* top speed: 32 knots or 37 mph or 16.5 m/s 

This is the lead ship of her class, USS *Nimitz* (CVN-68):

```{figure} ./Nimitz.png
---
width: 350px
name: directive-fig
---
USS Nimitz!
```

1. What is the momentum of such a vessel traveling at 10 m/s?

2. It takes miles for a big ship like this to come to a stop. It takes 2.2 nautical miles (4000 m) to stop when it's traveling at 10 m/s, which requires a reverse thrust of 1 million Newtons, $1 \times 10^6$ N, provided by its two nuclear reactors and four steam turbines. How long does it take to stop?

3. What is its acceleration (deceleration)?

------

**The Answer:** 

1. The momentum comes from the definition:

$$
\begin{align*}
p &= mv \\
  & = (80 \times 10^6 \text{ kg})(10 \text{m/s}) \\
p &= 800 \times 10^6 = 8 \times 10^8 \text{kg m/s}
\end{align*}
$$

2. This is an impulse question and we can find it by noting that the initial momentum is the big value above and the final momentum is zero...since it's stopping. So we can get this from the impulse relationship:

   $$
   \begin{align*}
   F\Delta t &= \Delta p \\
    &= p-p_0 = 0-p_0 = -p_0 \\
    \text{the force }& \text{ points away from the motion and the – sign enforces that} \\
    \Delta t &= \frac{-8 \times 10^8 }{-10^6} \\
    \Delta t &= 8 \times 10^2 = 800 \text{ s} = \text{ about } 13 \text{ minutes} 
   \end{align*}
   $$
   
3. Galileo can almost tell us the acceleration. We assume here that it's constant and so we go from a speed of 10 m/s to zero and it takes 800 seconds to do that, so the deceleration is:

$$
a = \frac{\Delta v}{\Delta t} = \frac{10}{800} = 0.0125 \text{ m/s}^2 \nonumber
$$

