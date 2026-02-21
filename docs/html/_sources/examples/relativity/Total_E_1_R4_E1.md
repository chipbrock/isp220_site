# Relativity 4

## Example 2: The Total Energy Relation

**The Question:**  

The relation of the total energy to momentum is not an obvious extrapolation from our original total energy relation. So let's work through this:

How do we go from
$$
E_T=m\gamma c^2
$$
to 
$$
E_T^2 = m^2c^4 + p^2c^2 \text{ ?}
$$

------

**The Answer:** 

Here's what we know:
$$
\begin{align}
\text{energy: }E_T &= m\gamma c^2 \nonumber \\
\text{momentum: } p &= m\gamma v
\end{align}
$$
Let's square Equation 1:
$$
E_T^2 = m^2\gamma^2c^4
$$
and look at the square of the gamma function...a kind of insider-trick among relativistic aficionados.
$$
\begin{align}
\gamma &= \frac{1}{\sqrt{1-\beta^2}} \nonumber \\
\gamma ^2 &= \frac{1}{1-\beta^2} \nonumber \\
\end{align}
$$
and use that in Equation 4:
$$
\begin{align}
E_T^2 &= m^2\gamma^2c^4 \\
E_T^2 &= m^2c^4 \frac{1}{1-\beta^2}  \\
& \text{multiply through the big fraction: } \nonumber \\
E_T^2 \left( 1-\beta^2 \right) &= m^2c^4 \text{ almost there} \\
E_T^2 - E_T^2\beta^2 &= m^2c^4 \\
E_T^2 &= m^2c^4 + E_T^2\beta^2
\end{align}
$$
Now look at the last term in Equation 9 and do some manipulation remembering the momentum equation and that $\beta = v/c$.
$$
\begin{align}
E_T^2\beta^2 &= m^2 \gamma^2 c^4 \beta^2 \nonumber \\
E_T^2\beta^2 &=(m\gamma c)^2 \left( c^2 \beta^2 \right)\\
E_T^2\beta^2 &=(m\gamma c)^2 v^2 \\
E_T^2\beta^2 &=(m\gamma v)^2 c^2 \\
E_T^2\beta^2 &=p^2c^2
\end{align}
$$
so now we have it by substituting Equation 12 into Equation 9:
$$
\begin{align}
E_T^2 &= m^2c^4 + E_T^2\beta^2 \\
E_T^2 &= m^2c^4 + p^2c^2
\end{align}
$$
