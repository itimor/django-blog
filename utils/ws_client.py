# -*- coding: utf-8 -*-
# author: itimor

a = """
<h2>JS代码</h2>
<pre class="codehilite"><code class="language-javascript">function test(){
    console.log(&quot;Hello world!&quot;);</code></pre>


<blockquote>
<p>哈啊哈哈大大
<em>恶趣味群翁群</em></p>

<img class="1231" src="./dadsa.ipg"/>
<p>eqeqw
312321</p>
<img class="1231" src="./dadsa.ipg"/>
</blockquote>
"""

import re

comp = re.compile(r'<img .*?src=".+.ipg"/>')
b = re.sub(comp, 'image', a)
print(b)
