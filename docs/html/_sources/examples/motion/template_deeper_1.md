# A little deeper

## How to find the equation without time.

The equations of motion for constant acceleration are mixtures of the variables in play:

* space
* time
* velocity
* acceleration

We started with space and time and by letting Galileo motivate our choices produced:
$$
x = x_0 + v_0t + \dfrac{1}{2} at^2. \label{first}
$$
Notice that I used "$x$" here which is meant to apply to horizontal acceleration (like walking or in your car) or a vertical direction (like dropping something or throwing something up). This is the most general as it allows for a situation in which the initial position is not 0 and in which the initial velocity is not 0. For example, we could be standing on a roof (at a value of $x_0$ that might be 100 feet) and not just drop something, but throw it straight down so that the initial velocity might be 50 mph. 

But we can derive this from some simple definitions.

Remember that the average speed is equal to:
$$
<v> = \frac{\Delta x}{\Delta t} = \frac{x_f-x_0}{t_f - t_0} \label{avev}
$$
Where I'm calling out the final quantities this one time only. Let's presume that we have started our clock at $t_0=0$ and that simplifies things a bit and here we would get the second equation in the set of 4.

Let's remember what the areas mean for velocity. Suppose we have a **constant velocity**, then this figure shows that the area under the velocity line is the distance traveled: just from the formula for a rectangle:

![](../../images/mechanics/centforce.png)
*A ball going in a circle from overhead at successive times, labeled (a), (b), (c), and (d). The motion is uniform, so the speed around the circle is unchanging which is reflected in the fact that the momentum vector lengths are all the same.*



Likewise, the average acceleration is:
$$
<a> = \frac{\Delta v}{\Delta t} = \frac{v_f-v_0}{t} \label{avea}
$$
But if the acceleration is constant, then $<a>$ is just $a$. If we rearrange \@ref(eq:avea), we find:
$$
v_f=v_0 + at \label{two}
$$
which is the first equation in the set of 4. If we now try to isolate $x$ and $t$, we can derive the third equation of the set. 





Both Equations \@ref(eq:one) and \@ref(eq:two) have time as a variable, but Equation \@ref(eq:one) has space and time and no velocity (the intitial velocity is just a constant number and not a variable) and Equation \@ref(eq:two) has velocity and time, but no space. We can complete that arrangement of the three by eliminating $t$ and deriving an equation that has space and velocity, but no time.

It's important to recognize that this only works for a constant acceleration, if the acceleration is also varying --- which is a pretty common real life event --- then this derivation doesn't work. You'll see why.

