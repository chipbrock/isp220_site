## Maxwell’s Insight and Electromagnetic Waves

Let’s look at basically what bothered Maxwell. First, remember that a current, which means a changing electric field, is generated when a magnetic field changes in time. That’s the current loop above, where the electrons in the wire move because of the magnetic-field-induced electric field pushing them.

Let’s look at two metal plates that are connected to wires in a circuit. Maxwell thought of the region between the plates as consisting of actual non-conducting material (called a dielectric) and the whole device is a circuit element called a capacitor, about which we’ll have more to say below. For now let’s just be simple–by even more strangely imagining that there’s nothing between the plates. 

Here’s the picture: a battery, a switch that’s closed, and our plates. Simple, but odd as we watch what happens as time passes.[^2]

In the top figure, we close the switch and current begins to flow. Remember:

* the convention is that current flows from the positive terminal of a battery to the negative. The arrows signify that.
* in actuality, the actual current is electrons in the wire which are repelled by the negative terminal of the battery and go in the opposite direction of the conventional current. I'm just the messenger. Blame Ben F.

In the bottom figure, you can see that the flowing current creates a circular magnetic field around the wire with the direction indicated. 

[^2]: This is not a realistic circuit because it would lead to smoke and melt something. Let's pretend that the wire itself has a significant electrical resistance! 

```{figure} ./../_images/EandM/displacement_noplate_v.png
---
name: displacement_noplate_v
width: 450px
align: center
---
At the top, a switch is open and no current flows. At the bottom, the switch is closed and the current creates a magnetic field circulating around the wire throughout.
```

Now let's add a circuit element to the picture, namely two metal plates and a gap between them...called a capacitor. We can collect charge on a capacitor by connecting it across a batter like shown. In the bottom figure, the switch has been closed and current starts to flow. But:

* There's a gap! So charges don't flow from P2 to P1 (unless it sparks, which is an unwanted current in most circuits!)
* So we see that the charges in the whole circuit start to arrange themselves so that electrons build up on P2 and leave P1...leaving an overall positive charge on P1.

```{figure} ./../_images/EandM/displacement_nope.png
---
name: displacement_nope
width: 450px
align: center
---
Now a circuit is interrupted by two parallel, metal places and a switch. The plates are a circuit element called a 'capacitor' used to store charge. In the top the switch is open and nothing happens. Then the switch is closed and the bottom figure shows what starts to happen. As current flows, a magnetic field develops where current is flowing. That current is interrupted by the plates which begin to store charge on their surfaces.
```

On can picture the electrons building up on the right hand plate (Remember the current flows in the opposite direction of get actual conducting electrons. Thanks, Ben.) and how the left hand plate is robbed of electrons and becomes positive. 

* This charge build-up happens over time. 

Look at the situation below as time goes on. We start from no current and no voltage across P2-P1 ($V_P$). Then after the switch is closed, current starts to flow and that charge build-up happens...a little (lower left)...and then more...lower right. At each of these two stages, the voltage builds on the plates and the electric field between them gets stronger and stronger.

Notice how unsatisfying this magnetic field is: it just goes blank at the edges of the plates. It's discontinuous and in some sense Maxwell found that his model would fix that!

```{figure} ./../_images/EandM/displacement_E.png
---
name: displacement_E
width: 450px
align: center
---
This is the same situation as in the previous figure, but in the bottom two sketches, the electric field is shown developing between the plates. As more current is delivered, the magnetic field gets stronger and the electric field (confined to between the plates) gets stronger. A voltage develops across the plates getting bigger as more charge is deposited.
```

Let's continue to let the current flow and come back to that unpleasant gap of magnetic field.

The top figure below is just before the voltage across the gap matches that of the battery. When than happens, that balance means that there's no incentive for the electrons to flow and:

* the current stops flowing
* $V_P=V_B=1.5 \text{ V}$ 
* and without a current, the magnetic field goes away and we've got a stable situation.
* But: there's now a static electric field left between those two plates.

```{figure} ./../_images/EandM/displacement_BE.png
---
name: displacement_BE
width: 450px
align: center
---
But the discontinuity of the magnetic field is bothersome and Maxwell's model responded. There is a magnetic field between the plates also as suggested in the top. Eventually the charge deposited on the plates leads to a voltage across the plates that's equal to the battery voltage. When that happens, the current stops flowing: the magnetic field disappears and the electric field remains.
```

Now about that strange discontinuity of the magnetic field. Look at Maxwell's mechanical picture again:

```{figure} ./../_images/EandM/maxwell_model.png
---
name: maxwell_model
width: 450px
align: center
---
Maxwell's mechanical model again, showing little currents that that are not flowing inside of wires: like P-q.
```

Notice that there are other idler spheres that are not connected to any external circuit in this model. They are not "real" currents and don't actually transmit real electrical charges–but the act like little currents. Maxwell called them "displacement currents" and proposed that between those plates, they were in action:

* although no currents actually transmit charges, there is an effective–even "fictitious" current called the "displacement current," $i_d$. 
* if you've got a current, then you've got a magnetic field! And so he preserves the continuity of the magnetic circular fields through the gap by pretending that there's a strange, displacement current.

```{figure} ./../_images/EandM/displacment_current.png
---
name: displacment_current
width: 450px
align: center
---
Maxwell posited the existence of the 'displacement current' that flows without actual charge exchange between the plate. As a 'current' it might generate that missing between-the-plates magentic field. But it's more concreted to tie the existence of the magnetic field to the changing E field and not to the displacement current.
```

But what's really going on is that there's that changing electric field between the gap:

* That **E** changes as the current charges up the capacitor 
* It's responsible for the displacement current
* which is responsible for the (changing) **B** field 
* But why not just get rid of the middleman, that displacement current?

It's the changing **E** field that creates that inter-gap <u>changing</u> **B** field. 

Now, he’s added to the picture: not only does a changing magnetic field create an changing electric field, but a changing electric field creates a changing magnetic field.

He had 20(!) equations, each of which described the four phenomena listed at the beginning of this discussion. But they were asymmetric originally with a changing magnetic field featuring prominently in #3. Now, there’s a corresponding changing electric field creating its partner magnetic field in #4.

This makes the sum total of that set of equations have solutions which were familiar to all physicists of his and our time. These solutions are waves. There is a solution that describes a time-waving electric field and another one that describes a time-waving magnetic field. 

And. They are linked together. One of them creates the other…and the other creates the former:

* A changing **E** field creates a changing **B** field

* which in turn creates a changing **E** field

* which in turn creates a changing **B** field

* which in turn creates…and so on

This is an electromagnetic wave and the velocity at which that wave propagates is:

* perpendicular to the directions of the two perpendicular **E** and **B** vectors
* and has the magnitude of $c = 3 \times 10^8$ m/s

This is what Weber missed. His speed had no physical interpretation. Maxwell provided the missing piece…and then he took away the “scaffolding” of the mechanical spinning balls and let the equations stand on their own.

```{admonition}  &nbsp; Maxwell, in his 1864: A Dynamical Theory of the Electromagnetic Field  <br>
:class: important

"The agreement of the results seems to show that light and magnetism are affections of the same substance, and that light is an electromagnetic disturbance propagated through the field according to electromagnetic laws."
```

His 20 equations were made more succinct by Oliver Heaviside into four vector differential equations which all physicists and engineers revere as “**Maxwell’s Equations.**” 

That Maxwell's Equations predicted waves with a speed equal to the measured speed of light meant that light is composed of electricity and magnetism. 

```{note}
Maxwell’s equations unified optics, electricity, and magnetism into a single model of nature: Electromagnetism.
```

His death at the age of 48 in 1879 was tragic for his family and friends, but also a depressing conclusion to the Maxwell story. The distinct prediction of electromagnetic waves was to await confirmation until 1887, less than a decade later. After two years of work, the young, but brilliant Heinrich Hertz (for whom we name the frequency of wave motion), was able to detect the wavelike nature of radiation from sparks (which are visibly bright, but also “bright” in other wavelengths) and actually measure the wavelength of the light that traversed the length of his lab. Hertz himself was to die tragically at the age of 36.

What Hertz confirmed was that an electromagnetic wave is a coupled arrangement of mutually-inducing oscillations of magnetic and electric fields moving together at the speed of light. Here's a cartoon:

```{figure} ./../_images/EandM/armswaving.png
---
name: armswaving
width: 450px
align: center
---
The mutual creation of electric and magnetic fields---one changes in time creates the other changing in time, which in turn, creates the first...and so on. All from the solutions to Maxwell's Equations.
```

The electromagnetic wave is moving to the right. You can see the oscillating fields, E up and down and B in and out. The Changing **E** field creates a changing B field...and that changing **B** field in turn creates its partner changing **E** field...and so on and so on. Furthermore, their magnitudes are related:

$$
\frac{E}{B}=c \nonumber
$$
