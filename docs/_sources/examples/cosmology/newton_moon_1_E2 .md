# Galileo's Astronomy and Newton's Gravitation 

## Example 2: Newton's argument about the moon

This is a famous story with a famous Newton recollection. 

Let's put in the modern numbers, and I'll show where he made an early mistake:

* The velocity of the Moon, you figured out in Example 1. It turned out to be $3.36\times 10^3$ ft/s.
* The distance from the Earth to the Moon had been known since the Greeks to be about $D_M=60 \times D_E$ the radius of the Earth. That too had been known fairly well. The modern average number is $D_E=20,902$ ft.
* So, $D_M=60 \times 20,902 = 1.26 \times 10^9 \text{ ft}$

From that we can calculate the value of the centripetal acceleration of the Moon:

$$
\begin{align}
a_C(\text{M}) &=\frac{v_M^2}{D_M} \nonumber \\
&= \frac{(3.36 \times 10^3)^2}{1.26\times 10^9} = \frac{11.3\times 10^6}{1.26\times 10^9} \nonumber \\
a_C(\text{M}) &= 0.0089 \text{ ft/s/s}
\end{align}
$$
Now he actually does a remarkable bit of thinking. What, he wonders, would the centripetal acceleration be *if the Moon were brought to the radius of the Earth*? The reasoning from above was that the centripetal acceleration would be increased by the ratio of the distance to the Earth's surface to that of the Moon distance...squared. So:

$$\begin{align}
a_C(\text{E}) &= a_C(\text{M}) \times \frac{D_M^2}{D_E^2} \nonumber \\
a_C(\text{E}) &= 0.0089 \times \frac{(D_E \times 60)^2}{D_E^2} \nonumber \\
a_C(\text{M}) &= 0.0089 \times 60^2 = 32 \text{ ft/s}^2
\end{align}$$

Sound familiar? He knew that Huygens had measured the acceleration of gravity at the surface of the Earth ('cause that's where Huygens...and everybody is) to be 32 ft/s$^2$.

Bingo. What we've been calling "little $g$" is the centripetal force experience by objects orbiting the Earth at an "altitude" of one Earth's radius!

He first calculated this when he was back on the farm during the plague and he used a value for the radius of the Earth which was wrong. That led him to the value of the centripetal acceleration of the Moon to be:

$$
a_C(\text{M, Newton})= 0.0079 \text{ ft/s}^2.
$$
He knew the Huygens value would have predicted (going the other way from Earth to the Moon) 0.0089 ft/s $^2$ but he thought that was pretty good. He recalled this calculation many years later and wrote 

>**Famous Newton Recollection**<br><br>
>From Kepler’s rule of the periodical times of the Planets being in sesquialterate proportion of their distances from the center of their Orbs,I deduced
>that the forces which keep the Planets in theirOrbs must be reciprocally as the squares of their distances from the centers about which they revolves: and thereby compared the force required to keep the Moon in her Orb with the force of gravity at the surface of the Earth, and found them answer pretty nearly.

That is, that 0.0079 is pretty nearly 0.0089. Yup. And he fixed that mistake later.