#!python

from distutils.core import setup, Extension

example_module = Extension('_bct30_sim',
                           sources=['bct30_sim_wrap.cxx', 'bct30_sim.cpp'],
                           )

setup(name='bct30_sim',
      version='0.1',
      author='Alex McMaster',
      description="""BCT30 Simulator.""",
      ext_modules=['bct30_sim_module'],
      py_modules=['bct30_sim'],
      )
