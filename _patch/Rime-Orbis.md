---
layout: post
excerpt: "Game Patch"
title: "Rime"
---

<!-- # {{ page.title }} -->

{% include_relative index.md %}

[Installation Guide](/install-instructions/)

## Resolution Patch

Author: [illusion](https://twitter.com/illusion0002)

This patch was made and tested on Base Hardware. not sure if PS4 Pro outputs at 4K or 1080, experiment for yourself what works best.

In file `eboot.bin`

<details>
<summary>Code 1.00 (Click to Expand)</summary>

{% highlight none %}
48 8B 1D 82 FF 26 02

# 720p for Base PS4

C7 03 0A 57 85 42 90

# 900p for PS4 Pro

C7 03 7F AA A6 42 90

# 0A 57 85 42 = 66.67f
# 7F AA A6 42 = 83.33f 900p
{% endhighlight %}

</details>
