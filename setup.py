from setuptools import setup; from Cython.Build import cythonize; setup(name='ssb', ext_modules=cythonize('ssb.pyx', language_level=3), zip_safe=False)
