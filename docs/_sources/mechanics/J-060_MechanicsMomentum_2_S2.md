## Impulse: Getting Going

$\require{enclose}\require{cancel}$

Newton's mechanics and many of the concepts we'll concern ourselves with, from electromagnetics to quantum mechanics to astrophysics, rely on the idea of a force. It's a common word, one of many that bear responsibility for everyday speech as well as specific, technical speech. Your common experiences with forces are all around you and you've instinctively learned to use everyday forces to move around and compensate for forces that threaten you. But your experiences with technical forces are probably related to weighing yourself or other things (that is, measuring the force that the earth pulls on something) and putting air in your tires (measuring the pressure that your tire presses against the tire's walls). There you deal with the US units of force, namely the pound (lbs), or in the case of your tires, pound per square inch (psi). We'll need to dig deeper than this, but whenever you see "pounds," you're talking about forces.

In a conventional physics course, Newton's Three laws of mechanics would be a major focus of study. In QS&BB we don't need that depth, but we do need three important concepts...the ones that underpinned his system: the concepts of **force**, **mass**, and **momentum**. Let's move:

In the previous lesson we laid out the rules that govern an object's motion, including whether it moves at a constant speed or accelerates. What we conveniently avoided was what causes motion --- on that score Galileo had nothing to say. (Remember that Descartes insisted on the cause of things before beginning to work on the outcomes? He explicitly denigrated Galileo’s work because Galileo explicitly avoided speculating on why an object would accelerate --- its cause.)

Of course Aristotle had something to say about everything and as we saw in the last lesson he insisted that *unnatural* motion is not for free, that one always needs to apply a contact force to start something to move and then to keep it going. Natural motion *is for-free* for him. No explanation of how, just that weird desire that heavy, falling objects have for the earth. There's so much that's wrong with both of these ideas that it's difficult to know where to start!

One of the many ways that Isaac Newton got into the textbooks was to argue with Aristotle: No. Constant motion *is* free. It's only accelerated motion that requires payment in the form of the action of a force. Further, while Aristotle simply declared what his rules were, Newton built the first-ever mathematical model describing them. Remarkably, his model has functioned for four centuries and still forms the basis of mechanical and civil engineering --- even NASA projects.

To start something moving from rest? Apply a force. To speed up or slow down something already moving? Apply a force! To cause something to deviate from a straight line? Yes. Another force. To keep something moving at a constant speed? No (net) force required, thank you.

Here's what he said:

>Whenever there's a change of velocity, a force is at work: forces are responsible for acceleration. </p>
These are Newton’s conclusion, but let’s start slowly and sneak up on this idea. Impulsively.

### Impulse In Practice

Newton:  To get something up to speed, you need to whack it or shove it --- either a sharp collision or a steady push increases the speed of an object. Push harder? More speed. Push longer? Again, more speed. And as you know from any sport involving a collision, something that’s moving fast can in turn exert a bigger force than something that’s moving slowly.

So let’s codify that everyday notion into a model of forces and motion. Let’s imagine a force, *F* that pushes during some time interval, $\Delta t$. A whack means that $\Delta t$ is small (like a golf club hitting a ball) while a steady shove (like a rugby scrum) means that the force is slowly applied so $\Delta t$ is larger.

Here’s what we know from experience: applying a force ($F$) to something for a time interval ($\Delta t$) results in the speed increasing in proportion, ($\Delta v$). We have the beginnings of a model:

$$
F\Delta t \propto \Delta v.
$$ (almostimpulse)

Increase $F$, $\Delta t$, or both on the left-hand side, and the speed goes up on the right-hand side. The quantity on the left side is called the **Impulse**. It's the sports-quantity. Any game involving a ball involves impulse and exceptional athletes can control both the $F$ and the $\Delta t$. The quantity on the right implies that the speed changed and of course if the speed changed, then the object accelerated.

We need to refine the model. But first some units and language:

>**May the force be with you by so many different names**
>We will use forces many times in QS&BB, which is a common quantity in our lives because of “weight.” But if you’re from the United States, when you step on the bathroom scale it reports back to you your weight in the Imperial measurement system (or “customary measures system”) as too many **Pounds**, lbs. In a minute, you’ll see why that’s confusing when comparing to the rest of the world where the bathroom scale would report kilograms. <br><br>
>In any case, the unit of force in the International System of Units (SI), which includes the older “metric system” or MKS (Meter, Kilogram, Second) is the **Newton**, N. If you go to the gas station in Berlin, you’ll fill your tires to a pressure measured in Pascals, which is Newtons per square meter. Of course up the street from me, our Michigan gas station reports pounds per square inch for my pressure.


We'll predominantly use the unit of Newton as the modern measure of a force --- like the rest of the civilized world. `As I've said, we'll not obsess with units and so I'm happy for you to rely on Mr. Google in almost all instances. Let's practice:

```{admonition} &nbsp; Please study Example 1:
:class: warning

Try a free warmup question:
<a href="./../examples/mechanics/poundsnewtons_1_E1.html" target="_blank">convert Newtons to Pounds </a>

```

```{admonition} &nbsp; Please answer Question 1 for points:
:class: danger

Try a free warmup question:
<a href="https://loncapa.msu.edu/tiny/msu/cTY9Sf" target="_blank">Pounds into Newtons and flour </a>

```

### Inertia

*Pressing* forward (see what I did there?). Let's think about pushing.

Suppose I apply a force of $F=100$ pounds for 60 seconds to a Volkswagen and you apply a force of $F=100$ pounds for 60 seconds to a little red wagon. We both begin our efforts at point A:

```{figure} ./../_images/mechanics/wagon.png
---
width: 350px
name: wagon
align: center
---
The same force applied to two red objects, of very different sizes.
```

Will the resulting $\Delta v$ at point B be the same for both vehicles? 

Of course not. The little red wagon will gain more speed than the Volkswagen (regardless of its color). The VW is more reluctant to be accelerated than the wagon. So Eq.6.1 is not the whole story. What's missing is just that reluctance that any object has to being accelerated, which has a name: **inertia**.

```{admonition} &nbsp; Have a look at this 6 min video example 1:
:class: warning

<video width="320" height="240" 
       src="./../_static/videos/beetlewagon.mp4"  
       controls>
</video>

```

> Inertia is the resistance that an object has to being accelerated.

**Wait.** What if the VW had been blue rather than red <br>
**Did you really ask that?** Stop it.
