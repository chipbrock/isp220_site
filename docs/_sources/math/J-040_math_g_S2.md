## The M Word

I promise that the math of QS&BB will not be hard and we’ll get through it together. In this lesson I'll develop most of the tools that we’ll return to repeatedly: simple algebra, some familiar geometry, exponents, and powers of ten.

> **Wait.** Why use mathematics in a book for non-science people? I’m not a math person!

> **Glad you asked.**  Two reasons. First, there is a direct connection between   a mathematical description of a phenomenon and nature itself. As I said, we   don't know why that's the case and the argument about whether mathematics is   "discovered" or "invented" is endless.<br>   Second, it's much more economical than using words.<br>   Finally, it's a little deductive engine for many of our purposes. You can   "discover" things by manipulating the symbols...things that will further   explain the physics.<br>I guess I lied. That's three reasons.<br>Oh. There’s no  such thing as a “math person” at the level we’ll be using math!

I had a decision to make in designing a set of lessons about physics for non-experts: use no mathematics or use some. Let me show you what I decided, and why. But first, here's my guide to the use of mathematics in QS&BB:

> We'll use mathematics as a language to be “actively read” and a part of the narrative. But you'll not have to derive things on your own from scratch.

> **Wait.** What’s “active reading”? <br>
> **Glad you asked.** It means reading with your pencil moving. When you see this suggestive symbol:

```{admonition} &nbsp; Pens out!
:class: warning

the page will turn a color and you start “close-reading” the colored material by writing in your notebook…filling blanks, making notations, even copying what your eyes see --- yes, **by all means copy what you are reading!** (I do when I learn something new.) Then when it’s time to stand down, the page will go back to white and you can go back to “just” reading.

```

> **Wait.** I don’t have a notebook. <br>
> **Glad you asked.** Please get one for the full QS&BB experience ;) I'll wait. (tapping foot)


### A Tiny Bit Of Algebra

Our algebraic experience here will involve some simple solutions to simple equations. I’ll need the occasional square root and the occasional exponent, but no trigonometry or solving simultaneous equations and certainly no calculus. I’ll refer to vectors, but you’ll not need to do even two-dimensional vector-component calculations. What's not to like?

```{aside}

Some units, introduced prematurely:<br>   In this brief defense I’ll use some units that we'll learn more about: a kilogram   is a unit of mass, a Newton is a unit of force – an apple has a weight on earth of about 1 Newton, and of course a meter is a unit of length of about 3 feet.

```

If I'd chosen to avoid all mathematics in QS&BB then I think something important would be missing. To learn about QS&BB ideas would be like learning how to paint but ignoring a particular color...where "red" should be, you'd insert a tiny note saying that "red should be here." I'm convinced that absorbing a simple equation, which stands for something in the world, is a cognitively different experience from reading its symbols in a sentence.

### An example of the power in symbols

Later we'll learn the most fantastic model of motion that Isaac Newton invented---his Universal law of Gravitation. It explained the moon's orbit around the earth, the planets' motions around the sun, and still guides spacecraft through the solar system today. I could just tell you about it, or I could write it as an equation...a model. 

Let's compare two extreme approaches: I'll write out the content of the Gravitation rule in an English paragraph and in its algebraic form. Then we'll compare.

Unlike in Fight Club, let's talk about this battle:

>   **In this corner: Newton's Gravitational law as a paragraph**<br><br>
>   “The force of attraction experienced by two masses on one another is directly proportional to the product of those two masses and inversely proportional to the square of the distances that separate their centers. The constant of proportionality is called the Gravitational Constant which is    $0.0000000000667408\; \text{m}^3 \text{kg}^{-1}\text{s}^{-2}.$”

There. A perfectly good, if not moving, literary description of Newton’s rule. Lots of words, but it's complete and it's accurate.  But it's also inefficient and worse, it's... lifeless.

Let's contrast this with the mathematical opponent:

>**And in this corner: Newton’s law of Gravitation in symbols:**

> $$ F = G \frac{mM}{R^2} $$
> *F*  stands for the force of gravitation, $m$ and $M$ stand for two masses, $R$ is the distance between them, and $G$ is a number...that tiny number in the paragraph.

That's it.

I claim that in addition to the obvious efficiency of the symbolic, compact notation...there's  **insight** buried inside of an equation that's not in an English sentence. For example, here's a perfectly good interesting question about gravitation:

```{admonition} &nbsp; Pens out!
:class: warning

**A question!**  How might you guess at the approximate force of attraction that the moon feels from the Sun compared with the force of attraction that the moon feels from the earth?  <br><br>
**Glad you asked.** The paragraph-representation is not helpful. But the symbol-equation-representation is very easily manipulated to answer a question of it. Twist it around and it's ready to tell you something new. 
**Good job!** 

```

```{admonition} &nbsp; Pens out!
:class: warning

**Question!** So do it:  What is the approximate force of attraction that the moon feels from the Sun compared with the force of attraction that the moon feels from the earth? <br><br>
**Glad you asked.** We could answer the question by forming  the ratio of the two situations. Here's just the answer, postponing the actual solution to the lesson on gravity:

$$\begin{align*}
r(\text{SunEarth}) & =\frac{F_{Sm}}{F_{Em}} = \frac{G \frac{mM_S}{R_{Sm}^2}}{G \frac{mM_E}{R_{Em}^2}} \\
& = \frac{M_S}{M_E}\frac{R_{Em}^2}{R_{Sm}^2} \\
\end{align*}$$

```

It looks like distance matters a lot since it's involvement is squared. Putting in the values for masses and distances, you'd find that the moon feels the Sun almost twice as much as it feels the earth. **That information was buried inside of the symbolic representation...but not in the paragraph.**


The symbolic approach is agile. It gives us a path to the physics. It's alive! The paragraph just sat there. Watching.

> There's physical *insight* to be gained by looking at a function that describes---or maybe *is*?---nature.