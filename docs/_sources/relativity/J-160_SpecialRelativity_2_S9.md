## Is Relativity the Case?

My friends from particle physics and I use Special Relativity as a tool, so I trust it quite a bit (although there's a story there which I'll tell you at the end of this lesson). But while there were a number of tests that seemed to confirm Relativity, there was one classic experiment in 1963 that puts our conclusions on full display. Let's go to New Hampshire.

### A Bit of the Particle Physics Zoo

This is my rendition of an electron. It's a familiar particle, responsible for the chemistry of all of the members of the periodic table and, as it turns out, is a very light object. It has an electrical charge of $-e$ and perhaps somewhat confusingly, we also refer to it by its nickname, $e$. It has a mass of that's less than 0.1% of that of the proton. We'll have a lot more to say about this particular particle and its cousins.

<img align="left" src="../_images/relativity/electron.png" width=90%/>

<BR CLEAR="all">

<figcaption> An artist's rendition of an electron, sitting still, minding its own business.
</figcaption>

And, here is a cartoon of one of those cousins, another particle called the muon.

<img align="left" src="../_images/relativity/muon.png" width=90%/>

<BR CLEAR="all">

<figcaption> An artist's rendition of a  muon, sitting still, minding its own business.
</figcaption>

This particular object came as a big surprise in the 1940's. It was unpredicted and unwelcome and ushered in an era in which surprises became the norm.

The muon goes by the nickname, $\mu$, and has an electric charge of $-e$, just like the electron. In fact, the muon is *in every way identical to the electron*, except that it's much heavier: $m_\mu = 207 \times m_e$ and about 10% of the mass of a proton.

But one thing about quantum mechanical particles is that they are not long for this world. If there are particles lighter, then heavy particles typically decay into the lighter ones and that's the case for the muon. In about a microsecond and a half, it decays into an electron (and two neutrinos, stay tuned).

<img align="left" src="../_images/relativity/muon_decay.png" width=90%/>

<BR CLEAR="all">

<figcaption> An artist's rendition of a muon which disappears and becomes an electron.
</figcaption>

One other particle player, another particle surprise in the same experiment that found the muon, is the pion, aka $\pi$, which comes as both an electrically charged version and a neutral version. The pion's mass is about the same as the muon's mass...but a smidgen (that's a technical term) heavier. So...yup. It decays also into...maybe you know now, a muon.

<img align="left" src="../_images/relativity/pion_decay.png" width=90%/>

<BR CLEAR="all">

<figcaption> An artist's rendition of a pion which disappears and becomes a muon which disappears and becomes an electron.
</figcaption>

### Cosmic Ray Showers

We're under attack all of the time from above. There are rogue protons barreling through the solar system that randomly bombard our upper atmosphere and undergo staggeringly energetic collisions with the Nitrogen atoms that make up the vast bulk of our air. These collisions produce billions and billions of particles about a third of which become pions and in flight, undergo that chain of decay.  Here's an animation:

```{note}
The story of cosmic rays hitting the Earth. Duck!
<center>
<video width="600"  controls>
  <source src="https://qstbb.pa.msu.edu/storage/QSBB_videos/relativity_temp/relativity_lesson_1.mp4" type="video/mp4">
</video>
</center>
```

Remember that the muon has a lifetime of about 1.5 microseconds. That's its half-life and so its likelihood of decaying on average is 50% after 1.5 $\mu$s. So here's the question:

```{note}
How far would a muon travel on average if it is traveling at the speed of light if its half-life is 1.5 microseconds?
```

This is a simple calculation akin to any constant speed process, so that distance is:

$$
L=v \times t = c \times t = 3 \times 10^8 \text{ m/s} \times 1.5 \times 10^{-6} \text{ s} = 450 \text{ m} \nonumber
$$

From the animation above, maybe you can see that the muons are produced at a height of about 30,000 m above the Earth, so the "number of lifetimes" that any muon would survive all the way to the surface of the Earth before decaying into electrons is about $30,000/450 = 67$. That corresponds to a probability of survival of about 0.00000000000000000000000000011. No muon should make it to the Earth, and yet we're constantly bombarded by muons. About every second, a muon goes through your thumbnail...and every other square centimeter of your body. Day and night, all of your life.

```{admonition}  &nbsp; Wait. How can this be? If they all should have decayed we shouldn’t be hit by any muons!   <br>
:class: warning

**Glad you asked:** That's right. But who's Away and who's Home in the muon's world?
```

As an example, rather than our quick calculation of the muon traveling at $c$ (which is not possible since it has a mass...stay tuned), let's make it a little more realistic and assume that our average muon travels at 90% of the speed of light. So $\beta=0.99$.

Let's think about the Earth as the Home frame. There we see the muon in the Away frame, with an internal clock–its lifetime of 1.5 microseconds– dilated to something much longer. The $\gamma$ plot suggests to me that factor is just about 8:

$$
\begin{align*}
T_H =& \gamma T_A = 8 \times 1.5 \times 10^{-6} = 12 \times 10^{-6} \text{ seconds}
\end{align*}
$$

So the muons would be almost an order of magnitude more likely to reach Earth. [Truth time: The decay is actually an exponential with the time, $N(t) = N_0 e^{-T_Ht}$.]

 So we have two possibilities:

1. The decay of muons according to the space and time physics of Newton and Co.
2. The decay of muons according to Special Relativity, featuring the dilation of the clock of the muon lifetime.

The situation was resolved in 1962 in the : experimenters D. H. Frisch and J. H. Smith went to a lab at the top of Mount Washington in the White Mountain National Forest in New Hampshire, which is about 6280 feet (about 1900 m) above its base. This mountain is notorious for terrible weather with wind speeds of more than 100 mph. One doesn't learn how to do experiments under these conditions in graduate school!

<img align="center" src="../_images/relativity/washington.png" width=90%/>

<BR CLEAR="all">

By measuring the number of muons that hit the top of the mountain and with identical equipment, measuring the number at then base of the mountain they compared the loss from top to bottom with what one would expect from Newtonian time to Relativistic time.

This graph shows their result compared with a simple calculation imagining that 100 muons went past the peak. Basically, if Newtonian time were how our world worked, we should expect that most of the muons that are around at the top of the mountain would have decayed by the surface...about 5 out of 100 would survive. But if Time Dilation is the case, then about 60 muons out of 100 would survive and that's what they measured.

<img align="center" src="../_images/relativity/muon_washington.png" width=90%/>

<BR CLEAR="all">

This is one of the first confirmations of Time Dilation, which is now just a tool in our particle and nuclear physics toolbox. We don't do experiments to confirm Special Relativity now...we trust it and we use it.

Now that we're messing with Space and Time, let's dig deeper into the First Postulate and we'll go back to the airport.
