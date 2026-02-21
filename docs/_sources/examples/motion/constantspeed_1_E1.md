# Motion

## Example 1: Up North.

**The Question:** Our plan is to watch an afternoon Tigers game and then head "up north" to the Mackinac Bridge. 

<img src="./images/michigan.png" width="500px" />

If we start after the game at 4 o'clock ($t_0=4$) at the entrance to I75 right near Comerica Park ($x_0$), reach 60 mph as we merge on the highway, and keep our speedometer steady at that value ($v=60$), then we'll get to the Mackinac Bridge, 300 miles away ($x=300$) by 9 o'clock ($t=9$). 

Here's our model of speed 

<img src="./images/mackinac.png" width="500px" />

It's a lot easier to use numbers rather than names and clock times so let's add the town's distances from the beginning and use decimal hours on the horizontal axis starting at the 4 o'clock point which we have the freedom to define to be $t_0=0$.

<img src="./images/bridge_a.png" width="500px" />

Grayling, Michigan is 200 miles from the freeway entrance. What time will it be when we fly by Grayling?



------

**The Answer:**

Two ways to look at this, both mean the same thing: we solve the equation for time:

$$\begin{align}
v &=\frac{\Delta x}{\Delta t} \\
\frac{v}{\Delta x} &= \frac{1}{\Delta t} \\
\Delta t &= \frac{\Delta x}{v} = \frac{200}{60} = 3.33 (\text{hours}).
\end{align}$$ 

So the time is $4+3.33 = 7.33$  o'clock, or about 7:20 pm.

Or we can "solve" the equation by looking at the left hand plot above where we would go up to 200 and then across to the line (the model of the equation) and down to just about 3.3 hours. 