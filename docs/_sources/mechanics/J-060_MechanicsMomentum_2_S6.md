## Newton's Second law

Students in a physics class become intimately familiar with the 2nd law, which is all about momentum and how to change it. A simple arrangement of the Eq. 6.3 relation yields the real mathematical definition of Newton's 2nd law:

$$
\vec{F}=\frac{\Delta \vec{p}}{\Delta t}.  
$$ (impulse)

Maybe you've maybe seen this equation but written in a different way. Inserting back the definition of momentum, $p=mv$  (in one dimension, so we'll drop the vector notation):

```{admonition} &nbsp; Pens out!
:class: warning


$$
F=\frac{\Delta p}{\Delta t} = \frac{\Delta mv}{\Delta t}  
$$ (second1)

Let's assume that the mass of the object doesn't change, so we can push the $\Delta$ operation through the mass and let it act directly on the velocity and get

$$
F=\frac{m\Delta v}{\Delta t} \label{second3}
$$

and what's $\Delta v / \Delta t$? That's nothing more than acceleration, so we finally arrive at the T-shirt version of the famous Newton's Second law of motion:

$$
\begin{equation}
F=ma. 
\end{equation}
$$ (second4)

$$F=ma.\label{second4}$$

Notice that if you isolate the acceleration by dividing both sides by $m$,

$$
a = \frac{F}{m} \nonumber
$$


```

you get the force divided by the mass. There's the "inertia" nature of mass making its appearance: the *larger* the mass (so that $\frac{1}{m}$ is a *small* number) the *harder* it is to accelerate for a given force (the Volkswagen)—$a$ is small. On the other hand, if that force is now applied to a light object (so that $\frac{1}{m}$ is a *larger* number) then the acceleration will be *greater* (that's the wagon).

```{admonition} &nbsp; Pens out!
:class: warning

Stare at Eq. {eq}`impulse` : if you think about it, there are three ways for $\vec{p}$ to change:

1.  As we've just seen, if the speed changes, the velocity vector changes, so then the momentum vector changes. That's easy and what you'd expect.

2.  If the *mass* changes, then the momentum changes.

3.  If the velocity *vector* changes, but the speed stays the same? Ah. That's interesting, and we'll look at that carefully in section *Circular Motion* below.


```

```{aside}

Item #2 at the left requires some thought. Remember what "change" means: something at the end minus something at the beginning. So, the mass in a balloon is decreasing, so $\Delta m = m - m_0$ which is a negative quantity. in fact, the mass escapes out the nozzle and the momentum change is in the opposite direction (the negative sign of $\Delta m$ becomes a directional sign of the opposite of the direction that the mass goes.

```

#1 makes sense in our everyday lives. If you change the speed, the velocity will change. #2 is less obvious but think about pinching the opening of a balloon that you've blown up. The balloon's mass consists of the stretchy material of the balloon plus the mass of the air inside. Held out in front of you there is no net force and it's at rest in your hand. Puncture it with a pin and the air rushes out *fast* and so the mass of the air inside the balloon rapidly decreases. The consequence of that decrease in mass, a $\Delta m$ in a time $\Delta t$ all by itself results in a change in the momentum of the balloon! That's how rockets work. For #3 we'll wait a bit.

Let's play with this on a trip:

```{admonition} &nbsp; Please study Example 5:
:class: warning

<a href="./../examples/mechanics/airbus_accelerate_1_E4.html" target="_blank">AIRBUS accelerating </a>

```
