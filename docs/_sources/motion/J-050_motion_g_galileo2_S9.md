## Acceleration, In Everyday Terms

So far we've treated acceleration descriptively: it's when velocity increases (or decreases) over time. Let's put this on a more firm footing by defining acceleration as a rate just like we defined velocity:

```{admonition} &nbsp; Pens out!
:class: warning

$$a = \frac{\Delta v}{\Delta t}=\frac{v-v_0}{t-t_0}.\label{acceleration}$$

This is another quantity that you're well acquainted with…after all, the pedal by your right foot is the "accelerator." In that spirit remember that a standard measure of manliness is ownership of a muscle-car capable of  "0 to 60" (mph) in a short period of time: the everyday epitome of an acceleration, from one speed (0) to another speed (60 mph). The units are little odd, as maybe you noticed with $g$. Let's race.

If you own, say, a Mitsubishi Mirage ES, it will take you around 12 seconds to get to sixty from rest. If you own a Porsche 911 Carrera S, it will take you closer to 4 seconds. From our definition we can quote the acceleration of the Mitsubishi as

$$\begin{align}a &=\frac{\Delta v}{\Delta t} \nonumber \\ &=\frac{60 \text{ mph}-0\text{ mph}}{12\text{ seconds}-0\text{ seconds}} \nonumber \\ &=5 \text{ mph per second} \nonumber \nonumber \end{align}$$

That odd double time unit, miles per hour per second, shows you that this is a rate...of speed change. If you start from a standing start in your Mitsubishi then after 1 second you will have reached 5 mph and after 2 seconds, 10 mph. Every second, your speed will increase by 5 mph.

While this "mph per second" unit makes it plain, it's not what we would usually say. In physics, we'd convert to a single unit of time and then square it. I'll do this once and then we'll use Mr. Google for unit-conversion in order to convert from one unit to another without the drudgery of forming all of those ratios.

Let’s convert 5 mph into miles per second: <br>

$$\begin{align} X \frac{\text{miles}}{\text{second}} &= 5 \frac{\text{miles}}{\text{hour}}\times \frac{1 \text{ hour}}{60 \text{ min}} \times \frac{1 \text{ min}}{60 \text{ sec}}  \nonumber \\
&= 5 \frac{\text{miles}}{\text{second}}\times \frac{1}{3600} \nonumber \\
&=1.3 \times 10^{-3} \text{miles/s} \nonumber
\end{align}$$

So our acceleration is $1.3 \times 10^{-3} \text{miles/s}^2$

```

> **Wait.** I don’t have any idea what that number means in my life! <br>
> **Glad you asked.** Neither do I. It’s an acceleration which isn’t one of our normal everyday units (even though we speed up and slow down all the time while walking and driving). But one acceleration we do have a feel for is that of gravity, so let’s compare it to little gee, $g$.

This doesn't exactly press you to the back of your seat. You know how I know that? Because we can further convert it to something that we can compare with falling. That is, compare it to little $g$ which we know to be about $10$ m/s$^2$. So let’s get the miles per second into meters per second and we’ll just a little engine to do that. 

We know:

* our acceleration is $1.3 \times 10^{-3} \text{miles/s/s}$
* we can change the miles into meters and we’d then have that acceleration in meters per second per second

```{admonition} &nbsp; Please answer Question 5 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/dgkZsF" target="_blank">Some conversion practice </a>

```

We find that our unenlightened Mitsubishi acceleration of  $1.3 \times 10^{-3} \text{miles/s}^2$ converts to $2.2$ m/s$^2$. One more step to get it into something we can compare with life.

> **pulling gees**
>Acceleration at a rate of $g$ is called…well, “gees.” And “pulling gees” is a measure of acceleration that fighter pilots (and NASCAR drivers) must contend with: In order to not black out, humans can tolerate accelerations up to around 6 $g$’s, or accelerations of $6 \times 9.8$ m/s$^2=$  about 60 m/s$^2.$ That’s moving right along as you will see from the Porsche-experience below.

Remembering that $g=32 \text { ft/s}^2 = 9.8 \text{ m/s}^2$ we realize that flooring the little Mitsubishi isn't exactly like falling off a log...or falling off of anything for that matter, since it’s more than 4 times less acceleration than falling off that log at $g$ (9.8/2.2 = 4.4) .

If you black out while speeding up in your Mitsubishi, it’s not because of acceleration.

### Graphical Kinematics

Here's what our two cars' accelerations look like plotted:

```{figure} ./../_images/motion/carsv.png
---
width: 550px
name: carsv
align: center
---
The change of speed of our two cars shown as m/s but with a hint of what it would be in mph shown as an additional axis in green. The red line indicates the 60 mph mark corresponding to the two times of these two rather different automobiles.
```

Completing our journey through the graphical representations of constantly accelerated motion, here's the quadratic relation of the distance that the Mitsubishi and Porsche travel as a function of time:

```{figure} ./../_images/motion/carsx.png
---
width: 550px
name: carsx
align: center
---
The distance traveled as a function of time for both cars is shown above.
```

```{admonition} &nbsp; Please answer Question 6 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/lJY1Vr" target="_blank">Acceleration in a Porsche </a>

```

Finally, we can compare distance versus speed for our two cars.

```{figure} ./../_images/motion/carsxv.png
---
width: 550px
name: carsxv
align: center
---
The rest of the story of our two cars without explicitly using time as variable. We see what we'd expect: the Porsche reaches 60 mph in only about 50 meters while the Mitsubishi is still only going at about 30 mph at that distance and from the above curve is much behind its fancy rival.
```
