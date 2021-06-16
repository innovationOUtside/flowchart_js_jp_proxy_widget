__version__="0.0.3"

from .jp_flowchartjs import FlowchartMagics

def load_ipython_extension(ipython):
    ipython.register_magics(FlowchartMagics)
