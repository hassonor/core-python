"""
<<<<<<<< Modules >>>>>>>>>
-> Python's basic tool for organizing code
-> Normally a single Python source file
-> Load modules with import
-> Represented by module objects
"""

"""
<<<<<<<< Package vs. Modules >>>>>>>>>
 package                module.py
 |--------module.py     (Modules are generally files)
"""

"""
<<<<<<<< sys.path >>>>>>>>>
-> List of directories 
-> Searched in order in import
-> First match provides module
-> ImportError -> when there is no match
"""

"""
<<<<<< PYTHONPATH >>>>>>>>>
Environment variable
-> List paths added to sys.path
   | Windows |
   > set PYTHONPATH=path1;path2;path3
   | Linux/macOS | 
    $ export PYTHONPATH=path1:path2:path3
    
    <Full Details>
    -> sys.path: docs.python.org/3/library/sys.html#sys.path
    -> PYTHONPATH: docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
"""

"""
Summary:
-> All modules in hierarchy are imported
    -> Only the first name is bound
    -> Use fully-qualified names for submodules
    
-> Package directory paths are stored in __path__
-> sys.path controls modules search
    -> It is initialized from PYTHONPATH
"""
