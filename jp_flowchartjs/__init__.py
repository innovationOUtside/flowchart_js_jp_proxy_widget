from IPython.core.magic import register_cell_magic
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget

__version__="0.0.1"

@register_cell_magic
def flowchart_magic(line, cell):
    "Send code to simulator."
    return FlowchartWidget().charter(cell, embed=True)
