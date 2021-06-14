from IPython.core.magic import register_cell_magic
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget
from pyflowchart import Flowchart

__version__="0.0.2"

@register_cell_magic
def flowchart_magic(line, cell):
    "Send code to flow charter."
    return FlowchartWidget().charter(cell, embed=True)

@register_cell_magic
def pyflowchart_magic(line, cell):
    "Generate flowchart code and send to flow charter."
    fc = Flowchart.from_code(cell)
    return FlowchartWidget().charter(str(fc.flowchart()), embed=True)