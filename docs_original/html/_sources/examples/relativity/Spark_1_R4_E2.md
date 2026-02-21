# Relativity 4

## Example 4: Spark!

**The Question:**  We're going to work out a number of relativistic quantities experienced by an electron in a major spark in a neighborhood high voltage transmission line substation feed. You see the spark? That's electrons ionizing the air as they jump from a hot to a ground connection. It's a current without a wire.

![spark](spark.png)

Assume tha tthe voltage is 138,000 Volts, which is common. (That's East Lansing's provider Lansing Board of Water and Light's substation voltage, for example.)

So electrons gain kinetic energy by being accelerated through that voltage.

Calculate:

1. The rest energy of an electron in  Joules and electron volts
2. the rest mass of an electron, eV/$c^2$ 
3. kinetic energy of an electron in  Joules and electron volts
4. the relativistic $\gamma$ of an electron's frame as viewed by the ground
5. the $\beta$ of an electron
6. the relativistic mass of an electron in eV/$c^2$ 
7. the total energy of an electron in eV

------

**The Answer:** 

Here's what we know:

$$
\begin{align*}
m_e &= 9.11 \times 10^{-31} \text{ kg} \\
V &= 138,000 \text{ Volts, V} \\
V &= 138,000 \text{ Joules/Coulomb, J/C }
\end{align*}
$$

1\. Rest energy of an electron...in Joules and in electron volts, eV

This is the T-shirt equation at work:

$$
\begin{align}
E_m &= m_ec^2  \nonumber \\
&= (9.11 \times 10^{-31} \text{kg})(3 \times 10^8 \text{m/s})^2 \nonumber \\
E_m &= 8.2 \times 10^{-14} \text{ J} \nonumber
\end{align}
$$

Remember that the definition of an electron volt is the energy acquired by a particle of the fundamental electric charge ($\pm e$) as it's accelerated through a voltage of 1 V. 

$$
U = QV = (1.6 \times 10^{-19} \text{ C})(1 \text{ J/C}) = 1.6 \times 10^{-19} \text{ J} \equiv 1 \text{eV}
$$

Let's convert our electron energy:

$$
\begin{align*}
E_m &= 8.2 \times 10^{-14} \text{ J} \nonumber \\
&= \text{multiply by 1, written as: } 1=\frac{1 \text{ eV}}{1.6 \times 10^{-19} \text{ J}} \\
E_m &= 8.2 \times 10^{-14} \text{ J} \times 1 \nonumber \\
E_m &= 8.2 \times 10^{-14} \text{ J} \times \left[\frac{1 \text{ eV}}{1.6 \times 10^{-19} \text{ J}}\right] \nonumber \\
E_m &= 5.11 \times 10^{3} \text{ eV} \\
E_m &= 5.11  \text{ keV} \\
E_m &= 0.511  \text{ MeV} \\
\end{align*}
$$

That's what we say: that the rest mass of an electron is "0.511 em-ev" or half of an MeV.

2\. the rest mass of an electron, eV/$c^2$ 

This is where the electron volts units start to be useful. We cheat. 

$$
\begin{align*}
E_m &= mc^2 \\ 
m &= \frac{E_m}{c^2} \\
m &= \frac{0.511 \text{ MeV}}{c^2} 
\end{align*}
$$

We're done. That's what we say is the mass: "0.511 em-ev over c-squared" or half of an MeV/$c^2$ . Mr Google agrees:

![electron_W](electron_W.png)

3\. kinetic energy of an electron in  Joules and electron volts

The kinetic energy of each electron is the energy given to them by that large voltage. In Joules:

$$
\begin{align*}
U &= QV = (e)(V) = (1.6 \times 10^{-19} \text{ C})(138,000 \text{ J}) \\
U &= K = 2.2 \times 10^{-14} \text{ J}
\end{align*}
$$

And, in electron volts...watch this:

$$
\begin{align*} 
K &= (2.2 \times 10^{-14} \text{ J}) \times \left[\frac{1 \text{ eV}}{1.6 \times 10^{-19} \text{ J}}\right] \\
K &= 138,000 \text{ eV} = 138 \text{ keV}
\end{align*}
$$

Notice the same number, but different circumstances.

4\. the relativistic $\gamma$ of an electron's frame as viewed by the ground

This comes from the definition of the relativistic kinetic energy:

$$
\begin{align*}
K &= mc^2(\gamma -1) \text{ ...manipulate this a little:}\\
\frac{K}{mc^2} &= \gamma -1 \\
\gamma &= \frac{K}{mc^2} +1 = \frac{K}{E_m} +1 \\
\gamma &= \frac{138 \text{ keV}}{511 \text{ keV} }+1 \\
\gamma &= 0.27 + 1 = 1.27
\end{align*}
$$

...which is mildly relativistic as you know from using the $\gamma$ plots. 

5\. the $\beta$ of an electron

Just look at a $\gamma$ plot to read off the $\beta$ and you'll get about 

$$
\beta = 0.65 \nonumber
$$

5\. the relativistic mass of an electron in eV/$c^2$ 

That's simple:

$$
\begin{align*}
m_R &= m\gamma = (511 \text{ keV/}c^2)(1.27) = 650 \text{ keV} \text{...or} \\
m_R &= (9.11 \times 10^{-31} \text{ kg})(1.27) = 11.6 \times 10^{-31} \text{ kg}
\end{align*}
$$

Notice again that even though we've used a special name "relativistic mass" it's nothing but the mass of the electron as viewed in the Home frame. The textbook mass of an electron is its mass as viewed in its own rest frame:

$$
m_R = m_H \nonumber
$$

so

$$
\begin{align*}
m_H &= 650 \text{ keV} \\
m_A &= 511 \text{ keV}
\end{align*}
$$


6\. the total energy of an electron in eV

Just add 'em up...the only two energies, that of mass and that of motion:

$$
\begin{align*}
E_T &= E_m +K \\
E_T &= 511 \text{ keV} + 138 \text{ keV} = 650 \text{ keV}
\end{align*}
$$

the same...since the total energy is the same as the relativistic mass. 
