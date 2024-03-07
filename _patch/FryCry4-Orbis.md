---
layout: post
excerpt: "Game Patch"
title: "Fry Cry: 4"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## 60 FPS Unlock

CPU+GPU Limited. For use with 9th generation of game consoles.

[Video](https://media.discordapp.net/attachments/650395105479360514/865565480357068800/0_46.mp4)

Author: [illusion](https://twitter.com/illusion0002)

In file `eboot.bin`

<details>
<summary>Code 1.07 (Click to Expand)</summary>

{% highlight none %}
85 F6 74 1C 3B 35 CF 1F C8 02 74 14 89 35 C7 1F C8 02 41 8B BD 00 02 00 00 FF CE

BE 00 00 00 00 41 8B BD 00 02 00 00 EB 0D C7 1F C8 02 41 8B BD 00 02 00 00 FF CE
{% endhighlight %}

</details>
