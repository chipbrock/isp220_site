# A little deeper

## How to find the equation without time.


$\require{enclose}\require{cancel}$

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
<v> = \frac{\Delta x}{\Delta t} = \frac{x_f-x_0}{t_f - t_0}
$$

Let's remember what the areas mean for velocity. Suppose we have a **constant velocity**, then the initial velocity is equal to the final velocity and is obviously equal to the average velocity: $v_0=v_f=<v>$. By rearranging Equation \@ref(eq:avev):

$$
\Delta x = <v>\Delta t 
$$

We see that this has the form of an area equation, and the figure suggests that the area under a curve of velocity versus time is the distance traveled:

<img align="center" src="./images/constantv.png">

<BR CLEAR="all">

<figcaption> Constant velocity. </figcaption>

So let's call  $A1$ to be the  ${\scriptstyle \enclose{circle}{\kern .06em 1\kern .06em}}$ area in the figure.

$$
	\text{so } A1 = \text{ base times the height } = (\Delta t)(<v>)
$$(avevtwo)

This is general: the distance traveled is the area under the curve of the velocity as a function of time.

## Average velocity for constant acceleration

Let's step it up to a constant acceleration, which means that the velocity will increase linearly as a function of time. Here it is:

<img align="center" src="./images/vaconstanta.png">

<BR CLEAR="all">

<figcaption> On the left: Acceleration for a...um...constant acceleration. On the right: Velocity for a constant acceleration. </figcaption>

Now what's the average velocity? Well, we calculate the area under the ramped velocity curve and divide by the time and that's the average velocity as in Equation {eq}`avevtwo`. Here it is, using the new area definitions in the figure.

$$
\begin{align}
A = A1 + A2 &= \dfrac{1}{2}\text{base times height } + \text{area of rectangle} \nonumber \\
A = \Delta x &= \dfrac{1}{2}(v_f-v_0)\Delta t + v_0\Delta t \nonumber \\
\Delta x &= \Delta t (\dfrac{1}{2} v_f + v_0 - \dfrac{1}{2} v_0) = \Delta t(v_f + v_0) \nonumber \\
<v> &= \frac{\Delta x}{\Delta t} = \dfrac{1}{2}(v_f + v_0) 
\end{align}
$$

That's interesting. If I'm 6 feet tall and you're 5 feet tall, what's the average of our two heights? That's simple:

$$
<h> = \frac{\text{sum of the heights}}{\text{the number of heights}}=\frac{6+5}{2}=5.5
$$

We've just seen that for a constant acceleration (only) the average velocity is just the average of the beginning and ending velocities:

$$
<v> = \frac{v_y + v_0}{2} \label{averagev}
$$

Don't buy it? Look at this geometrical construction.

<img align="center" src="./images/averagetriangles.png">

<BR CLEAR="all">

<figcaption> On the left: the same straight velocity curve (line) for constant acceleration as above. In the middle, remove the upper corner triangle at the midpoint. On the right: Moving things around to replace that triangle in the slot to the left. </figaption>


We started in the left at an initial speed of $v_0$ at $t_0$ and then at constant acceleration, go faster by time $t_f$ to $v_f$. Let's calculate the areas differently:

1. Lop off the little notch at the top of the triangle. You can see it is gone in the middle figure, with only a shadow of it remaining. So $A1 = A3 + A4$. So the area is less overall.
2. Now restore that $A4$ in the little area to the left of the truncated triangle.
3. Now we have a rectangle $A5 = A3 + A4$.
4. The area that we started with is now the same as in the right-hand figure, but it's now the sum of the areas of two rectangles:

$$
A1 + A2 = (v_? - v_0)\Delta t + v_0 \Delta t  \nonumber
$$

But what's $v_?$? In order for this construction to work, $v_?$ has to be the midpoint between $v_f$ and $v_0$: 
$$
v_? = \dfrac{v_f - v_0}{2} \nonumber
$$

So here we go:

$$
A1 + A2 = \left(\frac{v_f-v_0}{2}\right)\Delta t + v_0\Delta t = \Delta t \frac{v_f+v_0}{2} \nonumber
$$

and we get the same result as above:

$$
\frac{A1 + A2}{\Delta t} = \frac{\Delta x}{\Delta t} = \frac{v_f + v_0}{2} = <v>
$$

Now, with this result for the average velocity, we can derive the rest of the equations in the chapter.

## The first equation

The total displacement, $\Delta x$ is still the area under the velocity curve and the average velocity is *still*

$$
\text{ first equation } <v> = \frac{\Delta x}{\Delta t} \to \Delta x = <v> \Delta t \label{firstagain} \nonumber
$$

## The second equation

Likewise, the average acceleration is:

$$
\text{ second equation } <a> = \frac{\Delta v}{\Delta t} = \frac{v_f-v_0}{\Delta t} \to v_f = v_0 + a \Delta t \label{second} \nonumber
$$

## The third equation

If we now try to isolate $x$ and $t$, we can derive the third equation of the set. Let's take our constant acceleration average velocity and substitute into it Equation \@ref(eq:second):

$$
<v> = \frac{v_y + v_0}{2} = <v> = \frac{v_0+a \Delta t + v_0}{2}=<v> = \frac{2v_0+a \Delta t}{2}= v_0 + \dfrac{1}{2}a \Delta t
$$

Now go to Equation \@ref(eq:firstagain) and substitute from this:

$$
\Delta x = <v> \Delta t = \frac{2v_0+a \Delta t}{2}\Delta t= v_0\Delta t + \dfrac{1}{2}a (\Delta t)^2 \label{third}
$$

Now if we remember that $\Delta x = x-x_0$ and that we can always force $t_0=0$, we get 

$$
x = x_0 + v_0t + \dfrac{1}{2}at^2 \label{thirdagain}
$$

## The fourth equation

Now we can eliminate time and get the fourth equation.

$$
v_f = v_0 + at \text{,  so  } t = \frac{v-v_0}{a}
$$

If we substitute this into Equation \@ref(eq:thirdagain) we get:

$$
x = x_0 + v_0\frac{v-v_0}{a} + \dfrac{1}{2} a\left(\frac{v-v_0}{a}\right)^2
$$

Now after a tedious algebra event... we get the fourth equation:

$$
v^2=v_0^2 +2ax \label{fourth}
$$

Whew.
