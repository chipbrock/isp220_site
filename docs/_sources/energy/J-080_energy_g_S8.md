## Energy and Momentum, From 50,000 Feet

From the 1700s through the 1900's the science of mechanics became more and more mathematically formal. Rather than being a set of rough-and-ready tools at the disposal of engineers, mechanics and its mathematics revealed some neat things about how our universe seems to be put together. In particular, conservation laws went from a nice accounting scheme, to a clever way to solve difficult problems, to arguably the grandest of only a few universal concepts. I’ll try to explain some of this later when we delve into symmetry as we understand it today but let’s take a stab and meet Emmy.

```{figure} ./../_images/energy/emmy.png
---
width: 350px
name: emmy
align: center
---
A photograph of young Emmy Noether , probably around 1907, originally privately owned by family friend Herbert Heisig.
```

Amalie Emmy Noether (1882 - 1935) was the daughter of Max Noether, a well-regarded German mathematician from Erlangen University near Munich in the late 19th century. Max Noether was a contributor to algebraic geometry in the highly productive period where algebra was being abstracted as a very broad logical system, in which the puny subject that we learn in high school is only a small part. This particular apple fell very close to the tree and Emmy, as she was always known, turned out to be the most famous member of the Noether mathematical family (she had two brothers who had advanced mathematical training).

As a woman in Germany, only with an instructor’s permission, was she was allowed to sit in on courses at a university – she could not formally enroll as a student. She did this for two years when the rules were changed and she could actually enroll and she steadily advanced to her Ph.D. degree at Erlangen in 1907. She was not able – again, due to German law – to pursue the second Ph.D. that’s required in many European universities and so could not be a member of a faculty. So she stayed at Erlangen working with her father and colleagues. She even sponsored two Ph.D. students, formally enrolled under Max’s name, but actually working under her. She developed a spectacular reputation and gave talks at international conferences on her work in algebra. Nathan Jacobson, the editor of her papers wrote, "The development of abstract algebra, which is one of the most distinctive innovations of twentieth century mathematics, is largely due to her – in published papers, in lectures, and in personal influence on her contemporaries."

```{figure} ./../_images/energy/hilbert.png
---
width: 350px
name: hilbert
align: center
---
"David Hilbert, 1862-1943"
```

She was recruited in 1915 to work with the most famous mathematician in Europe, David Hilbert. He was racing Einstein to get to the conclusion of what became the General Relativity Theory of gravity and needed help with the complicated algebra and problems of symmetry, her specialty. Upon arrival at the Mathematics Capital of Europe, Göttingen, she quickly solved two outstanding problems, one of which has come to be known as Noether’s Theorem, and which is of fundamental importance in physics today.

Hilbert fought for years for Noether’s inclusion into the Göttingen faculty. He offered courses in his name, for her to teach. He led a raucous (in a early 20th century, gentile German sort of way) discussion in the faculty senate reminding his colleagues that theirs was not a bath house and that the inclusion of a woman was the modern thing to do. She was unpaid and yet still taught and sponsored a dozen Ph.D. students while at Göttingen. Einstein was particularly impressed and wrote to Hilbert, "Yesterday I received from Miss Noether a very interesting paper on invariants. I’m impressed that such things can be understood in such a general way. The old guard at Göttingen should take some lessons from Miss Noether! She seems to know her stuff."

Emmy’s great grandfather was Jewish and had changed his name according to a Bavarian law in the early 1800’s. However, this heritage became a dangerous burden for her and she emigrated in 1932 to Bryn Mayr College, outside of Philadelphia. There she resumed lecturing, including weekly lectures at the Advanced Institute at Princeton until she was suddenly and tragically stricken with virulent cancer that took her life in 1935. After her death, which was acknowledged around the world, Einstein wrote in the New York Times, "In the judgment of the most competent living mathematicians, Fräulein Noether was the most significant creative mathematical genius thus far produced since the higher education of women began. In the realm of algebra, in which the most gifted mathematicians have been busy for centuries, she discovered methods which have proved of enormous importance in the development of the present-day younger generation of mathematicians." But the most moving and personal obituary came from another eminent mathematician, Herman Weyl:

>**Weyl obituary** <br><br>
>You did not believe in evil, indeed it never occurred to you that it could play a role in the affairs of man. This was never brought home to me more clearly than in the last summer we spent together in Göttingen, the stormy summer of 1933. In the midst of the terrible struggle, destruction and upheaval that was going on around us in all factions, in a sea of hate and violence, of fear and desperation and dejection – you went your own way, pondering the challenges of mathematics with the same industriousness as before. When you were not allowed to use the institute’s lecture halls you gathered your students in your own home. Even those in their brown shirts were welcome; never for a second did you doubt their integrity. Without regard for your own fate, openhearted and without fear, always conciliatory, you went your own way. Many of us believed that an enmity had been unleashed in which there could be no pardon; but you remained untouched by it all.

An amazing person, all the more so at time when the path for women scientists was non-existent. We’ll see a few more as we go along. In any case, a crater on the Moon is named for her, a street and her childhood school are named for her, as are numerous prizes and scholarships around the world.

### Emmy Noether’s Theorem, In A Nutshell

The formal evolution of mathematics exposed a number of fussy, but important details. Encoded in this formalism is the regular Newton’s Second law and also momentum conservation, but the wrapper is elegant and (accidentally? No. Nature doesn't do accidentally) identically important in quantum mechanics and relativity. What Noether found was that this formalism included a hidden surprise. That surprise was how it would react if some of the terms were modified in particular ways.

```{figure} ./../_images/energy/emmySenior.png
---
width: 350px
name: emmySenior
align: center
---
Emmy Noether later in life.
```

If we were to take Newton’s Second law, good old $F=ma$ and remember that the $a$ term includes space and time coordinates, $x$’s and $t$’s, we can modify their appearance in the equation in particular ways. Suppose I were to take the appearance of every coordinate variable, $x$ and change every one of them to $x+D$ where $D$ is a constant distance, like an inch or a mile. In effect, shifting every space coordinate by a specific amount. What would you expect to happen? Should the rules of Newton change? This is in essence asking if  Newton’s Second law works fine here, what if I’m not here, but I’m 20 miles away? Surely I can rely on Newton's 2nd law and so cars, buildings, plumbing, and everything else mechanical should still function normally. So the form of Newton's 2nd law shoud not care about that change of $x \to x+20$. My lawnmower works on the east side of my lawn as well as the west side of my lawn. And, the structure of the equation $F=ma$ is such that the added "20" would go away. (Calculus is required to see this specifically.)

What Noether’s theorem says is that this shifting of space coordinates actually speaks to an "invariance" that Newton’s Second law respects...its *form is not altered* – and so my lawnmower works all over the yard – no matter where I am in space. This is a symmetry of nature. Nature’s rules hold every*where* the same. And this symmetry has consequences that tumble out of her mathematical description of this symmetry in the hands of the fussy formalism that mechanics had become: momentum conservation falls right out.

<p class="pullquote"  markdown="1">
Symmetries in physics equations mean that a conservation law is at work.
</p>

But wait, there’s more. My lawnmower works the same today as it did yesterday. And the same at the beginning of the job as at the end of the job. That means that if I take Newton’s Second law...and everywhere that time, $t$ appears, I replace it with $t+P$, where $P$ is some constant, like 20 minutes or 24 hours. What tumbles out is another symmetry of nature and another conservation law: **Energy conservation.**

> Noether's Theorem states that the equations of physics will be invariant if a conservation law is respected by the universe and that if a conservation law is found, that there must be a symmetry in the equations that describe that phenomenon.

The remarkable consequence of these observations, is that we now can interpret our conservation laws as not an algebraic accident, or even because of an experimental result. No. Our conservation laws come about because nature requires that our mathematical rules are unchanged whether we use them today or tomorrow, or over there or over here. They hold every**where** and every**when**.

Boy, is this important! Using Noether’s Theorem as a recipe, we can pick a symmetry as a test and then ask what our formal mathematical description of nature implies about physical conservation laws. If the laws work out, then we’ve found a symmetry of nature. If the laws are not observed in experiment, then we can discard that symmetry as not one that works in our universe.

We’ll exploit this, but I’ve used the word "universe" many times. Let’s go there. To the universe, I mean.

You might benefit from <a href="https://qstbb.pa.msu.edu/storage/isp220_video_2019/7_energy/" target="_blank">7.9_emmy_v1 </a>
for review and wrap-up of these sections.
