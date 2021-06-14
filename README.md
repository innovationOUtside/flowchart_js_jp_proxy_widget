# `flowchart_js_jp_proxy_widget`

[jp_proxy_widget](https://github.com/AaronWatters/jp_proxy_widget) class wrapper for [flowchart.js](https://flowchart.js.org/)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/flowchart_js_jp_proxy_widget/master?filepath=demo.ipynb)

## IPyhton magic to render `flowchart.js` flowcharts

![](flowchart_js_magic.png)

We can also script the production of the flowchart:

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


We can also define a couple of really simple magics:

```python
from IPython.core.magic import register_cell_magic

@register_cell_magic
def flowchart_magic(line, cell):
    "Send code to simulator."
    return FlowchartWidget().charter(cell, embed=True)
    
    
@register_cell_magic
def pyflowchart_magic(line, cell):
    "Generate flowchart code and send to flow charter."
    fc = Flowchart.from_code(cell)
    return FlowchartWidget().charter(str(fc.flowchart()), embed=True)
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


![](images/pyflowchart_magic.png)

If you `import jp_flowchartjs.jp_flowchartjs` the magics will be available.
