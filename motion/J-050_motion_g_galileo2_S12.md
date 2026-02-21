## Going In the Right Direction!

Now we need to add one more piece to the modern story. As we saw in the Mathematics review lesson, distances---displacements---are vector quantities. Because distance is in the definition of velocity, and since distance is a vector, so is velocity. Since velocity is a vector and acceleration is defined in terms of it? Yes, acceleration is a vector too.

### Velocity Is a Vector

Here’s our first physics-vector. I’ve been loose with the words speed and velocity. In fact, there’s a difference: velocity is a vector, $\vec{v}$, and so it includes a magnitude and a direction, and the magnitude of velocity is the speed. Now the definition of velocity should really be:

$$\vec{v} = \frac{\Delta \vec{x}}{\Delta t}$$

implicitly included distance ($\vec{x}$) as a vector quantity, but not time. North and east are different directions and $\vec{x}$ makes that clear. Like mass, temperature, and many other quantities, time is not a vector. At least, not yet!

Likewise, 60 mph east is not the same velocity as 60 mph north, but the speeds are the same---your speedometer would report the same speed for both trips.  Certainly if you’re trying to go north, you don’t want to deploy a *velocity* that points east. So both the magnitude (speed, here) and the direction are required to specify a velocity. We simply draw an arrow (on a paper, or map), the direction of which points in the direction of travel and the length of which is defined by some scale of speed magnitudes.


Now when you’re out walking I want for you to invent your own speed scale---how many inches equals 1 mph of walking speed---and then imagine this arrow sticking out of your chest. As you speed up, the arrow gets longer and as you slow down, the arrow shrinks. If you turn left, the arrow turns with you. Everywhere you go, you imagine your very own velocity arrow preceding you, pointing the way. You should also imagine arrows coming out of everyone you see, people on bicycles would have longer arrows and cars would have even longer ones. When they come to a stop sign? The arrow shrinks as you decelerate and blinks out of sight. Keep this in mind as we move on to those length-changing arrows.

### Acceleration Is a Vector

Since velocity is a vector and acceleration is defined in terms of velocity, it too is a vector:

$$\vec{a} = \frac{\Delta \vec{v}}{\Delta t}.$$

While the little arrow that represents your personal velocity always points out in front of you, its direction seems rather arbitrary. It goes where you go, but there’s nothing special about the direction. But that’s not really the case since our movement is inside of a coordinate system of streets, sidewalks, hallways, etc. and they all have relative directions and we could describe our velocity in terms of them. So, "60 mph east" would be a perfectly good vector description of speeding towards Detroit from East Lansing. Likewise, if we defined a vector of unit-length ($\mathbf{i}$) that points in the east direction and call that the $x$ axis, that same velocity could be written as $\mathbf{v}=60\, \mathbf{i}$ mph. The pretty subject of vector analysis is built this way, but in QS&BB we won't use that notation. We'll be relaxed and laid-back about most vectors. 

In that spirit let's choose to define our coordinate system such east is the positive direction and west, a negative direction. If you’re walking east, then you could say your velocity is 2 mph, east, or you could say that your velocity is $+2$ mph E. If you’re walking to the west, your velocity would be $-2$ mph E or $+2$ mph W (but usually we assign a positive direction and stick with it…East, to the right, is standard). The direction and the sign are mingled. Because we will work in one dimension most of the time, this dual-role for a sign will matter but hopefully be pretty easy and we will almost always be able to say: east is the $x$ axis and so our velocities above are $+2$ or $-2$, with the sign implying the direction of positive $x$ is east.

```{admonition} &nbsp; Pens out!
:class: warning

This is important as we consider the direction of an acceleration. Suppose your speed is 60 mph and after a certain time---let’s say 2 hours---your speed has increased to 70 mph. Remembering our ordering in the $\Delta$ notation of (now minus before), then  the magnitude of your acceleration would be:

$$a = \frac{\Delta v}{\Delta t} = \frac{70-60}{2} = 5 \text{ miles per hour}^2.$$

Now what if your original speed is reduced because you applied the brakes from 70 mph to 50 mph. Then we’d have:

$$a = \frac{\Delta v}{\Delta t} = \frac{50-70}{2} = -10 \text{ miles per hour}^2.$$

What are we to make of that negative sign? Of course it means we’re slowing down, and we learned that the term for that is deceleration. But that pesky sign change between accelerate and decelerate is again related to our coordinate system.

This figure lays out the circumstances for constant acceleration, including zero acceleration.

````{figure} ./../_images/motion/bugA.png
---
width: 550px
name: bugA
align: center
---
A car is shown for two events with the right column later in time than the left. In (a) the car moves at constant velocity; in (b), the car accelerates at a constant acceleration; and in (c), the car decelerates.
````

Of course the two vectors for velocity and acceleration would each refer to their own scales. At a constant speed, the velocity vectors are identical at the two times and the acceleration vector has zero length. As the car accelerates, the velocity vector gets longer. As the car decelerates, it's still going to the right, but its velocity vector gets shorter. The acceleration vector points the other way, so deceleration vectors point in the opposite direction as the velocity vectors.

I defy you now to not see arrows coming out of everything around you that moves. Welcome to my world.

```{admonition} &nbsp; Please answer Question 7 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/m5xh37" target="_blank">Dropping from that tower </a>

```

That speed is just about a high school fast ball, barely over the terminal velocity.

```{admonition} &nbsp; Please answer Question 8 for points:
:class: danger

<a href="https://loncapa.msu.edu/tiny/msu/hZcvt9" target="_blank">Little g </a>

```
