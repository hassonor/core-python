"""
<<<Extending Packages with Plugins>>>
-> Packages defines extension points.
-> Extensions are implemented outside the package.
-> Extension are discovered at runtime.
-> We'll look at two methods.
    -> Namespace package and pkgutil

<<<Implementing Plugins with Namespace Packages>>>
-> Core package designates subpackages as extension points.
-> Core package scans subpackages at runtime to discover plugins.
-> Plugins augment the namespace package's extensible subpackages.

<<<Implementing Plugins with setuptools Entry Points>>>
-> Define extension points using setuptools
-> Plugins add to extension points in setup.py
-> Core package iterates over plugins added to extension points.
"""

"""
Summary:
-> A project structure that supports all aspects of code construction
-> Separating production and test code
-> Install packages into a Python environment
-> Use plugins to extend packages
    -> Namespace packages
    -> setuptools
"""
