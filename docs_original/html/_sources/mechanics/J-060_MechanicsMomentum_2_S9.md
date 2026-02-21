## Circular Motion

In Eq. {eq}`second1` the relationship of force to the vector momentum is subtle, but you use it and experience it every day. Suppose Hazel and Ira are a passengers in a car going around a curve. When they enter the curve, they're moving north. When they emerge from the curve, they're pointing west. Hazel is driving and watching the speedometer carefully in order to make sure that they remain at the same speed through the whole path. So did their speed change? No! Did their velocity change? Yes! Because, the *direction* of their speed changed. This is shown in the figure:

```{figure} ./../_images/mechanics/carcurve.png
---
width: 550px
name: carcurve
align: center
---
A car going around a curve at constant speed: at A, its speedometer reads 60 mph, at C, 60 mph, and as it’s going through the curve, also 60 mph. During the period when it’s going around the curve (when the steering wheel is turned), for a brief time it traces out a segment of the dashed circle with its center shown at x.
```

Let’s think in terms of momentum and this diagram shows the momentum vectors at A, B, and C:

```{figure} ./../_images/mechanics/carcurvedots.png
---
width: 450px
name: carcurvedots
align: center
---

```

Let's recite the series of events that follow from going around this curve: Hazel and Ira both remain in the car, so somehow they are both "forced" to deviate from straight-line motion along with their vehicle. A variety of phenomena cause that to happen: Hazel's smart and is wearing her seatbelt. That keeps her attached to the car as it turns. Nobody can tell Ira what to do, so he never wears a seatbelt and slides across the seat and is pressed up against his door and that keeps him moving in a circle. Each of these phenomena constitute forces that act  in a direction pointing to the *inside* of the circle that their car is moving—the point labeled x in the figure. Let’s state some obvious, but subtle things about this simple act:

-   Their speed didn't change.

- But, their direction changed, so their velocity changed.

-   If their velocity changed then their momentum changed (from the definition of momentum, $\vec{p}=m\vec{v}$.

-   If their momentum changed, there had to be an inward force applied to both of them. (from the 2nd law).

These various forces all caused them to go in the same circle as the car (Second law) while they are trying desperately to continue to go straight (First law!). (In fact, Ira had an apple in his hand and when the car turned left, he let go and the apple kept going straight north, out of the open window.)

The forces are:

* The seatbelt pulled on Hazel;
* Ira experienced a frictional force between his jeans and the seat but it but was not enough to keep him from sliding;
* so he slid until he pressed against the door and *then* the door applied a force;
*  and the tires of the car also have a frictional force to the pavement and that points “in” as well…in fact, that’s the only way that a car ever turns a corner.

Each of these forces points “in” toward x, the center of the circle and they all do the same job: pull the objects towards that center. These kind of forcing-in-a-circle forces have a special name:

> A force that causes motion to deviate from a straight line is called "centripetal force."

Another pretty good idea of Newton's (and Christiaan Huygens').

### Newton’s Reasoning

The essence of circular motion can be visualized in this cartoon:

```{figure} ./../_images/mechanics/tether.png
---
width: 350px
name: tether
align: center
---
A person swinging a ball overhead which is attached to a rope.
```

where a figure is twirling a ball attached to a rope in a circle. Let's ignore gravity for a second and concentrate on the motion in the plane of the rope and ball...and his fist. You know by now what would happen if he let go of the rope. Without the rope pulling in towards the center, there is no horizontal force and according to Newton's First law, the ball would go straight. (That’s a sling-shot.) So the rope is causing the ball to deviate from a straight line. Can you agree that the rope is doing the same thing that the seatbelt and tire friction do?

```{admonition} &nbsp; Have a look at a deeper explanation
:class: note

<a href="./../examples/mechanics/deeper_centripetal_force_1.html" target="_blank">for how the pull is to the center of the circle </a>

```

Whenever an object deviates from a straight line path, there must be a force pointing perpendicular to that path. For the simplest such motion --- moving in a circle --- that force points to the center of the circle. Newton (and Huygens, see the next lesson) envisioned circular motion this way:

* the object tries to go straight
* it's tugged to the center (the rope)
* it tries to go straight again!
* and again, it's tugged toward the center

Over and over this motion can be thought of as jagged straight-jerk, straight-jerk...but if the tugs are infinitesimally close together in time, then the result is a smooth circle, and not a jagged path.

If there's a perpendicular force to the center, then there's also an acceleration toward the center. These are both special things and have their own formulas to represent them. They also have a special name: "centripetal."

Why is there an acceleration? Even if the objects speed is constant? It's because while the speed is not changing, the direction is. Here the vector nature of the velocity (or momentum) is a big deal and it matters!

### Centripetal Force and Centripetal Acceleration

If this understanding of circular motion weren't enough, Newton went a step further in his paranoid sort of way. He actually found a relationship for what the centripetal force would be and did it both using his new calculus and in a strictly geometrical fashion. The latter he published in *Principia*, and like other such derivations, kept the calculus version to himself. Why? He feared being scooped. Calculus was his ("my precious") private tool for a long time.

I’ll just enunciate the result without his tedious geometrical explanation or the more complicated calculus explanation.

The essence of this is shown on the left and right figures here, where we see a representation of the momentum vector and the centripetal force, $\vec{F}_C,$ on the left, and following Hazel and Ira’s experiences, pointing to the center.

```{figure} ./../_images/mechanics/centfa.png
---
width: 550px
name: centfa
align: center
---
"Centripetal force points to the center and centripetal acceleration does the same thing."
```

But where there's smoke, there's fire...or rather, where there's a force, there's an acceleration, because $F=ma,$ right? The right hand side of the figure shows this "centripetal *acceleration*," a different vector but pointing in the same direction as the centripetal force vector. So we have:

```{admonition} &nbsp; Pens out!
:class: warning

$$\vec{F}_C = m\vec{a}_C.$$

Here’s the punchline for centripetal acceleration:

Centripetal acceleration</mark> is special and has a very particular form (found by Newton and his Dutch competitor, Christiaan Huygens) for all curvy motions. It's<br>

$$a_C=\frac{v^2}{R}$$

Here, $R$ is the radius of that circle and $v$ is the magnitude of the velocity. So, we have for circular motion only:

$$F_C=m\frac{v^2}{R}.$$

The speed of an object moving in a circle is of interest and it’s easy to model that by multiplying the $F_C$ by $R$ and dividing by $m$:

$$v^2 = \frac{F_C R}{m}\label{vcentrip}$$

There are two ways to use this concept:

- If you want something to move in a curved path at a particular speed, you can calculate and apply a precise (centripetal) force---tug it---to make that happen. Depending on the curve ($R$) and the speed you want, you can dial up the $F.$ This is instinctive...your muscle-brain connection does it all the time.
- If you see that an object is *not moving in a straight line*, then there has to be a centripetal force being applied somewhere! You should be able to find the cause, or infer a cause.

Sometimes identification of such a force is tricky. Remember that in Hazel's car, what actually causes the car itself to go around a circular curve is the force of friction between the road surface and the four tires of the car---four little force vectors all pointing along the road-tire interface towards the center. Each little $F_C$ adds together to equal the $F_C=m\frac{v^2}{R}$ involving the speed and the turning radius. Here $m$ is the mass of the car plus that of its occupants (less that apple that went out the window).

* Reduce the stickiness of the road (ice, snow, rain?) and that friction force is reduced on the left --- we've all been there --- and that available force is reduced, sometimes considerably. You instinctively know this, so you drive slower (reducing $v$ in the numerator to match the $F_C$ that *can* be produced by the tires and road given the conditions.
*  Make  the turn tighter and so the $m\frac{v^2}{R}$ goes up and it better be balanced by the tires’ stickiness on the road.

If any of these limits are reached, you cease doing circular motion and Newton’s 1st law wins and you start going straight. Not good in most circumstances where the road curved.

```

```{admonition} &nbsp; Please study Example 8:
:class: warning

<a href="./../examples/mechanics/merrygoround_1_E8.html" target="_blank">Everyone's favorite playground device not requiring an apple </a>

```

```{admonition} &nbsp; Please answer Question 7 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/c3kRrt" target="_blank">Olympics...sort of </a>

```

```{admonition} &nbsp; Please study Example 9:
:class: warning

<a href="./../examples/mechanics/hammerthrow_1_E9.html" target="_blank">NCAA hammer throw </a>

```

```{admonition} &nbsp; Please answer Question 8 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/df6x0M" target="_blank">Centripetal force for hammer throw </a>

```
