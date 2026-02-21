## Lorentz Transformations

Notice that our model for transforming space intervals for our Newtonian sidewalk is like a little computing machine:

```{note}
* Space terms in the away frame, ie, $x_A$ --- in
* Space terms transformed into the home frame, ie, $x_H$ --- out
```

That's of course what an equation does. A perfect candidate for our fake circuit:

<img align="left" src="../_images/relativity/Galilean_trans.png" width=90%/>

<BR CLEAR="all">

```{admonition}  &nbsp; Pencils Out! 🖋 📓
:class: warning

Of course what our fake processor is doing is calculating:

$$
\begin{align*}
x_H=&x_A+ut \\
t_H=&t_A=t
\end{align*}
$$

Notice that the time does not change in the Newtonian/Galilean transformation. Nobody had ever imagined that to be different.

Remember that Lorentz preceded Einstein in worrying about Maxwell's equations and the comparisons across co-moving reference frames in in investigating them he came up with a different kind of transformation, which we call the Lorentz Transformations. Einstein derived them from an entirely different approach, without an ether, but the name stuck. These go into our processor the same, but come out differently:

<img align="left" src="../_images/relativity/Lorentz_trans.png" width=90%/>

The Lorentz Transformations (are a "thing" in relativity) are quite different, but familiar in some respects:

$$
\begin{align*}
x_H=&\gamma(x_A+ut_A)\\
t_H=&\gamma(t_A+\dfrac{u}{c^2}x_A)
\end{align*}
$$

Squint at these two equations for a moment. First, remember that if the frame speeds are very low compared with $c$, then

$$
\begin{align*}
\beta =& \frac{u}{c} \xrightarrow{u<<c} 0 \\
\gamma =& \frac{1}{\sqrt{1-\left(\dfrac{u}{c}\right)^2}}\xrightarrow{u<<c} 1
\end{align*}
$$

So now look at the first transformation equation: familiar, right? It's just the Newtonian/Galilean transformation.

```

```{admonition}  &nbsp; Please study example 1  🖋 📓
:class: danger

<a href="../examples/relativity/LT_extereme_1_R3_E1.html" target="_blank">What do the transformations look like when u is small?</a>
```


The second transformation is completely different from the Newtonian/Galilean transformation because the time coordinate also changes. But that's not a surprise now that you've enjoyed the Time Dilation experience. But again, with the low frame reference speeds, we get the Newtonian/Galilean transformation back.

Two things happen when we now take the Lorentz Transformations seriously. Remember that Newton's Second law involves space and time variables. If you want to compare a force between co-moving inertial frames of reference you must substitute the space and time variables with the Lorentz-Transformed versions and what you get is: something entirely different.

> Newton's Second law, <em>F = ma</em> is completely different between two frames: Newton's Second law of motion is <em>not invariant with respect to relative motion</em>.  </p>

What about the other great physical law? Maxwell's Equations? There's a surprise there also: