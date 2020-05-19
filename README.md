# flowchart_js_jp_proxy_widget
jp_proxy_widget class wrapper for [flowchart.js](https://flowchart.js.org/)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/innovationOUtside/flowchart_js_jp_proxy_widget/master)

*There is probably a much cleaner way of importing the js packages and creating a cell magic that can take flowchart descriptions and render them (eg [`anhi/nb-flowchartjs`](https://github.com/anhi/nb-flowchartjs) may provide a clue as to that approach?), but I was testing this approach as a more general pattern. Magic to follow...*

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

- return SVG embed: `testEmbed.get_svg()`
- return SVG data: `testEmbed.get_svg_data()`
- return PNG embed: `testEmbed.get_png()`
- oneliner return SVG: `FlowchartWidget().charter(fcode, embed=True)`

We can also define a really simple magic:

```python
from IPython.core.magic import register_cell_magic

@register_cell_magic
def flowchart_magic(line, cell):
    "Send code to simulator."
    return FlowchartWidget().charter(cell, embed=True)
 ```

and then call as:

```
%%flowchart_magic

st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
```
