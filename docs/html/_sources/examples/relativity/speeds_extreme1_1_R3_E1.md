# Relativity 3

## Example 2: Speeds in slow motion (get it?)

**The Question:**  The relativistic speed relationship looks much different from the simple, intuitive speed transformation of the airport. Let's look at it for the case in which the speed of the Away frame ($u$, remember) is small independent of the speed of the object moving inside of the Away frame ($v_A$, remember). 

***The scenario:***

- The Away frame is moving relative to "us" at a speed of $u$. An object is moving within that frame at a speed of $v_A$. So if it's the airport and you're walking on the moving sidewalk at 2 mph relative to the sidewalk, that's $v_A$. 
- The speed of the moving object as observed by the Home frame is $v_H$. Again, if it's the airport and the sidewalk moves at $u=3$ mph, then $v_H=v_A+u=2+3=5$ mph. 
- But this is relativity! So that means that $u$ is very, very fast and we have a different relationship:

$$
v_H = \frac{v_A + u}{1+\dfrac{v_Au}{c^2}}
$$

Somewhere inside of Equation 1...should be our simple, low-speed airport experience, right? Let's unwrap it.

------

**The Answer:** 

Let's look at three scenarios:

**Slow frame:** When the moving frame is slow relative to the speed of light. Let's call 

$$
\dfrac{u}{c}=\epsilon \nonumber
$$

and rewrite our relationship:

$$
v_H = \frac{v_A + u}{1+\dfrac{\epsilon v_A}{c}} \nonumber
$$

Now let's imagine that $\epsilon$  is smaller than any number you can imagine... so for $u$ very much smaller than the speed of light, $\epsilon$  is itsy bitsy. Can you see that the second term in the denominator is as good as 0? Then we'd have

$$
v_H=_A+u \nonumber
$$

which is exactly the Galilean "airport" situation. 

**Really fast frame:** Let's make our moving frame a light beam, so that $u=c$. What happens?

$$
\begin{align*}
v_H &= \frac{v_A + u}{1+\dfrac{v_Au}{c^2}} \\
v_H &= \frac{v_A + c}{1+\dfrac{v_Ac}{c^2}} \text{ now multiply by $\frac{c}{c}$ which is after all multiplying by 1}\\
v_H &= \frac{v_A + c}{1+\dfrac{v_Ac}{c^2}} \times \dfrac{c}{c} \\
v_H &= \frac{v_A + c}{c+v_A} \times c \\
v_H &= c
\end{align*}
$$

It doesn't matter how fast the thing traveling at $v_A$ is...once that Away frame itself is moving at $c$, then that's all the Home frame would see: $c$. So to speak.

**Something moving really fast within the frame:** Lets' now make our moving object be a light beam, so $v_A=c$:

$$
\begin{align*}
v_H &= \frac{v_A + u}{1+\dfrac{v_Au}{c^2}} \\
v_H &= \frac{c + u}{1+\dfrac{cu}{c^2}} \\
v_H &= \frac{c + u}{1+\dfrac{cu}{c^2}}\times \frac{c}{c} \\
v_H &= \frac{c + u}{c+u}\times c \\
v_H &= c
\end{align*}
$$
Just another way of saying "Second Postulate"!
