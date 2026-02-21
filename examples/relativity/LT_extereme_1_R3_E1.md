# Relativity 3

## Example 1: The Lorentz Transformation at the airport

**The Question:**  The Lorentz Transformation is the relativistic version of the Galilean transformation. The former transforms space and time while the latter transformed only space.

Let's look at the Lorentz Transformation in the airport --- my silly way of saying, when the Away frame is moving relatively slowly compared with the speed of light. 

***The scenario:***

Here it is:

$$
\begin{align}
x_H=&\gamma(x_A+ut_A)\\
t_H=&\gamma(t_A+\dfrac{u}{c^2}x_A)
\end{align}
$$

------

**The Answer:** 

Let's look at them individually. Let's define:

$$
\epsilon = \frac{u}{c}
$$

and remember that we're going to look at cases in which $\epsilon$ is the smallest number you can ever think of. Try it: think of the smallest number you can. $\epsilon$ is smaller than that. We can think of it as essentially zero. (Do you see that we're doing calculus without doing calculus? You're welcome.)

Okay. Let's take care of $\gamma$:

$$
\begin{align*}
\gamma &= \frac{1}{\sqrt{1-(\frac{u}{c})^2}}\\
\gamma &= \frac{1}{\sqrt{1-(\epsilon)^2}} \text{ let $\epsilon$ be tiny:}\\
\gamma &= 1
\end{align*}
$$

Now Equation 1, the space transformation part:

$$
\begin{align*}
x_H &= \gamma(x_A+ut_A) \text{ which we'll now let $\epsilon$ get tiny} \\
x_H &= 1(x_A+ut_A)
\end{align*}
$$

and bingo: that's the sidewalk transformation, the Galilean transformation.

Now let's work on the new bit: the time transformation piece, Equation 2:

$$
\begin{align*}
t_H=&\gamma(t_A+\dfrac{u}{c^2}x_A)\\
x_H=&\gamma(x_A+ut_A)\\
t_H=&\left( \frac{1}{\sqrt{1-(\epsilon)^2}}\right)(t_A+\dfrac{\epsilon}{c}x_A) \text{ let $\epsilon$ be tiny:}\\
t_H=&t_A
\end{align*}
$$

which is, again, what Galilean transformations do: they don't change time.
