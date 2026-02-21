## Gravitational Energy

We say that the planets are "bound" in their orbits to the gravitational field of the Sun. That word "bound" really means what it says! If, like the Moon, the planets didn't have their orbital motion – if they were just sitting still, they would fall to the Sun. They're captured by it because of the infinite extent of the gravitational force. Look at the famous  equation again:

$$F_{S-p} = G\cfrac{M_Sm_p}{R_{S-p}^2},$$

where here "*S*" stands for the Sun and "*p*" stands for any of the planets. That pesky inverse-square rule means that no matter how far away a planet is from the Sun, it's always going to feel even a tiny bit of attraction. Take Jupiter out of the solar system and transport it to the Andromeda Galaxy and it will still feel the force of the Sun's gravitational force (although of course it will feel much stronger gravitational forces from sources in its new neighborhood). Even if it's at just a smidgen less than an *infinite* distance away: still a force. 

Ah. But infinity is always interesting. Let's think about this figure:

```{figure} ./../_images/cosmology/applesun.png
---
name: applesun
width: 350px
align: center
---
An apple in outerspace. Currently it's at a distance $R_1$ from the center of the Sun and it's about to be repositioned at a distance $R_2$.
```

Let's place an apple (of mass $m$) at a distance $R_1$ from the Sun's (of mass $M$) center. It would feel the force of gravity from it (and the Sun from the apple) and it would have the value:
$$
F=G\frac{Mm}{R_1^2} \nonumber
$$
Suppose we let go. What would happen?

> **Wait.** Well, it would start to move.<br><br>
> **Glad you asked.** Right. It experiences a force and where there's a force, there's an acceleration, and where there's an acceleration, there's a change of velocity and that change would be toward the Sun. 

Said a slightly different, way, in order for the apple to stay at distance $R_1$, we'd have to hold on to it:

```{figure} ./../_images/cosmology/applesunhold.png
---
name: applesunhold
width: 350px
align: center
---
That apple wants to move.
```

Isn't this like holding a mass above a table where it really wants to fall and could do work like drive a nail – translating its potential energy into kinetic energy and then to work? 

One thing about our original $U=mgh$ formulation of potential energy is that $U$ depends linearly with the height. That's because near the Earth we treated the *force* of gravity to be constant, so $w=mg$ everywhere. Now we know that's not the case, just that it's a really (really!) good approximation. Newton taught us that the force of gravity actually changes with distance and so the gravitational potential energy will also.

So here we have the same situation. Letting go of that apple will cause it to gain kinetic energy so that were it to strike something in its way – it could translate that kinetic energy into work. Here's what that Gravitational Potential Energy looks like:

$$U(R) = -G\frac{Mm}{R}.$$ (gravpotential)

> **Wait.** Um. A negative sign?

> **Glad you asked.** Good eye. Yes, this requires some discussion and actually becomes a 21st century issue in cosmology.

The gravitational potential energy is indeed negative and here's how we think about it.

Let's reach in and move the apple further away to a distance $R_2$. Would the force the apple experiences be larger than or smaller than at its original position. Of course, smaller. Here's a logical reason to accept that negative sign. Follow along:

* When $R_1 \to R_2$, $F\downarrow,$  gets smaller.
* But if you released the apple at that further distance, it would gain more kinetic energy falling into the Sun than from the original position, so $\Delta K \uparrow.$
* But from Eq.\eqref{gravpotential} the magnitude of $\mid U\mid$ goes down, which is inconsistent with the kinetic energy going up. 
* So $U(R)$  must be negative so that a smaller negative number is translating into a larger kinetic energy.

Here's the way we really think about this. 

Let's pretend (in a mathematic-y sort of way) that we can transport that apple all the way to actual infinity and let go of it. That would mean that $R_{2}\to \infty.$ Now what happens if we just let go of it? From Newtons' Gravitational law,
$$
F=G\frac{Mm}{R_2^2} \nonumber
$$
when $R_2=\infty$ the force is zero. That piece of fruit is now free of the Sun's influence. We'd say that it's "gravitationally unbound." Now if that's not creepy enough for you, let's nudge it.

```{figure} ./../_images/cosmology/applenudge.png
---
name: applenudge
width: 450px
align: center
---
Moving that apple from infinity to just a hair less than infinity.
```

Imagine just gently placing it an infinitesimal distance toward the Sun to $R_3$ just a tiny bit less than $\infty$. While the force wouldn't be much – it's still a long, long way from the Sun – our lonely apple would then feel a tiny force. You know the mantra: if an object feels a force, it accelerates, if it accelerates, it increases its speed, and you can see that it will start to move slowly and then faster and faster (since the force increases at each moment) on its way toward the Sun. 

```{admonition} &nbsp; Pens out!
:class: warning

When we put the apple at infinity, it was unbound from the Sun, so it then has no potential energy which we can see from the gravitational potential form:

$$U(R) = -G\frac{Mm}{R}...$$
Make $R \to \infty$ and we get:

$$U(\infty)=0$$

and it's sitting still at infinity and so it has no kinetic energy;

$$K(\infty)=0.$$

So, what's its total energy, $E_T$?

$$E_T=U(\infty)+K(\infty)=0+0=0.$$

Energy is conserved! So if that's the energy at infinity, then every point after it's nudged should also have zero total energy. Here's the energy conservation relationship for any point (any arbitrary $R$) along the path back to the Sun

$$E_T=0=U(\infty)+K(\infty)=U(R)+K(R).$$

We all agree that kinetic energy is always positive, and so the gravitational potential energy must be...negative. Here how this works in our time-honored, thermometer diagram especially suited for conservation situations. 

````{figure} ./../_images/cosmology/Utherm.png
---
name: Utherm
width: 450px
align: center
---
Kinetic plus Potential energies always cancelling at three different locations away from the Sun to give a total of zero energy at each.

The actual functional forms of these are also instructive:

````{figure} ./../_images/cosmology/UK.png
---
name: UK
width: 450px
align: center
---
Kinetic and Gravitational Potential energies on the same graph...always summing to zero from infinity for each of the positions in the previous plot.

```
