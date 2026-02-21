## Some Mathematics

I'll treat mathematics is a language - something that I'll ask you to read, but not derive on your own. This is not a normal way of dealing with physics for non-science majors. Usually in such courses, you'd be reading along and *boom*, an equation will appear as if by magic. When I can, I'll motivate any relations which might require reading some of the story which will be in symbols and words, not just words alone. You'll see how I'll do that in a way that will increase your insight. Pencils will be involved.


That’s it. Now we have everything we need to turn numbers into sizes of...stuff.

### The Big 10: “Powers Of 10,” That Is

One of the more difficult things for us to get our heads around will be the sizes of things, the speeds of things, and the masses of things that fill the pages of QS&BB. Lots and lots of zeros for a large or small number means: lots of mistakes and a hopelessness for the relative magnitudes of one big or small thing compared to another. Big and small numbers are really difficult to process for all of us.

I have no idea how much bigger is the Milky Way Galaxy (950,000,000,000,000,000,000 meters) than the diameter of Jupiter (143,000,000 meters). It all blends together.

> **Wait.** That sounds pretty grim.
> **Glad you asked.** But wait. There's a solution: the beauty of "10" or lots of "10's."

#### Exponential notation

A number expressed in exponential notation displays like this:

$$\text{a number} \times 10^{\text{power}}.$$

So 5000 meters could be written as

$$5 \times 10^3 \text{meters}. $$

Let’s think about this in two parts. First, the 10-power part.

Some of you might have learned a different nomenclature like: 5E3. I'll accept it, but mixing letters for a number makes it harder to multiply or divide numbers in exponential notation. So I'll do it my way --- and I encourage you to also.

The rules above work for 10 just like any number, so $10^n$ is shorthand for the number that you get when you multiply 10 by itself $n$ times. This has benefits because of the features of 10-multiples, that we count in base-10, and now you can just count zeros. So for example:

$$10^3 = 10 \times 10 \times 10 = 1,000.$$

The power counts the zeros, or more specifically, the position to the right of the decimal point from 1. So if you have any number, you can multiply it by the 10-power part and have a compact way of representing big and small numbers.

```{admonition} &nbsp; Pens out!
:class: warning

So, following through:

$$ 3 \times 10^3 = 3 \times 10 \times 10 \times 10 = 3 \times 1000 = 3000. $$

We can do the same thing with numbers less than 1, by using negative exponents for the 10-power part.

$$ 0.03 = \cfrac{3}{100} = \cfrac{3}{10^2} = 3 \times 10^{-2}. $$

So you just move the decimal place the power-number to the right to go from $3 \times 10^{-2}$ to 0.03.

```

* BTW: you know the drill by now. Try typing in "3 * 10^3":

Calculate it:
        
<form target="_blank" action="http://www.google.com/search" method="get">
    <input type="text" name="q" size="80%"/>
</form>

* Or, "3 * 10^(-3)"?

The second thing is the number in front that multiplies the power of 10. It’s called the “mantissa” and that’s all it is…a number.

The powers of 10 come with handy nicknames that imply a particular amount... like "kilo-gram," meaning 1,000 grams. You already know many of them. Here are more powers of 10 than you ever want to know:

#### Powers of 10

:::{table} Large number powers of 10 including the SI ("International System of Units") letter-symbols.

| nickname | prefix | SI symbol | factor | power of ten |
| :- | :- | :- | :- | :- |
| septillionth  | yocto- | y      | 0.000000000000000000000001        | $10^{-24}$   |
| sextillionth  | zepto- | z      | 0.000000000000000000001           | $10^{-21}$   |
| quintillionth | atto-  | a      | 0.000000000000000001              | $10^{-18}$   |
| quadrillionth | femto- | f      | 0.000000000000001                 | $10^{-15}$   |
| trillionth    | pico-  | p      | 0.000000000001                    | $10^{-12}$   |
| billionth     | nano-  | n      | 0.000000001                       | $10^{-9}$    |
| millionth     | micro- | $\mu$  | 0.000001                          | $10^{-6}$    |
| thousandth    | milli- | m      | 0.001                             | $10^{-3}$    |
| hundredth     | centi- | c      | 0.01                              | $10^{-2}$    |
| tenth         | deci-  | d      | 0.1                               | $10^{-1}$   |
| one           |        |        | 1                                 | $10^{0}$    |
| ten           | deca-  | da     | 10                                | $10^{1}$     |
| hundred       | hecto- | h      | 100                               | $10^{2}$     |
| thousand      | kilo-  | k      | 1,000                             | $10^{3}$     |
| million       | mega-  | M      | 1,000,000                         | $10^{6}$     |
| billion       | giga-  | G      | 1,000,000,000                     | $10^{9}$    |
| trillion      | tera-  | T      | 1,000,000,000,000                 | $10^{12}$   |
| quadrillion   | peta-  | P      | 1,000,000,000,000,000             | $10^{15}$    |
| quintillion   | exa-   | E      | 1,000,000,000,000,000,000         | $10^{18}$    |
| sextillion    | zetta- | Z      | 1,000,000,000,000,000,000,000     | $10^{21}$    |
| septillion    | yotta- | Y      | 1,000,000,000,000,000,000,000,000 | $10^{24}$    |
| ... | | | | |
| googol        |        | ?      | 10,000,000,000,000,000,000,000,000, |    |
|               |        |        | 000,000,000,000,000,000,000,000, |    |
|               |        |        | 000,000,000,000,000,000,000,000, |    |
|               |        |        | 000,000,000,000,000,000,000,000, |    |
|               |        |        | 000 | $10^{100}$   |

:::

> **Wait.** Is there a Googol of anything in the universe?

> **Glad you asked.** I don't think so. There is something like $10^{80}$ atoms in the universe...mostly hydrogen, as you'll learn later. The number of possible chess games that can be played is $10^{123}$. The number of unique shuffles of two decks of playing cards is $10^{166}$. But no Googol of things in the unverse. 

>BTW: I'm sure you'll be happy to know that a Googolplex is defined to be $10^{\text{googol}}$ or $10^{10^{100}}$.

You'll notice that I got lazy and skipped right to the end, where there's a "story there." When the Google.com inventors (one from East Lansing, BTW) were trying to come up with a name that would represent an enormous number of searches, someone suggested the name "googol," which is the nickname for $10^{100}$, which is indeed a lot. Well, when they went searching to see if anyone had registered the name, one of them misspelled it "google" and so that's what the company became. You're welcome.

A "feel" for sizes is pretty much limited to our puny human experiences. I can probably estimate a length of about 10 feet. So I might be able to approximate the hight of a building, for example. Or compare the distances of two plots of land. But much more than that, I'm out of in-grained tools. Well, this is "particle physics" and "cosmology"...the smallest items and the largest ones in the whole universe. So the prefixes in the list above? We'll need many of them. Here's a list of "things" from normal to, well, extreme.

### The Big and the Small of QS&BB: Sizes in the Universe

Here is a ranked list of big and small things with approximate sizes, along with the nicknames that we use. We’ll span these enormous distance ranges and eventually Tera-this and pico-that will just roll off your tongue.

#### Big Stuff


1. African elephant, 4 m
2. Height of a six story hotel, 30 m, $3.0 \times 10^1$ m
3. Statue of Liberty, 90 m, $9.0 \times 10^1$ m
4. Height of Great Pyramid of Giza, 140 m, $1.4 \times 10^2$ m
5. Eiffel Tower, 300 m, $3.0 \times 10^2$ m
6. Mount Rushmore 1700 m, $1.7 \times 10^3$ m, 1.7 km
7. District of Columbia, 16,000 m square, $16.0 \times 10^3$ m, or $1.6     \times 10^4$ m
8. Texas, East to West, 1,244,000 m, $1.244 \times 10^6$ m, 1244 km, or 1.244 mega-m
9. Pluto, 2,300,000 m diameter, $2.3 \times 10^6$ m
10. Moon, 3,500,000 m diameter, $3.5 \times 10^6$ m
11. Earth, 12,800,000 m diameter, $12.8 \times 10^6$ m, or $1.28 \times     10^7$ m
12. Jupiter, 143,000,000 m diameter, $143.0 \times 10^6$ m, or $1.43 \times     10^8$ m
13. Distance Earth to Moon, 384,000,000 m, $384.0 \times 10^6$ m, or $3.84     \times 10^8$ m
14. Sun, 1,390,000,000 m diameter, $1.39 \times 10^9$ m, 1.39 giga-m
15. Distance, Sun to Pluto, 5,900,000,000,000 m, $5.9 \times 10^{12}$ m, 5.9 tera-m
16. Distance to nearest star (Alpha Centuri), 41,300,000,000,000,000,000 m, $41.3 \times 10^{18}$ m, or $4.13 \times 10^{19}$ m, 41.3 Exa-m
17. Diameter of the Milky Way Galaxy, 950,000,000,000,000,000,000 m, $950     \times 10^{18}$ m, or $9.5 \times 10^{19}$ m, 9.5 Exa-m
18. Distance to the Andromeda Galaxy, 24,000,000,000,000,000,000,000 m, $24.0     \times 10^{21}$ m, or $2.4 \times 10^{22}$ m, 24 zetta-m
19. Size of the Pisces–Cetus Supercluster Complex, our supercluster,     9,000,000,000,000,000,000,000,000 m, $9.0 \times 10^{24}$ m, 9 zetta-m*
20. Distance to UDFj-39546284, the furthest object observed,     120,000,000,000,000,000,000,000,000 m, $120 \times 10^{24}$ m or $1.2 \times 10^{26}$ m

> This is out of hand. we have different units for astronomical objects!

And on the other end of the scale:

Representative big and bigger things.

#### Small Stuff

1. Circumference of a basketball, (regulation 30 inches) 0.762 m, 76.2 cm
2. Diameter of a golf ball, 0.043 m, 4.3 cm, or 0.043 m, 43 milli-m, mm
3. Diameter of a green pea, 0.001 m, 1 cm, or 0.01 m, 10 mm
4. A small ladybug, 0.5 cm, 0.005 m or $5\times 10^{-3}$ m, 5 mm
5. A human hair diameter. $10^{-4}$ m, 100 $ \text{micro-m, }  100 \mu$ m
6. Wavelength of mid infrared wave, $100 \times 10^{-6}$ m, $100 \mu$ m
7. Diameter of a human cell. $10^{-6}$ m, 10 $\mu$ m
8. Width of a large molecule. Sugar, $6 \times 10^{-10}$ m, 0.6 nm, 600 pico-m, pm
9. A large atom. Cesium atom (largest)  $ 2.225 \times 10^{-10}$ m, 0.225 nm, 225 pm
10. Wavelength of soft X-ray (12.4 keV), $100 \times 10^{-12}$ m, 100 pm
11. Wavelength of hard X-ray (124 keV, 300 EHz), $10 \times 10^{-12}$ m, 10 pm
12. Compton wavelength of an electron, $2.4 \times 10^{-12}$ m, 2.4 pm
13. Bohr radius, $53 \times 10^{-11}$ m, 53 pm
14. 1 Angstrom, $10^{-10}$ m, 100 pm
15. Radius of Helium nucleus (alpha particle). $1.6 \times 10^{-15}$ m, 0.016 femto-m, fm
16. Radius of a gold nucleus. $7 \times 10^{-15}$ m, 0.000007 nm, 7 fm
17. Diameter of a hydrogen nucleus (a proton). $ 1.3 \times 10^{-15}$ m, 0.0000013 nm , 1.3 fm
18. Radius of a quark (upper limit), $10^{-18}$ m, 1 am
19. The smallest distance that can exist: the “Planck length,” $10^{-35}$ m

<p class="caption"> Representative tiny things.</p>

We'll care about both extremes of these two tables of things.
I don't know Mr Huang, but his *Scale of the Universe 2* (http://htwins.net) is worth playing with, if not owning his app. You know. For parties.


### Simple Algebra

Have you ever used a spreadsheet? If not, I'll bet you will and in order to simplfy calculations, you'll probably write formulas and manipulate the results of formulas that you create. You'll do Microsoft Algebra, or "just algebra" since I don't think Microsoft has copywrited it yet.

It's no secret that physics can be pretty mathematical. QS&BB physics, notsomuch. We'll use zero trigonometry. We'll of course not use calculus. We'll use vectors, but only pictorially or in one-dimension only. Algebra manipulation is almost like a strategy game. You know where you want to go and what the rules are about getting there. You just need to remember:

