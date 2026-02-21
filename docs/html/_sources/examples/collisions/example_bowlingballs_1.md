# Collisions

## Example 4: Two dimensional collision…without a single equation

Bowling ball $A$ is thrown at bowling ball B, which is sitting still. $A$'s path is slightly off center relative to $B$'s position (which is the dashed horizontal line) so it scatters at an angle and also pushes B into an opposite angle. The initial state is slightly transparent relative to the final state.

<img align="center" src="./twoballs.png">

<BR CLEAR="all">

We'll use real units here: mass is in kg, velocity is in m/s, and so momentum units are kg-m/s.

-   mass of the beam ball, $A$ 7 kg
-   mass of the target ball, $B$ 7 kg
-   speed of the beam ball: $v(A) =14$ m/s
-   so, the initial momentum of $A$ is  $p_{0,x}(A) =(7)(14)=100.8$ kg-m/s (call it about 100 kg-m/s)
-   speed of the target ball is zero, so $p_{0,x}(B) = 0$ kg-m/s
-   **I’ll tell us the final momentum vector components for $B$.** Let's say that the target ball, $B$, scatters down as show in the picture with the components
    -   $p_x(B)=40$ kg-m/s
    -   $p_y(B) = -60$ kg-m/s

**Question:**

-   What's the momentum and direction of the $A$ ball?


**Answer:**

What we want to know is the momentum of the $A$ ball after the scattering. The picture sort of hints at what to expect for the direction, right?

It's the same story as above, except we keep track of both directions separately and then combine them at the end. So here's a picture of the initial state for both the $x$ (left) and $y$ (right) momenta:

<img align="center" src="./two_initial.png">

<BR CLEAR="all">

All of the action is along the $x$ axis at the beginning, so the vertical action in (b) is all zero. 

* (a) is just like the stop shot in that $A$ has all of the initial momentum, in this case $p_{0,x}(A) = 100$ kg-m/s. 
* Notice that $T=0$ for the $y$ direction at the beginning, so whatever momentum there is in the final state...it has to add to zero. 
* Meanwhile, the $T$ for the $x$ direction is now established and carries over.

What we know about the final state is shown here. Remember, we know both the horizontal and the vertical $B$ momenta in the final state **and we know the final $T$ total momentum for each component because of momentum conservation**:

<img align="center" src="./two_final_a.png">

<BR CLEAR="all">

Notice that neither the $x$ nor the $y$ values of $B$'s final momenta are equal to $T$ in each direction...but momentum conservation says that the total of $A$ and $B$  should be equal to the respective horizontal and vertical $T$'s. 

So we can *simply construct* the missing $A$'s momentum in each direction:

<img align="center" src="./two_final_b.png">

<BR CLEAR="all">

Look at it. It makes sense since $A$ recoils from $B$ in the final state and if $B$ went down, then $A$ should go up…and it does here.

Now we know everything there is to know about the final bowling balls' two final state motions. We can then draw a *precise and accurate*  **Momentum Space Diagram** from this information:

In the Momentum Space Diagram, the scale is required and is shown in (a). (b) shows the initial state momenta and (c) takes the thermometer solution from above and plots the final momenta:

<img align="center" src="./two_scatter_1.png">

<BR CLEAR="all">

This is how car crash expert witnesses make their money. Doing these sorts of calculations but without bowling balls.
