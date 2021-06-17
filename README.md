# `flowchart_js_jp_proxy_widget`

[jp_proxy_widget](https://github.com/AaronWatters/jp_proxy_widget) class wrapper for [flowchart.js](https://flowchart.js.org/)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/flowchart_js_jp_proxy_widget/master?filepath=demo.ipynb)


## Installation

Installation is currently from Github only:

```
pip install --upgrade git+https://github.com/innovationOUtside/flowchart_js_jp_proxy_widget.git
```

## Flowchart widget to render `flowchart.js` flowcharts

Script the production of a flowchart:

```python
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget

fcode='''
st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
'''

testEmbed = FlowchartWidget()
testEmbed.charter(fcode)
testEmbed
```

- return SVG embed: `testEmbed.embed_svg()`
- return SVG data: `testEmbed.get_svg()`
- return PNG embed: `testEmbed.embed_png()`
- return PNG raw: `testEmbed.getpng()`
- oneliner return SVG: `FlowchartWidget().charter(fcode, embed=True)`


Using [`cdfmlr/pyflowchart`](https://github.com/cdfmlr/pyflowchart/), we can create a flowchart from the AST (abstract syntax tree) of a function definition:

```python
from pyflowchart import Flowchart

fc = Flowchart.from_code(cell)
fc_text = str(fc.flowchart()

# Render
FlowchartWidget().charter(fc_text, embed=True)
```


## Magics

We can also use magics:

![](images/flowchart_magic.png)


Load in the magics:

```
%load_ext jp_flowchartjs 
```

and then call as:

```python
%%flowchart_magic

st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
```


And:

```python
%%pyflowchart_magic 
import time

def demo(msg='demo'):
    for i in range(10):
        print(f'{msg} loopcount is {i}')
        time.sleep(i)
```
