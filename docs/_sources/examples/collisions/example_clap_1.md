# Collisions

## Example 1: Impulse, Newton’s 3rd law, and Momentum Conservation

**The Question:** 

Let’s develop the simple machinery to analyze the simple, short “round of applause” we just gave to Mr Huygens.

```{figure} ./clap.png
---
width: 350px
name: directive-fig
---
One round of applause.
```

**The Answer:**

Let's develop the simple machinery from Newton's ideas. Remember the impulse model…let's enjoy that one again:

$$\vec{F}\Delta t = \Delta \vec{p} .$$ (impulse)

The momentum change of an object is equal to the force that alters its motion times the time through which that force acts. Think about what happens when object A collides with object B. Let's imagine that A is your left hand and B is your right hand. Now give Huygens a big hand (shall we?) and clap them together, like Collision 3.

You can make two simple, but important observations from this:

>Some of the quantities which appear to be absolutely conserved in nature are: momentum and energy; angular momentum; and electric charge. As we’ll see, energy and momentum are actually a single quantity which is conserved.

When they just start to make contact your left hand begins to exert a force on your right hand and your right hand exerts a force on your left. Is there any difference? Does one hand fly away from the other? No...from Newton's 3rd law, these forces are equal (and opposite). So let’s name your hands. Feel free to write on your palms: 


$$
\begin{align*}
F_\text{left} &= F_A \\
F_\text{right} &= F_B\end{align*}
$$

We’re recreating Collision 3 (but without glue). They have opposite directions, so while the magnitude of the forces is the same, the directions are opposite:

$$
F_\text{A} = - F_\text{B}. \nonumber
$$

Is the <i>time</i> that your left hand is in contact with your right hand any different from the time that your right hand is in contact with your left? No, of course not. So:

$$
\Delta t_A = \Delta t_B \nonumber
$$

So let's put these two silly (but not silly!) observations to work. Look at the impulse experienced by any two colliding objects A and B (your two hands). Here are those relations that describe their changes in momentum:

$$
\vec{F}_A\Delta t_A = \Delta \vec{p}_A \nonumber
$$

$$
\vec{F}_B\Delta t_B = \Delta \vec{p}_B \nonumber
$$

And as we learned "by hand," (see what I did there?) both, $F_A = -F_B$ and $\Delta t_A = \Delta t_B$. So:

$$
\begin{align*}
F_A\Delta t_A &= - F_B \Delta t_B \text{ …giving us:}\\ 
\Delta p_A &=  - \Delta p_A\end{align*}
$$

Let's pretend that their collision is in one dimension and remember the convention for “change of” and that we'll use the subscript “$0$” to indicate the initial quantities:

$$
\begin{align*}
 \Delta p_{A} &= p_{A} - p_{A,0} \nonumber \\
\Delta p_{B} &= p_{B} -p_{B,0} \nonumber \end{align*}
$$

Putting them together, we then find:

$$
\begin{align}\Delta p_{A} &= - \Delta p_{B}  \nonumber\\
      p_{A} - p_{A,0} &= - (p_{B} - p_{B,0}) \nonumber\\ 
\text{rearrange} &\text{ these terms...} \nonumber \\
p_{A,0} +  p_{B,0}  &= p_{A} + p_{B} \label{pcon} \end{align}
$$
