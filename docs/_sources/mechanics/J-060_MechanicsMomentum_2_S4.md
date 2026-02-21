## The "Quantity of Motion": Momentum

We just developed a sense that our hand-built, car-pushing formula, Eq. {eq}`almostimpulse`  has to depend on speed *and* mass and so we'll just add it in on the right-hand side to get:

```{admonition} &nbsp; Pens out!
:class: warning

$$
F\Delta t = m\Delta v  
$$ (impulse)

Being more explicit, when fleshed out impulse is

$$
F\Delta t = m(v - v_0)
$$ (fullimpulse)

> **There’s more to this story**
>To be totally correct, the right hand side of this equation can be written as $\Delta (mv)$ which recognizes that the mass might change instead of, or in addition to, the velocity changing. This is how a balloon jumps from your hand when you stop pinching the nozzle, or how a rocket is propelled by ejecting burned propellent out the back. In each case, the mass of the moving object changes and that results in a thrust. But we’ll not encounter that in QS&BB.

This quantity on the right, $mv$ is momentum.
```

### Momentum In Practice



This was Newton's second good idea: the concept of "**momentum**" which he called the "quantity of motion" --- a nice description, I think. The idea that a moving object possessed *something* --- some quality --- was pretty hard to ignore. But, nobody could figure out how to describe it for 2000 years before him. Aristotle just denied it: "No," a moving object doesn't possess any quality. Galileo vaguely said "yes," there is something "in" a moving body that he called *impetio*. Kepler seemed to say "yes." Descartes definitely said "yes." Newton agreed with his 17th century predecessors but made the idea useful.

```{admonition} &nbsp; Pens out! 🖋 📓
:class: warning

What he concluded was that the "quantity of motion" is **momentum**. Keeping with tradition by using the symbol "*p*" as its nickname, momentum is:

$$ \begin{equation}
p = mv
\end{equation} $$ (momentum)

With this now we can continue the manipulation of Eq. {eq}`fullimpulse` and restate it one more time in terms of momentum:

$$
F\Delta t = \Delta p 
$$ (impulse4)
```

Remember, sports with balls are delivery vehicles for impulse questions:

```{admonition} &nbsp; Please study Example 2:
:class: warning

<a href="./../examples/mechanics/nimitz_1_E2.html" target="_blank">Big Boat </a>

```

```{admonition} &nbsp; Please answer Question 2 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/lzKzSs" target="_blank">golf and impulse </a>

```

How about stopping? Violent stopping? Besides, you've wondered when an apple question might appear.

```{admonition} &nbsp; Please study Example 3:
:class: warning

<a href="./../examples/mechanics/apple_1_E3.html" target="_blank">applesauce </a>

```

```{admonition} &nbsp; Please study Example 4:
:class: warning

<a href="./../examples/mechanics/dragon_1_E3.html" target="_blank">SpaceX docking at ISS </a>

```

```{admonition} &nbsp; Please answer Question 3 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/dgwcM0" target="_blank">more applesauce </a>

```

> We're going to find that momentum is the most important quantity in our particle physics story.

>**The sports quantity**
>Equation $ \ref{eq:impulse4} $ works in three ways: either you know the force and you use the formula to calculate the change in momentum in a given time. Or, you know the change in momentum and you use it to calculate the total force in a given time, or you adjust the time for a given force.<br>
>Now you've gotten the formula that governs all sports involving whacking one thing with another, like baseball, golf, tennis, soccer, or football. Think about what you almost always want to do: you want to make the ball go faster after you hit it. That means, you want the change in the momentum to be the highest possible. So, Eq. \@ref(eq:impulse4) tells you how: you hit the ball as hard as you can (that's a large $F$) and you get "good contact" (which means you hit the part of the bat or racquet or club where you can touch the ball as long as possible...which is the largest $\Delta t$).<br><br>
>This also explains how airbags and bumper-crumple zones in automobiles work. There, you know what the change in momentum is:
>
> $$
F\Delta t = m\times (v_{after}-v_{before}).$$
> 
>That's the *change* where the final velocity is zero (the car stops). The initial velocity is fixed and so $v_{before}$ has to be divided up between the force and the time in $F\Delta t$ where the force is applied, say to your bumper. High force is not good for the occupants inside the car, so this leads to the design goal of spreading out the time---large $\Delta t$ so that the force will be smaller. This is the same reason that you bend your legs when you jump off a table and hit the floor!

### Momentum Is a Vector

Because velocity is a vector, momentum is also. In the next lesson when we consider collisions, which is where momentum shines in QS&BB, the direction-part of the momentum vector will play a crucial role. For that matter, since momentum and force are vectors the actual general statement about Impulse is:

$$
\vec{F}\Delta t = \Delta \vec{p}
$$

Here's a buzz-word: "state." If you give me the **position and the momentum** of any object---I know everything I need to know to predict where it will be at any subsequent time. In Newton's world, which is good enough for us for a while:

> An object's position and its momentum are called its "state."

