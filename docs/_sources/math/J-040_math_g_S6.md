## A Gentle Review 2: Skills for Only a Few Times

There are a handful of skills that will sometimes come up, but not every lesson. I have in mind here reading log-plots, unit conversions, approximating functions, simple graphical vector manipulations, and a few more geometrical relationships.

### Log-Log and Semi-Log Plots 

> **Wait.** LOGARITHMS!!? NO! 
>
> **Glad you asked.** Calm down. There will be only a couple of times when I'll ask you to read a plot…meaning identify a point on a curve in which the axes are not linear (1, 2, 3, 4…) but logarithmic (10, 100, 1000…). No functional manipulations. Just interpretation.

Sometimes it will be useful to plot functions or data that range over a wide scale, maybe even many powers of 10. I want to make use of log-log plots and semi-log plots because it's about the only way to display functions that range over many orders of magnitude. So we'll use them as a tool, but we'll never actually evaluate a logarithm. Here's an example.

We'll learn that there is a relationship between the time it takes for a planet to orbit the sun (its "period") and the distance away that its orbit is from the center of the sun. Here it is for a slice of distances. The graph displays the orbital period in units of days versus the distance  from the sun in units of 100,000,000 kilometers. So the left hand "origin" is at 100,000 km, then the next big tick mark is at 110,000,000 km and the next (labeled) tick mark is at 120,000,000 km. That's a lot of zeros, so I labeled the horizontal axis as units of $10^8$ km.

```{figure} ./../_images/beginning/earthlinear.png
---
width: 550px
name: earthlinear
align: center
---
If I asked you to find the distance earth, which has a period of 365 days, is from the sun, you'd look at the vertical, period axis, dig into the tick marks, and figure out where to find 365 on the vertical axis, right? I've kind of done that --- what your finger would probably do --- and I find that the horizontal, light lines are at every 10 days and the tick marks are at every 20 days, so I'd find 365 at about where the horizontal arrow is. Using the model --- solving the equation that relates period to distance --- means simply finding the point on the curve and reading down to the distance. Going down from the curve, it would hit at about $1.5 \times 10^8~$km. That's about right.
```

If I asked you to do the same thing for Venus, but the other way around you could do that.

```{admonition} &nbsp; Pens out!
:class: warning

If Venus is $1.07 \times 10^8$ km can you convince yourself that its orbital period is about 226 days? 

```

How about Mars? Its period is about 687 days. Certainly the model (the blue line) should describe Mars. How about Mercury? Its period is 87 days and it's distance is $0.58 ]\times 10^8$ km. How about Neptune? It's period and distance are 60,200 days and $44.8\times 10^8$ km. None of these fit on the graph. So this plot is pretty useless as a guide to the solar system. Don't despair. There's a way.

This is where a log-linear or log-log plot saves the day. In a log plot the axes are labeled by powers of 10, so 1, 2, 3… and so on, standing for $10^1, 10^2, 10^3$. This power relation distorts the curve from presentation on a linear scale pair, but it's not wrong, just different. Let's do that for our solar system for the horizontal axis. 

```{figure} ./../_images/beginning/earthLinLog.png
---
width: 550px
name: earthLinLog
align: center
---
In this figure, the dark, black vertical lines tell you the $1\times 10^8, 1\times 10^9, \text{ and } 1\times 10^{10}$ km marks. The vertical gray lines indicate the $2, 3, 4, 5, 6, 7, 8, 9\times 10^{8, 9, \text{ or }10}$ km marks. The  circular inset breaks down the $10^8$ region to that of the linear horizontal plot up above. Notice that the red, dashed lines mean what they did in the first plot: 365 days for Earth's period on the vertical axis and about $1.5 \times 10^8$ km for Earth's distance from the center of the sun on the horizontal axis.
```

In this figure, the dark, black vertical lines tell you the $1\times 10^8, 1\times 10^9, \text{ and } 1\times 10^{10}$ km marks. The vertical gray lines indicate the $2, 3, 4, 5, 6, 7, 8, 9\times 10^{8, 9, \text{ or }10}$ km marks. The  circular inset breaks down the $10^8$ region to that of the linear horizontal plot up above. Notice that the red, dashed lines mean what they did in the first plot: 365 days for Earth's period on the vertical axis and about $1.5 \times 10^8$ km for Earth's distance from the center of the sun on the horizontal axis.

But we still can't represent much of the solar system in one plot, so we must also make the vertical axis logarithmic. A "log-log" plot, whereas the previous is a "linear-log" or "semi-log" plot. Here it is, the model of orbiting planets around our particular Sun. Earth is again represented as the red, dashed lines and now we can evaluate the periods and distances for many more planets.

```{figure} ./../_images/beginning/solarsystem.png
---
width: 550px
name: solarsystem
align: center
---
Kepler's 3rd law for anything orbiting in our solar system: the period versus the distance from our sun.
```

This covers 6 orders of magnitude in days and 4 orders of magnitude in kilometers.

```{admonition} &nbsp; Pens out!
:class: warning

Jupiter is $483 \times 10^6$ miles from the sun. What's its period in days? You'll want to consult Mr Google to get km. The period is about 4000 earth days, about 12 earth years.

```

### Unit Conversions 

Numbers are just numbers without some label that tells you what they refer to. Not all numbers have to refer to something, a pure number is a respectable mathematical object—prime numbers for example have been a topic of research for centuries. Irrational numbers --- those that can’t be expressed as a ratio of whole numbers, like $\pi$, --- are likewise objects with no necessary relationship to...“stuff” in our world. But they keep coming up in nature, so we warm to them.

We’re mostly concerned with numbers that measure a parameter or count physical things and they come with some reference unit  ("foot")  that is a customary way to compare one thing with another. Of course not everyone agrees on the units that should be used. Wait. Let me restate that: there’s THE WHOLE WORLD that agrees on one set and then there’s the *United States* that marches to its own set of units. Thinking of you, "feet," "pounds," and "Fahrenheit."

I’ll not use Imperial units (feet, inches, pounds, etc.) very much, except to give you a feeling for something that you’ve got an instinct for…like the average height of a person or a single story house. We’ll use the metric system, in particular the MKS, aka SI units[^1] in which the fundamental length unit is the meter (about a yard), the fundamental mass unit is the kilogram, and the fundamental temperature unit is the Celsius. I'll generically refer to these as "MKS" (for meter-kilogram-second) or "metric units" without being too fussy about the fancier names, like SI.

[^1]: This stands for meter-kilogram-second, as the basic units of length, mass, and time. It’s a dated designation as the real internationally regulated system is now the International System of Units (SI) which stands for *Le Système International d’Unités*. The French have always been good at this.

It's small comfort that we're all in agreement on seconds, minutes, and hours and its base-60 origins. In 1793 the French tried to change that to "decimal time" with a 10-hour day, 100 minutes in an hour, and 100 seconds in a minute and so on, but it didn't catch on. 

Just like an exchange rate in currency, so many euros per dollar, we’ll need to be able to convert among many different units. All the time.

> **Wait.** That can be pretty involved. 
>
> **Glad you asked.** You're right and it can be a way to make mistakes and get all wrapped up in the conversion that you lose track of the physics. You know what? I'll not care. I'll give you little conversion engines that will do any unit conversion that you need to do. Just let me show you what it means and then we'll be pretty low-key about this.

Having said that, we should review how this works—what will be behind any tool that does unit conversion. 

Let’s get our bearings. What’s the height of an average male. Mr Google tells me that’s about 5’10”. How many inches tall is our average male? Here’s the pre-QS&BB  thought-process you’d use to calculate this.

Three steps:

1.  A single foot is $12$ inches.
2.  So, $5$ feet is $5 \times 12$ = $60$ inches
3.  and the combination is $60 + 10 = 70$ inches.

...which you could almost do in your head, which, by the way, averages in circumference at about 22 inches. You're welcome.

But this simple, almost intuitive calculation uses a more general conversion from one unit to another through a tricky multiplication by the number 1.  Can you multiply by 1? Then you can convert units like a champ.

```{admonition} &nbsp; Pens out!
:class: warning

Here's a cute way to write 1 by starting with some basic conversion translation like $12 \text{ inches} = 1 \text{ foot}.$ Then you make "1" out of it:

$$\begin{align*}
12 \text{ inches} &= 1 \text{ foot} \\
1 &= \frac{1 \text{ foot}}{12 \text{ inches}} \\
\text{ or} & \\
1 &= \frac{12 \text{ inches}}{1 \text{ foot}} \end{align*}$$


All unit manipulations this conversion factor and all you have to do is figure out which version to insert.

Armed with this, we can do the conversion of 5 feet to inches.


$$
\begin{align*}
5 \text{ feet} = 5 \text{ feet} \times 1 &=  5 \text{ feet } \times  \frac{12 \text{ inches}}{1 \text{ foot}} \\
5 \text{ feet} \times 1 &= 5\times 12 \text{ inches} = 60  \text{ inches} \\
5 \text{ feet} &=60  \text{ inches}
\end{align*}
$$
Notice that we treat units like algebraic terms and can cancel them as if they were symbols or numbers: the “feet" cancel above. That’s the neat thing. If you set up the conversion factor right, the units will multiply and divide along with numbers so you can always see that you get what you want. <br><br>
While this is a particularly simple conversion, sometimes we’ll need to do some which are either more complicated, or use units that maybe you’re not very familiar with. I won’t be so pedantic usually, but hopefully you get the point!


```

>Let’s work out an example. Something you can use at a party. I first worked this out for a class when I was in Geneva, Switzerland working at CERN. It was July 4, 2010, which was just another Sunday over there. The United States came into existence on July 4, 1776[^3] which was $2010-1776 = 234$ years ago.

[^3]: Actually, the Declaration of Independence wasn’t fully signed until August 2, 1776—my birthday! The day, not the year.

```{admonition} &nbsp; Pens out!
:class: warning

**Question!** How How many seconds had the United States been around if we start from midnight on July 4, 1776?<br>
**Glad you asked.** We need a handful of 1's here:
>
$$\begin{align*}
1 &= \frac{1 \text{ minute}}{60 \text{ seconds}} = \frac{60 \text{ seconds}}{1 \text{ minute}} \\
1 &= \frac{24 \text{ hours}}{1 \text{ day}} = \frac{1 \text{ day}}{24 \text{ hours}} \\
1 &= \frac{1 \text{ hour}}{60 \text{ minute}} = \frac{60 \text{ minute}}{1 \text{ hour}} \\
1 &= \frac{1 \text{ year}}{365 \text{ day}} = \frac{365 \text{ day}}{1 \text{ year}}
\end{align*}$$

Now it's a matter of just multiplying by the right combinations of "1" as many times as necessary to get where you want to be.

$$\begin{align*}  
234 \mbox{ year} &=  1 \times 1 \times 1 \times 1 \times 234 \mbox{ year} \\
 &= \frac{60 \text{ seconds}}{1 \text{ minute}}\frac{60 \text{ minute}}{1 \text{ hour}}\frac{24 \text{ hours}}{1 \text{ day}}\frac{365 \text{ day}}{1 \text{ year}} \times 234 \text{ year}\\
&= \frac{31,536,000 \text{ second}}{\text{year}} \times 234 \\
234 \mbox{ year} &= 7.38 \times 10^9 \text {seconds}
\end{align*}$$

**Good job!**

```

There are a few of things to notice here. First, that’s a lot of seconds! Second (get it?), if we'd known that there are $3.154 \times 10^7$ seconds in a year we could have started with that and had just one factor of 1. And finally..."3.154"? Does that sound familiar to anyone? 

Quite by accident, the number of seconds in a year is close to the first few digits of $ \pi = 3.14159... $ times $10^7$ and so we often say that the number of seconds in a year is about "$\pi \times 10^7$."
Just as a memory device. You're welcome.

### Vectors, 2 

Some quantities in nature have a magnitude (like a temperature) and a magnitude and a direction, like a velocity. 60 mph north does not result in the same trip as 60 mph east, so direction and speed both matter. I think that the most intuitive vectors are those associated with a distance in space and a force, so in this survey I'll concentrate on those two. We'll meet many other vectors throughout QS&BB, but I'll highlight their vector natures when we come to them. As I'm writing this, the World Series in 2018 is about to start, so let's think about a baseball diamond.

In baseball, the distance between the bases is 90 feet and according to the rules, a runner must follow the bases in order. So to go from home plate to second base, the path that's followed must be according to the two arrows in this figure. This situation is shown in the (a) below. Here, Frank has hit a double and being a good sport has indeed taken the appropriate path to second base.

```{figure} ./../_images/beginning/bbinfield.png
---
width: 550px
name: bbinfield
align: center
---
Figure (a) shows the appropriate path to second base. (b) Shows an illegal path to second base. 
```

```{admonition} &nbsp; Pens out!
:class: warning

Notice that the total path is represented by two vectors,

$\vec{D}_{h1}$ and $\vec{D}_{12}$.

```

> By the way, the formal name for a vector representing how fast something is going is velocity and the length of the velocity vector is speed. We'll cover that idea in the next lesson.

There are many ways to represent the combination of magnitude and direction for a vector. When marking with a pencil, one would typically draw an arrow over the symbol as I've done here. In a fancy printed version, the $D$ would be bold, **D**. We must also adopt a coordinate system in every situation so that the direction can be concretely specified. You might have used an $x-y$ coordinate system, but that's not necessary. Here the ballpark has been layed out with north being directly to second base from home plate---that's a coordinate system.<br><br>

> It's also incorrect for a baseball diamond to be oriented straight north. According to Rule 1.04, "It is desirable that the line from home base through the pitchers plate to second base shall run East-Northeast.

In order to represent all of the information in a vector, we'll be satisfied with either a graphical representation---a labeled picture---or something else. Here's an example. If Ossie hits a single, we could represent his trajectory vector from home to first base as

$$\vec{D}_{h1} = 90 \text{ ft NE}. \nonumber$$

The formal name for a vector in regular space is *displacement* and the formal name for the magnitude of a displacement vector is *length* or *distance* so the vector $\vec{D}$ is the displacement and 90 ft is the length.

Maybe not the way you might have seen a vector displayed, but it's perfectly okay. It encodes the length (90 feet) and the direction (northeast) in one thing.

Next up, Dewey smacks a double, and so his vector would be

$$\vec{D}_{h1} +  \vec{D}_{12}. \nonumber$$

Chester is up next and realizes that the *shorter distance* from home plate to second base is straight north across the diamond over the pitcher's mound, which is shown in (b). While he hit the ball to the warning track, after that day he didn't play long on that team since he took that shorter path and was called out for not following the rules. What's okay in mathematics is not necessarily okay in baseball.

Chester is right, though. Before he was called out, he correctly navigated what is actually the vector sum of two vectors:

$$\vec{D}_{h2 } = \vec{D}_{h1} +  \vec{D}_{12}. \nonumber$$

Both the left side and the right side of that equation are equivalent in that they both connect home plate with second base.

```{admonition} &nbsp; Pens out!
:class: warning

**Question!** Earlier Earl was at bat and hit a ground ball to the shortstop but he fell down halfway to first base. How does his displacement compare to Ossie’s in vector notation? <br>
**Glad you asked.** Before his embarrassment, Earl was running in the same direction that Ossie ran---and thousands of ball-players before them. However his vector would be:

$$\vec{D}(\text{Earl}) = 0.5 \vec{D}(\text{Ossie}) = 45\text{ ft NE},$$

an arrow pointing from home plate halfway to first base.

**Good job!**
```

> Dewey was also unlucky and after Chester was called out he tried to steal third base from second base, but fell down 1/3 of the way. What’s the vector that represents his short trip?

In QS&BB we’ll make a lot of use of the handy arrow symbol: $\rightarrow$. The length of the arrow represents the magnitude and of course the orientation and the head of the arrow represent the direction. Arrows can be $\longrightarrow$, or short $\rightarrow$, pointed in different directions, $\nwarrow$, $\leftarrow$, $\nearrow$, etc. Very handy.

The magnitude can mean many things, depending on the physical quantity being represented. Some of the vectors that we'll meet are displacement, velocity, momentum, force, electric field, magnetic field, and angular momentum.

A few useful things from this figure:

```{figure} ./../_images/beginning/vectors6.png
---
width: 350px
name: vectors6
align: center
---
Random vectors, all of the same length. 
```

Two vectors, $\vec{A}$ and $\vec{B}$ are said to be equal if they are
*both* the same length *and* point in the same direction so

$$\vec{A} = \vec{B}. \nonumber $$

Vector $\vec{C}$ is the same length as both $\vec{A}$ and $\vec{B}$ but

$$\vec{C} \ne \vec{A} \text{ and } \vec{C} \ne \vec{B} \nonumber $$

because its direction is different. Finally, the negative of a vector is that same vector pointing in the opposite direction. So for example,

$$\vec{A} = - \vec{D}. \nonumber $$


#### Vector addition in one dimension 

Generally, we'll treat a vector quantity as an arrow pointing in some direction and a length that represents its magnitude. Sometimes a vector can represent an actual path in space (like meters, feet, and so on) where it's easy to imagine what it means. We do this all the time on maps with a scale showing that some map-distance (an inch) can stand for a real-world distance ("1 inch = 1 mile").

But, sometimes a vector doesn’t represent a length in space, but some other physical quantity, like a force or a velocity. This can be complicated since you’re drawing an arrow that has a "regular" length, but you mean it to be something else, like a force. But, it still works geometrically (the arrow still points in space) and we just use a different scale. Let's do something simple.

```{admonition} &nbsp; Pens out!
:class: warning

In the next figure are two vectors that now represent forces, so their lengths have the units of pounds. I'm obligated to provide a scale and you can see it. Vector $\vec{B}$'s length has a magnitude of 2 pounds and $\vec{A}$ is one pound more.

<img align="center" src="./../_images/beginning/vectors1.png" width=90%>

<BR CLEAR="all">

<figcaption> Two force vectors with lengths 2 and 3 pounds. </figcaption>

If $\vec{A}$ corresponds to Muriel pulling the leash on her reluctant and enormous dog and vector $\vec{B}$ corresponds to Earl's ability to also pull, then the two of them together can pull with the obvious 5 pounds.

<img align="center" src="./../_images/beginning/vectors2.png">

<BR CLEAR="all">

This is our first vector addition problem. The total vector force that the two of them can exert is in pictures above and in symbols

$$\vec{C} = \vec{A} + \vec{B} = \vec{B} + \vec{A} .$$
Here's the rule: We constructed $\vec{C}$ by connecting the tail of one vector with the head of the other. Keep that in mind, even though it's pretty obvious when everything is along one direction.

```

#### Vector addition in two dimensions, the head to tail way

Here's a different combination of vectors, which looks more like Chester's baseball career's embarrassing final act. Here, we have two vectors that have the same lengths on your screen, but now their lengths represent displacement (both a distance and a direction). They look like the force vectors and their lengths on your screen are the same, but the units are different: $\vec{A}=3$ blocks and $\vec{B}=2$ blocks.

```{admonition} &nbsp; Pens out!
:class: warning

<img align="center" src="./../_images/beginning/vectors3.png" width=90%>

<BR CLEAR="all">

This situation represents a trip through city blocks on the sidewalk: (a) going east $\vec{A}$ and then north, $\vec{B}$. Equivalently, (b) represents a trip from the same starting point to the same ending point by cutting across a park, $\vec{D}$. That third vector is gotten by doing the same tail-to-head manipulation as we did in one dimension. Of course, you'd create that third vector by just walking straight across the park. $\vec{D}$ is equivalent to the combination of $\vec{A}$ and $\vec{B}$, which is to say

$$\vec{A} + \vec{B} = \vec{D}$$

Obviously, it's useful to figure out whether the diagonal path is shorter than the sidewalk paths (thats' clear by looking) and just how much shorter it is. For that, we need the scale. Let's use the standard notation that the length (or "magnitude") of a vector is $\lvert\vec{V}\rvert$. So here $\lvert\vec{A}\rvert = 3$ blocks and $\lvert\vec{B}\rvert = 2$ blocks.

```

```{admonition} &nbsp; Pens out!
:class: warning

**Question!** In the figure, how much shorter is cutting across the park as compared to traveling on the sidewalk? 

**Glad you asked.** Obviously the sidewalk journey is  $3 + 2 = 5$ blocks. What's the length of $\vec{D}$? We can do this two ways. One way is to look at the triangle in (b) and remember Pythagoras' Theorem.

$$\begin{align*}
\lvert \vec{D}\rvert^2 &= \lvert \vec{A}\rvert^2 + \lvert \vec{B}\rvert^2 = 3^2 + 2^2 = 9 + 4 = 13 \\
\lvert \vec{D}\rvert &= \sqrt{13} = 3.6 \end{align*}$$

Or we can use the scale, as in (c)…construct $\vec{D}$  with the head-tail rule and then just transplant  it to the scale and see that its length is indeed a little more than 3 and a half. Or, somehow move the scale like a ruler and measure the length of $\vec{D}$.

Either way, it's shorter to cut across the park by almost a block and a half. But you sort of knew that.

```

#### Vector addition in two dimensions, the parallelogram way

Here's another situation.

```{admonition} &nbsp; Pens out!
:class: warning

<img align="center" src="./../_images/beginning/vectors5.png" width=90%>

<BR CLEAR="all">

The figure is sort of the same, but means something different. First, the scale says pounds, so it's two forces $\vec{A}$ and $\vec{B}$ but now they're oriented differently as shown in (a). It seems that Muriel and Earl were unable to get their acts together and so they're pulling on the dog's collar at right angles to one another.<br><br>

So their total pull here is going to be less than 5 pounds and will be some total amount that's oriented between the two. The (b) figure shows another way to add vectors as a manipulation. Instead of tail to head, (b) shows a placeholder parallelogram drawn in dashed outline and the sum of the two vectors is the diagonal. Of course it's the same vector you'd get if you'd transported $\vec{B}$ horizontally to the head of $\vec{A}$ and added them as before. So this is actually an alternative way to construct vectors sums: the head-to-tail way or the parallelogram way. 

```

#### Decompose a vector

An inverse of the process of adding two vectors is called *resolving* or *decomposing* a vector into its components. This figure shows the steps and is literally the parallelogram addition-method done backwards!

```{figure} ./../_images/beginning/vectors4.png
---
width: 550px
name: vectors4
align: center
---
The successive steps involved in 'resolving' a vector into its perpendicular components.
```

 vertical directions (it could be any two directions and they need not be perpendicular). The way to construct this is to add a placeholder parallelogram --- usually a rectangle --- with the original vector across a diagonal. Then the sides become the two decompositions:  the vector components. In both of these cases we're doing:

$$\vec{D} =  \vec{A} + \vec{B}. \nonumber$$

Here going from left to right (decomposition of $\vec{D}$) and just before, going from right to left (addition of $\vec{A} \text{ and } \vec{B}$).

####Vector subtraction

```{admonition} &nbsp; Pens out! 🖋 📓
:class: warning

Subtraction of vectors is easy, but requires some thought. In order to construct 

$$\vec{A} - \vec{B} = \vec{D} \nonumber$$

<br><br>We absorb the subtraction sign into the direction designation of $\vec{D}$ and make a new vector, $\vec{E} = -\vec{D}.$...and then add them. This shows the whole sequence of $\vec{A}-\vec{B} = \vec{A} + \vec{E} = \vec{D}$:

````{figure} ./../_images/beginning/vectors7.png
---
width: 550px
name: vectors7
align: center
---
The sequence involved in calculating $\vec{A} - \vec{B} = \vec{D}$
```
That is everything we'll need for any vectors that come along in QS&BB!




### Approximating Functions

```{admonition} &nbsp; Pens out!
:class: warning

One skill we'll need a couple of times is to be able to look at a function and estimate its form for extreme conditions. Here's what I mean. Look at this perfectly fine function:

$$y(x) = \frac{a}{b+x}. \nonumber$$

We'll ask this question of a function often: <br><br>

What is $y$ if $x>>b$ <br><br>

or what is $y$ if $x<<b$? <br><br>


Here's the thought process you'd go through to answer these questions. For the first one, if $x$ is very much larger than $b$ then that's nearly asking the question, "What is $y$ if $b = 0$?" which is the extreme of noting that if $b$ is really tiny compared to $x$ then it's almost as if $b$ isn't there are all. We'd get:<br>

$$y(x>>b) \approx \frac{a}{x} \nonumber$$

 The other extreme would lead you to say to yourself, "If $b$ is huge compared to any $x$, then it's almost as if $x$ isn't there at all." So:<br>

$$y(b>>x) \approx \frac{a}{b} \nonumber$$


This kind of analysis can lead to useful insight to the physics of a particular model. But we almost always want to look at a graph, like here, for the special case in which $a$ and $b$ are both 1:<br>

$$f(x) = \frac{1}{1+x} \nonumber$$

````{figure} ./../_images/beginning/function.png
---
width: 550px
name: function
align: center
---
The function $f(x) = \frac{1}{1+x} \nonumber$ which shows exotic behavior when $x=-1$.
```


For a moment, let's concentrate on this function for only positive values of $x$. Then the function looks like this:

```{figure} ./../_images/beginning/function_positive.png
---
width: 350px
name: function_positive
align: center
---
f(x) = \frac{1}{1+x} for values of positive $x$, that is,  $x>0$.

```

Now let's ask our previous two questions and look for answers in the behavior of the function in this restricted graphical incarnation: when $x$ gets very very small, the function approaches 1, just as you predicted: $y(1>>x) \approx \frac{1}{1}.$  Likewise, when $x$ is enormous, the function gets very small since it now looks like $y(x>>1) \approx \frac{1}{x}.$



But there's a more nuanced way of looking at approximations which is due to Isaac Newton. He found a way to represent a function in pieces, for cases in which the power of such a function could be anything: a positive integer, a negative integer, or even a fraction. The pieces add together to perfectly recreate the original function. The bad news is that to do so perfectly requires an infinite number of them! The good news is that one can get very close to the original function with only a few of the pieces.  In contrast to how that sounds, it’s actually very useful for many physics applications as we’ll see. 

Here's his expansion for our function:

$$f(x) = \frac{1}{1+x} \approx 1 - x + x^2 - x^3 + ... \nonumber $$

That last bit of $...$ means that the expansion continues in that pattern for an infinite number of terms. 

But notice that each term is a separate function in and of itself. That is, $f(x)$ can be written as the sum and difference of many functions, $1, x, x^2,...$. Add them all up and you'll get the original function in all of its glory. Add only the first few terms and you'll get close to the original function. Let's do that for the first four terms and compare it to the original, full-fledged function.

```{figure} ./../_images/beginning/combinedfunction.png
---
width: 550px
name: combinedfunction
align: center
---
The original function is in solid red and each successive curve adds the next term in the series. So, the blue dotted line is $f(x)=1$, the first term in the series; small dashed orange is adding $-x$, so $f(x)=1-x$; medium dashed green is $f(x)=1-x+x^2$; and finally, long dashed purple is $f(x)=1-x+x^2-x^3$.
```

Let's zoom into the region in the box. 

```{figure} ./../_images/beginning/combinedfunction_blowup.png
---
width:550px
name: combinedfunction_blowup
align: center
---

```

> **Wait.** I've had more fun than this… 
>
> **Glad you asked.** Here's the punchline. You'll thank me when we get to relativity. Or not.

Suppose that all you cared about was $x$'s that are less than about 0.1 and you need to evaluate the curve quickly, or gain some physics insight for that small of an $x$ region. Then you could get away with approximating 

$$\frac{1}{1+x} \approx 1-x$$

Look at how close the solid red curve is to the short dashed orange curve. Good enough.

Suppose you cared about $x$'s that are less than 0.3…then $1-x$ would not be accurate enough, but the long dashed purple curve would be since it's indistinguishable from the solid red curve up to that point.


Look how each curve successively makes the approximation better and better as $x$ increases. So if you can be confident that your $x$'s are going to be less than say 0.1, then you can approximate the original function with maybe the first two terms:

$$f(x) \approx 1-x \nonumber $$

since the blue and orange curves when added together are neatly underneath the red curve. The more terms we might add the further out in $x$ that agreement would continue. Add an infinite number of terms—not advisable—and you'd perfectly reproduce the original function. 

Remember this! It will become important later when we’ll encounter some physics functions and approximate them with a few terms of the expansions that we'll encounter.  Here are the functions that we’ll see in the lessons ahead:

$$\begin{align} \sqrt{1+x} &= 1+  \tfrac{1}{2} x - \tfrac{1}{8}x^2 + \tfrac{1}{16}x^3 - ... \\
\frac{1}{ \sqrt{1-x}}  &= 1 - \tfrac{1}{2} x +\tfrac{3}{8}x^2 - \tfrac{5}{16}x^3
+ ...\label{approxgamma}  \\
  \frac{1}{ 1-x}  &= 1 +  x + x^2 + x^3 + ...  \\
  \frac{1}{ (1+x)^2}  &= 1 -  2x + 3x^2  -4 x^3 + ... \label{approxforce}
  \end{align}$$

Thanks, Isaac.

### Formulas From Your Past That Might Only Be Referenced Informally

Ellipses and hyperbolas will come up, but descriptively. I’ll just want you to have a feel for their shapes and some of the terms that are defined by them. Just file away this location and we’ll come back only a few times.

#### Equation of an ellipse  

An ellipse is a squashed circle (?) that has two axes, the major axis ($a$) and the minor axis ($b$). The points at which the curve goes through the axes at the major axis points are called the vertices of the ellipse. The equation of an ellipse centered on the origin is

$$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1.$$

The figure of an ellipse centered on the origin is here:

```{figure} ./../_images/beginning/ellipse.png
---
width: 550px
name: ellipse
align: center
---
An ellipse with equation $\frac{x^2}{36}+\frac{y^2}{16}=1.
```

The focus ($c$ in the diagram) of an ellipse is shown and has the relationship to the curve in that any line connecting one focus to the curve and then to the other focus is always constant. The relationship to the major and minor axes is $c^2 = a^2-b^2.$ So, if $a=b$ then the ellipse is actually a circle and the position of the focus is at the center of the circle, here the origin. The degree to which an ellipse is almost-circle-like (more symmetric) and almost-flattened-like is determined by its “eccentricity,” $e$. It’s defined as $e = \frac{c}{a}$. So an eccentricity of zero is a circle and the larger the eccentricity, the more the focus point is close to the vertex...and the flatter it is.

#### Equation of a hyperbola  

I’ll want to refer to a hyperbola once in QS&BB and it will have a particular shape. This particular form of hyperbola is open to the right and left and crosses the $x$ axis at $\pm a$---the “semi-major axis”---and has a semi-minor axis of $b$ (see the figure). The equation is

$$\frac{(x-x_0)^2}{a^2} - \frac{(y-y_0)^2}{b^2} = 1.$$

The points $(x_0, y_0)$ are where the center of the hyperbola is and in the figure, that’s the origin.

There are a variety of definitions which you can see on the diagram.

```{figure} ./../_images/beginning/hyperbola.png
---
width: 550px
name: hyperbola
align: center
---
The equation of this hyperbola is $\frac{x^2}{36} - \frac{y^2}{16} = 1.$
```

