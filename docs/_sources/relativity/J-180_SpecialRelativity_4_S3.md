## The Rubber Meets the Road: Particle Creation and Potential Energies

In our lesson on energy we learned to represent energy conservation as

$$
E_{T (\text{before})}=K_0 + U_0 = K + U = E_{T (\text{after})}\nonumber
$$

Kinetic plus potential energies before...must equal kinetic plus potential energies after some event. That potential energy term was always a little squirrelly – like it was added to make things work.

Let's imagine a football tackle. Player $1$ runs at player $2$, tackles him, and they stick together forming a new, single object "$12$." The masses of the two players are identical and their speeds are equal.

<img align="left" src="../_images/relativity/tackleR.png" width=90%/>

<BR CLEAR="all">

```{admonition}  &nbsp; Pencils Out! 🖋 📓
:class: warning

What would a physics student have calculated in 1904? First, she would have said that momentum was conserved:

$$
\begin{align*}
p_{1,0} - p_{2,0} =& p_{12} = 0 \text{, so} \\
p_{1,0} =& - p_{2,0} \\
mv_1 =& - mv_2 \text{ which, since their masses are identical,} \\
v_1 =& -v_2 \text{ so, call each of them just }v = |v_1|=|v_2|
\end{align*}
$$

And she would have conserved energy:

$$
\begin{align*}
K_{1,0} + K_{2,0} =& K_{12}=0 \\
\frac{1}{2}mv_1^2 + \frac{1}{2}mv_2^2 =& 0 \text{, which, since their masses are identical,} \\
& \text{   and since the $v's$ are identical}\\
v_1^2 + v_2^2 =& 2v^2 = 0
\end{align*}
$$

which doesn't make any sense. At this point her professor would mumble about energy lost in heat, the springiness of the two objects causing compression and then a release of that compression by heating and moving the air, which we'd hear as sound...and so on and so on. That is, this completely inelastic collision would conserve total energy, but we would have written it like this:

$$
\begin{align*}
E_T =& K_{1,0} + K_{2,0} = K_{12} + E(\text{lost}) \\
E_T =& K_{1,0} + K_{2,0} = 0 + E(\text{lost}) \\
E_T =& K_{1,0} + K_{2,0} = E(\text{lost, heat, sound, elastic compression, yadda yadda yadda})
\end{align*}
$$

Now let's suppose it's early 1906 after Einstein's realization, and the collision is a for  *relativistic football tackle*.

```

```{admonition}  &nbsp; Pencils Out! 🖋 📓
:class: warning

In Special Relativity, we would now write:

$$
\begin{align*}
E_{T (\text{before})} =& E_{m, 1 (\text{before})} + K_{1 (\text{before})} + E_{m, 2 (\text{before})} + K_{2 (\text{before})}\\
=& E_{m, 12 (\text{after})}+K_{12 (\text{after})} = E_{T (\text{after})}
\end{align*}
$$

Total energy is still conserved, but how it arranges itself between energy of mass ($E_m$) and energy of motion ($K$) changes.

Now, momentum is still conserved, so the combined objects, 12, stop dead (no pun intended...but if it's relativistic, they're moving pretty fast!). That means that  $K_{12 (\text{after})}=0$ and we now have:

$$
\begin{align*}
E_{T (\text{before})} =& E_{m, 1 (\text{before})} + K_{1 (\text{before})} + E_{m, 2 (\text{before})} + K_{2 (\text{before})}\\
=& m_1c^2 + K_{1 (\text{before})} + m_2c^2 + K_{2 (\text{before})} = m_{12}c^2
\end{align*}
$$

Let's rearrange this a little:

$$
\begin{align*}
E_{T (\text{before})} =& m_1c^2 + m_2c^2 + K_{1 (\text{before})}  + K_{2 (\text{before})} = m_{12}c^2 = E_{T (\text{after})}
\end{align*}
$$

which is different from the 1904 calculation. Remember, there we found that

$$
K_{1 (\text{before})}  + K_{2 (\text{before})} = 0 \text{ in 1904} \nonumber
$$

and that's now not the situation. In fact,

$$
K_{1 (\text{before})}  + K_{2 (\text{before})} >0 \nonumber
$$

and so

$$
m_{12}c^2  > m_1c^2 + m_2c^2 \text{ ! in 1906} \nonumber
$$

```

The combination of the two moving objects is more massive when they collide than they were separately, before they collided. All of that mumbo jumbo about leftover energy can be interpreted as a mass increase: the energy of motion has become additional energy of mass. Said, another way:

$$
\begin{align*}
\text{before 1905, nobody would have disputed that: } &m_{12} = m_1 + m_2 \\
\text{after 1905, we must assert that : } &m_{12} > m_1 + m_2
\end{align*}
$$

```{admonition}  &nbsp; Mass + Energy is the thing  <br>
:class: important

Mass, by itself, is not conserved. Mass energy plus energy of motion is always conserved.
```

### Particle Physics: the sum is worth more than the parts

One of the discoveries in particle physics that I was involved in was the discovery of the most massive elementary particle we know of: the "top quark." We'll learn all about that later, but what's relevant here is that we collided protons with the antiparticles of protons. Antiparticles are identical to their particle counterpart, except they have the opposite electrical charge. So they have the same mass.

Remember that I said I'd sometimes refer to the mass of a proton as "1" in dimensionless units? This will be more of an issue in later lessons, but some nomenclature:

```{note}
* Antiparticles will be written with a "bar" over the top.
* So an electron is $e$ and an anti electron would be $\bar e$. (It's so useful in medicine and other areas of life that it has a name: the positron.)
* A proton is $p$ and so an antiproton is $\bar{p}$.
* A top quark is $t$ and ...you get it, right? The anti-top quark is $\bar t$.
```

Here's where relativity is useful as a tool. Our top quark discovery reaction was:

$$
p + \bar{p} \to t + \bar{t}. \nonumber
$$

Here's a cartoon, where the "before" is at the top, then the physics of annihilation and creation is some very short time later (middle) and the two top quarks are the result, at the bottom.

<img align="left" src="../_images/relativity/ttbarcartoon.png" width=90%/>

<BR CLEAR="all">

Here's a kind of surprising fact:

$$
\begin{align*}
m(p) = 1 \\
m(\bar p) = 1 \\
m(t) = 173 \\
m(\bar t) = 173
\end{align*}
$$

So if you add up the masses in the initial state of the colliding proton-antiproton set you get $m(\text{before})=2$ and the masses of the resulting top-quark pair, $m(\text{after}) = 2 \times 173 = 346!$

That's why we must accelerate the protons and antiprotons to very, very high energies – so that the energy of motion in the beams can be turned into energy of mass in the final products. Sweet.

Here's a colorful model for the collision of two objects into two objects:

```{admonition} &nbsp; Pencils Out! 🖋 📓
:class: warning

<img align="left" src="../_images/relativity/twototwo.png" width=90%/>

<BR CLEAR="all">

```

Look at each term carefully. Because we're going to create new matter.

Let's make a cartoon particle accelerator, in the spirit of the Large Hadron Collider in Geneva. Two protons are accelerated around a huge, evacuated pipe (steered by magnets and accelerated in electric fields as we've discussed). In this play-accelerator, they are brought together in one place where they collide.

1. At the top, we see them coming toward one another
2. At the bottom they've disappeared and created two, new...things, $t$. The things are much more massive than the original protons.

```{admonition}  &nbsp; Wait. Disappeared? Like Beam me up, Scotty?   <br>
:class: warning

**Glad you asked:** Not quite and as maybe you've heard me say before, stay tuned. We will talk about that when we get to quantum mechanics where the explanation is both beautiful and weird.
```

<img align="left" src="../_images/relativity/thing12.png" width=90%/>

<BR CLEAR="all">

Here is the reaction formula for a proton from the Left colliding with a proton from the Right to make two "things," $t(1)$ and $t(2)$:

$$
p(L) + p(R) \to t(1) + t(2). \nonumber
$$

Feynman Diagram for the process:

<img align="left" src="../_images/relativity/FD_things.png" width=60%/>

<BR CLEAR="all">

```{admonition}  &nbsp; Wait. What happens in the gray blob?  <br>
:class: warning

**Glad you asked:** That's a quantum mechanics model that we'll get to. Stay tuned. Sorry.
```

```{admonition}  &nbsp; Pencils Out! 🖋 📓
:class: warning

Here are the ground rules for this game. Although energies would typically be Joules, or electron volts, we'll just use fake energy units scaled to the mass-energy of a proton.

$$
\text{Mass energy of a proton } = E_m = m_pc^2 = 1 \nonumber
$$

The mass of a "thing" is big:

$$
\begin{align*}
\text{Let's assume that the mass of 1 thing } =& 3.5\times m_p \\
\text{So, the mass-energy of 1 thing } =& 3.5 \times 1 = 3.5\\
\end{align*}
$$

Nature only produces pairs of "things" so the minimum mass-energy required to create two things is:

$$
\text{Mass energy of two things } = 2 \times 3.5 = 7. \nonumber
$$

Finally, the protons are moving – fast. So there's kinetic energy in their motions of three times the mass-energy of a proton:

$$
\text{Let's assume that the kinetic energy of each proton } = 3 \times m_pc^2 = 3 \nonumber
$$

From our energy conservation equation we can keep track of the before energies and the after energies:

$$
\begin{align*}
E_T(\text{beam protons} =& \text{ Mass energies } + \text{ kinetic energies} \\
E_T =& 2 \times m_pc^2 + 2 \times K \\
E_T =& 2 \times 1 + 2 \times 3 = 2 + 6 = 8
\end{align*}
$$

The question is whether there is enough total energy in the beam protons to be able to make two "things" in the collision.

You'll need a worksheet that you'll find on-line in the course pack. It looks like this:

<img align="left" src="../_images/relativity/particle_collision_blank.png" width=90%/>

<BR CLEAR="all">

Let's add it up:

Let's imagine a chart on a whiteboard. Here is the total mass-energy of the two beam protons:

<img align="left" src="../_images/relativity/justmass.png" width=90%/>

<BR CLEAR="all">

The vertical axis will tally energies of each of the objects scaled in units of our fake units of $m_pc^2$:

1. The mass-energies of each proton.
2. This totals to 2.
3. The total mass-energy required in order to make two things is $2 \times 3.5 = 7$.

Now let's add in the kinetic energies:

<img align="left" src="../_images/relativity/massKandtotal.png" width=90%/>

<BR CLEAR="all">

4. Each beam proton had $K=3$ .
5. So the total of the beams' energies of motion is 6.

Putting it all together:

6. The kinetic energies plus the total mass energies of the protons
7. totals to 8.

As you can see, we needed $E_T = 7$ but the collision provided a total energy of $8$, more than required in order to just make two things.

```{admonition}  &nbsp; Wait. So what happens to the extra energies?  <br>
:class: warning

**Glad you asked:** The things are not just hanging around after they're produced. There is energy left over after they are created as real particles...and so they're moving. They acquire some kinetic energy.
```

The two, shiny new "things" have kinetic energies of their own of $K_\text{things} = 1$.

What we just did is solve the energy conservation equations:

$$
\begin{align*}
E_{T,0}(p, L) + E_{T,0}(p, R) =& E_{T}(\text{thing 1}, L) + E_{T}(\text{thing 2}, R) \\
E_T = 2 \times m_pc^2 + 2 \times K_p =& 2 \times m_tc^2 + 2 \times K_t \\
2 \times 1 + 2 \times 3 =& 2 \times 3.5 + 2 \times K_t \\
2 + 6 =& 7 + 2K_t \\
2K_t =& 8-7 = 1
\end{align*}
$$

A lot of relativity is pretty elementary math.

That. In a nutshell is much of the goal of particle physics: make new things by using relativity (and quantum mechanics) out of very fast old things.

```{admonition}  &nbsp; Please answer question 4  📺
:class: danger

<a href="https://loncapa.msu.edu//tiny/msu/c53cQ2"  target="_blank">Making new things</a>
```


### Some Chemistry: as viewed by a physicist

Remember the hydrogen atom is one proton and one electron and that electron and proton are bound together by the electrostatic attraction due to their opposite electronic charges. Maybe you remember from chemistry that in order to liberate the electron – to "ionize" hydrogen, you must supply a particular minimum energy of 13.6 electron volts or $2.18 \times 10^{-18}$ J.

You would have learned that the electron is "bound" to the proton with a potential energy that's negative. The energy diagram would look like this in a chemistry class on the left and a physics class on the right:

<img align="left" src="../_images/relativity/hydrogenCP.png" width=90%/>

<BR CLEAR="all">

Let's look at each item here by the circled numbers in the diagram.

The left side, the chemist picture:

1\. The hydrogen energy level diagram is a succession of energy levels from the lowest – which is the most stable – to the highest, which is complete ionization....liberation of the electron.

2\. For chemists, the zero of energy is when the electron has been liberated...that's zero chemical energy.

3\. When the electron is bound, it has a negative electrostatic potential energy of $-13.6$ electron volts.

4\. Give an electron a hit of $+13.6$ eV (like from a photon), and it will be promoted away from the proton and is no longer bound: it's a separate proton and a separate electron.

The right side, the physicist picture:

5\. For the physicist the zero of energy is where there is no motion and there is no mass.

6\. For hydrogen, the energy is all in the mass of the hydrogen <u>atom</u>.

7\. For a real proton and a real electron, which are not bound together into an atom, the energy is just $m_pc^2 + m_ec^2$. Notice that this value goes to the zero value of the chemist picture: an independent and isolated proton and electron.

Why does the electron stay bound to the proton in hydrogen in the relativistic picture? Because the mass of a hydrogen atom is less than the mass of an electron and a proton. So it cannot just rattle apart into those two particles since

$$
E_m(\text{hydrogen atom}) < E_m(\text{real proton}) + E_m(\text{real electron})! \nonumber
$$

So how to reconcile this? Remember that what's not in the picture is the electric field.

* We know from Maxwell that the electric field has energy.
* We know from Einstein that energy and mass are equivalent.
* So the "missing mass" in the hydrogen atom is resident in the energy of the electric field.

It's all accounted for!


<img align="left" src="../_images/relativity/hydrogenbalance.png" width=90%/>

<BR CLEAR="all">

Since, after all, energy is mass and mass is energy. This same idea is what happens inside of nuclei and that "mass deficit" can be liberated, either in a controlled way – nuclear power – or an explosive way – nuclear weapons.

Everything you've learned about energy can be cast in this light. Potential energy can be done away with:

* Raise a mass above the ground? You increase its mass. That's what we've called potential energy.
* Heat up your eggs in the morning? They become more massive. The jiggling of the molecules in the eggs which we would call heat, can be interpreted as an overall increase in the eggs' mass.

Energy suddenly becomes a simple idea! And, it's always conserved...as long as mass-energy is included in the accounting.

```{admonition}  &nbsp; Please answer question 5  📺
:class: danger

<a href="https://loncapa.msu.edu//tiny/msu/f98qlQ"  target="_blank">Potential energies? Nah.</a>
```
