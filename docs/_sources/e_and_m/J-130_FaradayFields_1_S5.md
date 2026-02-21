## Energy In Electric Fields

Fields are the thing. We’ve established that a positive charge (our test charge) will be repelled by a positively charged vegetable (or, anything, fruit or vegetable), but now it’s really time to drop the language that suggests any direct contact between charges. What matters is only how a charge is influenced by the *fields* in its vicinity -- without regard to how those fields came about. We could create simple field shapes or complex ones, of course by arranging charges or shaping conductors with excess charges in them. We’ll go for “simple” since we can do a lot with that.

Remember our picture of a point-charge's $\vec{E}$ fields pointed radially _out_ from a positive charge and _in_ toward a negative charge. Our drawings suggest that the field is diluted, or less intense the further away from the charge source you look and that sense is conveyed by the fact that there are fewer $\vec{E}$ vectors piercing any equal area the further out you look. That's the beauty of these field drawings since that visual impression is accurate.

That's a relatively complicated geometry, but we just strung a bunch of charges together and created a uniform field. Above, no matter where we are inside the capacitor, the same number of arrows would pierce any area parallel to the plates. Notice that I've put a positive charge (still the broccoli) and a negative charge (my apple is back) in between the plates...what would happen to them?

```{admonition} &nbsp; Pens out 🖊
:class: warning

Well, we expect a force on each and here the force is given by a slight manipulation of $\vec{E} = \frac{\vec{F}}{q}$.  Now we can sing a familiar little song:

- when there’s a force, there’s an acceleration.

- When there’s an acceleration, the velocity changes.

- If the velocity changes, then the kinetic energy changes.

Not very catchy, but you'll see the point. Remember the definition of the electric field in terms of a charge that senses it and the force that it experiences:

$$\vec{E} = \frac{\vec{F}}{q}$$

which if we turn it around to represent the force:

$$\vec{F} = q\vec{E}.$$

This reminds us that a positive charge will experience a force that is oriented along the electric field direction. Let’s set up a fake-unit situation.  I've brought the broccoli out of retirement and charged it positively to $q_B=+2$. You've been wondering where the apple has been and so you're relieved to see that it's playing a new role, that of a negative charge of $q_A=-4$ (forgetting units). So $\vec{F_B}=+2\vec{E}$ and $\vec{F_A}=-4\vec{E}$ where the negative sign obviously reminds us that this force is in the opposite direction of the other one ("positive" setting the direction).
```

```{admonition} &nbsp; Pens out 🖋 📓 
:class: warning

Please study Example 2:
[Forces on produce:](./../examples/EandM/example_vector_forces_1.html)
```

This is the important question: which charge will gain the most kinetic energy? Normally, we would have expected the mass of the accelerated object to matter. Does it here?

```{admonition} &nbsp; Kinetic Energy of Electric Charges In An Electric Field 🖋 📓
:class: warning

How much kinetic energy does an electric charge gain when it's placed in an electric field? Assume that it starts from rest and placed in the center of the capacitor above. Also assume that they don’t interact with each other. Finally, assume that the kinetic energies are compared after they have both moved a distance, $d$ from the center.</h3like><br>

Here’s how to think about this:

$$\vec{F} = q\vec{E}$$

gives us a constant force. From Newton’s Second Law, we can calculate the constant acceleration that would result...in terms of the mass of each charge. From one of our kinematics equations ($v^2 = 2ax$) we can calculate the speed-squared. Then from there, it’s a simple move to calculate the kinetic energy, $K=1/2mv^2$. Okay? Here we go:

String together Newton’s Second Law with our electric field force, and solve for the acceleration, $a$ in terms of the mass of the positive charge, $m_p$:

$$ \begin{aligned} F &= m_pa = qE \nonumber \\             
a & =\frac{qE}{m_p} \nonumber \end{aligned}$$

Now find the speed squared from $v^2 = 2ax$ after it’s gone through a distance, $d$:

$$v^2 = 2ax = 2\frac{qE}{m_p}d$$

And now determine the kinetic energy,

$$\begin{aligned}
K   &= 1/2 mv^2 = \frac{1}{2}m_p\left( 2\frac{qE}{m_p} \right)d \nonumber \\
K   & = qEd \label{parallelenergy} \end{aligned}$$

See how the mass cancelled? Since the positive charge is half in magnitude of the negative charge, then the kinetic energy of the negative charge will be twice that of the positive.

```

```{admonition} &nbsp; Pens out 🖊 📓
:class: warning

Please study Example 3:
[Kinetic energies of produce:](./../examples/EandM/example_KE_1.html)
```

This is an important conclusion. For our constant electric field, the kinetic energy acquired by electric charges depends only on the charge and not the mass of the object! For example an electron would get the same kinetic energy boost than the much heavier proton. Here,  the kinetic energy of the charges comes from the force, but the force comes from the field. We conclude that fields carry energy...we could say that

>Electric fields store energy and can do work on electric charges.

If a circumstance can create a kinetic energy, it's reasonable to think of a potential energy that enables it and that's the case here. For example, the term “voltage” comes in relating the work done on a charge in an electric field. When you deploy a battery in your flashlight, you’re arming it to supply energy to electrons to force them through the circuit and the higher the voltage rating, the more current you can supply.

```{admonition} &nbsp; Pens out 🖊
:class: warning

It's useful to think about the energy that _could_ be expended in moving a charge, and that’s just the electrical potential energy, $U$. So the kinetic energy we found above, $K = qEd$ can be more conventionally recast as: A particular arrangement of electric charge will change how $U$ relates to $E$:

$$U=qEd,$$

which is just a force ($qE$) times a distance ($d$), like we first learned.

"Voltage" is then the potential (energy) _per unit charge_ with units of Volts (V), or Joules/Coulomb. So

$$ 1\text{ V} = 1 \text{ J/c}.$$

The form of the voltage, or $U$ depends on the configuration of the electrified plates that create the field. For this simple arrangement of parallel flat plates,

$$\text{from } U=qEd, \text{ we get } V=Ed$$

which in turn leads us to the more practical measure of Electric Field of “Volts/meter,” which is pretty much universally used in engineering. (But from the original definition of the field, $E=F/q$, “Newton’s per Coulomb” is another, perfectly acceptable unit for the field). Here are some typical electric fields that you might encounter.

| Source                                      | Electric Field Strength, V/m Comments |                                              |     |
| ------------------------------------------- | ------------------------------------- | -------------------------------------------- | --- |
| atmosphere                                  | 100-150                               | near the surface of the Earth                |     |
| home background                             | <100                                  | typical home                                 |     |
| inside your grandparents' TV tube           | 40,000                                |                                              |     |
| near an electric blanket                    | <1,000                                | in typical use                               |     |
| near a microwave oven                       | 600                                   |                                              |     |
| near a cell phone                           | <50                                   | <0.1 inside your body just below the surface |     |
| below a huge 500~kV power distribution line | 10,000/m                              | some states restrict to 3-5 KV/m             |     |

```

Let’s put this together.

```{admonition} &nbsp; Pens out 🖋 📓 
:class: warning

Please study Example 4: [Energy in your parents' old TV:](./../examples/EandM/example_TV_1.html)
```

All of that voltage for just a tiny bit of kinetic energy in each electron? There are lots and lots of electrons!

```{admonition} &nbsp; Please answer Question 3 for points 🖥️ :
:class: danger
[Charge trapped between plates](https://loncapa.msu.edu/tiny/msu/psQ0Hf)
```
