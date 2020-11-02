  
from setuptools import setup

from os import path

def get_long_description():
    with open(
        path.join(path.dirname(path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

def get_requirements(fn='requirements.txt', nogit=True):
   """Get requirements."""
   if path.exists(fn):
      with open(fn, 'r') as f:
        requirements = f.read().splitlines()
   else:
     requirements = []
   requirements = [r.split()[0].strip() for r in requirements if r and not r.startswith('#')]
   if nogit:
       requirements = [r for r in requirements if not r.startswith('git+')]
   return requirements

requirements = get_requirements()

print(f'Requirements: {requirements}')

setup(name='jp_flowchartjs',
    author='Tony Hirst',
    author_email='tony.hirst@open.ac.uk',
    url='https://github.com/innovationOUtside/flowchart_js_jp_proxy_widget',
    description='IPython/Jupyter notebook magic for generating JS flowcharts.',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license='MIT License',
    packages=['jp_flowchartjs'],
    # Dependencies
    install_requires=requirements,
    #setup_requires=[],
    
    # Packaging
    #entry_points="",
    include_package_data=True,
    zip_safe=False,

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'License :: Free For Educational Use',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
)
