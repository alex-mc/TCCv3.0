#!python

from distutils.core import setup, Extension

test_module = Extension('_bct30_swig',
                        include_dirs = ['C:/Users/Alex/Google Drive/MRO/TCCv3.0/'],
                        libraries = ['bct30.h', 'indiapi.h'],
                        sources=['bct30_wrap.cxx', 'bct30.cpp'],
                        )

print('made it')
setup (name = 'bct30',
       version = '0.1',
       author = "Alex McMaster",
       description = """A test module""",
       ext_modules = [test_module],
       py_modules = ['bct30_swig'],
       )
