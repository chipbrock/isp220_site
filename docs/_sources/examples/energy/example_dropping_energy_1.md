# Energy

## Example 4: energies exchanged

**The Question:** 

What are the contributions to its energy at point A, point B, and halfway between them in the following figure? This apple has a mass of 100 grams.

<img align="center" src="./apple1m.png">

<BR CLEAR="all">

Our apple has a mass of 100 g $=$ 0.1 kg and for simplicity’s sake, let’s pretend that the acceleration due to gravity is 10 m/s$^2$ rather than its more precise value of 9.8 m/s$^2$.

What are the contributions to its energy at point A, point B, and halfway between them?

**The Answer:**

The contributions ot the energy of the apple would be combinations of potential and kinetic energy. Once we define where the "zero" of potential energy is located, it can be calculated at any height. Obviously, the most sensible thing to do is to define

$$
U(B) = 0. \nonumber
$$

When the apple is just tipped over the edge of the table, its energy is *all potential* and would have the value:

$$
E = U(A) = mgh_A = (0.1)(10)(1) = 1\text{ J}. \nonumber
$$

That sets the scale of what 1 Joule of energy is like...Dropping an apple a meter above the ground provides it with a potential to do work on whatever it it lands on. 

When the apple has reached point B, its potential energy is spent, traded for kinetic energy as the apple has sped up from rest at A to the fastest that it will be just before hitting the floor (and deforming into a bruised fruit). So that energy is:

$$
E = K(B) = 1/2mv^2=U(A) = \text{ in value to }mgh_A \nonumber
$$

So we could ask how fast the apple is going, and this energy balance gives us the answer:

$$
\begin{align*}
K(A) + U(A) &= K(B) + U(B) = E_T \text{ the total, constant energy}\\
0 + U(A) &= K(B) \\
mgh_A &= 1/2mv^2 \\
gh_A &= 1/2v^2 \\
v &= \sqrt{2gh} = \sqrt{(2)(10)(1)} = \sqrt{20} = 4.5 \text{ m/s}
\end{align*}
$$

It dropped from rest, so $K(A)=0$ and when it hit the ground, its potential energy is spent so $U(B)=0$.

But we could have gotten this same answer from Galileo’s constant acceleration formula from the last equation for constant motion:

$$
v_2=v_0^2 + 2ax = v^2 = 2gx
$$

Finally, halfway between A and B, the energy is made up of less potential energy than A and less kinetic energy than at B. Since $E_T = 1$ J and is shared with potential and kinetic energy as it falls, 

$$
E_T  = U(\text{halfway}) + K(\text{halfway})
$$

But we know $E_T=1$ J, so we can first calculate $U(\text{halfway})$ and then subtract from $E_T$ and find $K(\text{halfway})$:

$$
\begin{align*} K(\text{halfway})  & = mgh_{\text{halfway}} = (0.1)(10)(0.5) = 0.5 \text{ J} \\
K(\text{halfway})&= E_T-U(\text{halfway}) = 1-0.5=0.5  \text{ J}        \end{align*}
$$

<video src="./stop_shot_resolution.mp4"></video>
