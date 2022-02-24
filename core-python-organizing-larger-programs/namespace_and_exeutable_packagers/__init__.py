"""
PEP 420: Implicit Namespace Packages
"Namespace packages are a mechanism for splitting a single Python package
across multiple directories on disk."

python.org/dev/peps/pep-0420/
"""
"""
<<< Namespace Package Discovery Algorithm >>>
-> Scan each directory in sys.path
-> Import standard package if found
-> Import standard module if found
-> Otherwise, all matching directories 
    contribute to a namespace package
"""

"""
<<<<<<<<<<<< Executing Directories vs. Packages >>>>>>>>>>>>>>>>>
    python directory        |        python -m directory
    Executing a directory   |        - The "-m" tells Python to treat it a s a module
    
    "directory" added to sys.path |   "directory" treated like a package
    "directory/__main__.py" is not in a package | "directory/__main__.py" is a submodule of the directory package
"""

"""
__init__.py vs __main__.py
-> __init__.py: can execute any code it likes on import...
-> __main__.py: only a package with __main__.py can be executed
"""

"""
Summary:
-> Construct packages from multiple directories with  namespace packages
-> Namespace packages cannot contain __init__.py
-> Directories can be made executable with __main__.py
-> Python can execute zip files like directories
-> Packages can be both importable and executable with __main__.py
"""
