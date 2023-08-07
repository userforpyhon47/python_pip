from setuptools import setup

setup(
    name="crud",
    version="0.1",
    py_modules=[],
    install_requires=['click'],
    entry_points="""
                [console_scripts]
                crud=crud:main
"""
)

# pip install --editable 