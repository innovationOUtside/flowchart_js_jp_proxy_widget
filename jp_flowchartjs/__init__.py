from IPython.core.magic import register_cell_magic

@register_cell_magic
def flowchart_magic(line, cell):
    "Send code to simulator."
    return FlowchartWidget().charter(cell, embed=True)
