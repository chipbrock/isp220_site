## The Lorentz Force, Broken Down

Let's go back to the forces between two wires carrying currents and let's break it down to the actual particles involved in a current and the magnetic field that they produce. 

Remember that we saw that two parallel wires carrying current in the same direction would feel a force of attraction and physically move. Now we're going to understand why. Here we're concentrating on the force that wire B feels due to current A, $F_{BA}$. 

```{figure} ./../_images/EandM/twowires.png
---
name: twowires
width: 450px
align: center
---
```

This example will walk you through this:

```{admonition} &nbsp; Please study Example 2: 🖋 📓
:class: warning

<a href="./../examples/EandM/example_lorentzforce_1.html" target="_blank">The Lorentz force explains the force between current-carrying wires </a>

```

### Charged Particles in the Presence of Electric and Magnetic Fields

When an electric charge is in the presence of an electric field, as we know it experiences a force along the direction of the E field lines if it’s a positive charge, and against the direction of the field lines if it’s a negative charge. So in this figure the positive charge goes up and the negative, down.

```{figure} ./../_images/EandM/capcharges.png
---
name: capcharges
width: 450px
align: center
---
Magnetic fields are different. If you put an electric charge in a magnetic field…nothing happens. That stymied Faraday until he moved the magnetic field relative to the charges in a current loop–which is the same thing as moving an electric charge in the presence of a stationary magnetic field. Then, it feels a force.
```

Let's build a magnetic field distribution without worrying how we do that (stay tuned). Here in (a) we have a magnetic field that’s pointing up and extending out at you and into the screen–it’s in three dimensions. We’re looking at it with the B field arrows pointing right at us. In (b) we’ve changed our vantage point so that the B field lines point into the screen right toward us. Get the picture?

```{figure} ./../_images/EandM/capcharges.png
---
name: pile
width: 450px
align: center
---
```

Now let’s shoot a positively charged particle into that B-in oriented field so that its velocity is pointing to the right. 

```{figure} ./../_images/EandM/bfirstbend.png
---
name: bfirstbend
width: 450px
align: center
---
It feels a force, but perpendicular to both the field and its velocity–**it bends**! In this case up. That’s what magnetic fields do to electric charges. It bends their trajectories–the charge has to be moving and then it’s susceptible to a bending force.
```

> An electric charge which is moving relative to a magnetic field will experience a force which is perpendicular relative to its velocity and the direction of the magnetic field.

The value of the force is an important calculation if you build particle accelerators (or old-time TV sets). We’ll only need to know how to determine the *direction* of the bend.

The relevant quantities to determine this are the three vectors: $\vec{v}$, $\vec{B}$, and $\vec{F_M}$ (the magnetic force) and the electric charge sign, $+$ or $-$. This is a job for vector algebra, for which we’ll need a hand. In particular your right hand and this is another application of a “right hand rule."

```{figure} ./../_images/EandM/righthandrule1.png
---
name: righthandrule1
width: 450px
align: center
---
There are a couple of ways to use your right hand to figure out the direction of a force and the order of $\vec{v}$, $\vec{B}$, and $\vec{F}$ are important. Here’s probably the easiest one of…–dare I say a “handful” of right hand rules. Take your right hand and its index finger pointing out. Take your second figure and make it go perpendicular to your index finger (it only bends one way, unless you’re built strangely), and then extend your thumb in the only direction that it can go.
```

* Your index figure is the $\vec{v}$. 
* Your second finger is the $\vec{B}$.
* Your thumb points in the direction of the resulting $\vec{F}$.

Look again at the bending charge that we just sketched, now with some assistance. Notice that the **B** field direction is in, so the third finger is pointing into the screen.

```{figure} ./../_images/EandM/bendinghand.png
---
name: bendinghand
width: 450px
align: center
---
You might need to play with this a little. If you do it on the bus, people will stare, but try to look at both the perspective figure and the from-the-top figure and confirm that the force is where your thumb wants it to be.
```

So now we have what’s called the “Lorentz Force.” It’s the combination of the force on a charge experiencing an electric field and the force on a charge experiencing a magnetic field.

$$
F=q\vec{E} + q\vec{v} \times \vec{B}
$$

That $\times$ sign symbolizes the very special kind of multiplication of vectors called a “cross product.” For us, that’s just saying, “get out your right hand and do the thing with your three fingers!” In order: $\vec{v}$ then $\vec{B}$.

Suppose this had been an electron, so that the charge was opposite of that proton? Then the force would point in the other direction since the electrical sign will become a vector sign.

```{admonition}  &nbsp; Wait. Then what about the current, doesn’t that mean that the wires will separate?  <br>
:class: warning

**Glad you asked:** Remember that if we think about the current as an actual wire-carrying-electrons situation not only does $q$ become negative, but also the velocity changes direction so that the overall sign is the same as what we constructed. Good question, though.
```

Now we can build a particle accelerator. We start with protons or electrons (or nuclei) and inject them into a region of an **E** field. That accelerates them. They leave the accelerating region and enter a carefully crafted magnetic field region designed to bend the particles in the direction of an experiment. 

```{figure} ./../_images/EandM/accelerator1.png
---
name: accelerator1
width: 450px
align: center
---
Can you see that the bending of that beam of protons would be to the left, A?
```

Now we understand the Aura Borealis, the “Northern Lights.”

```{figure} ./../_images/EandM/aura.png
---
name: aura
width: 450px
align: center
---
The Earth’s magnetic field is concentrated at the north and south poles. It’s necessary for our survival because our Sun can be an angry neighbor. The charged particles near the surface of the Sun have varying speeds and some small fraction of the protons and electrons at that surface actually are above the escape velocity and off into space they go–this is the “Solar Wind.” The Sun’s solar storms can send whole swarms of charged particles that our Earth’s path might intersect.
```

But those charged particles get trapped in the **B** field lines of the Earth and spiral (that’s the $v \times B$  bending at work) toward the pole. As the field gets tighter near the pole the rotational speeds of the particles increase enough to excite the Nitrogen and Oxygen in the upper atmosphere which, when they de-excite emit light, green for Oxygen and blue and red for Nitrogen.
