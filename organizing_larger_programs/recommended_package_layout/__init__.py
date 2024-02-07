"""
<<<<<<<<<< Recommended Python Project Structure >>>>>>>>>>>>
project_name / <<<<<<<<<<<<<<< Project root - not the package
    README.rst <<<<<<<<<<<<<<< Overview documentation
    docs/ <<<<<<<<<<<<<<< Project documentation
    src/ <<<<<<<<<<<<<<< Package/production code
        package_name/
        __init__.py
        more_source.py
        subpackage1/
            __init__.py
    tests/ <<<<<<<<<<<<<<< All tests for the project
        test_code.py
    setup.py
"""

"""
<<<README.rst / reStructuredText>>>
 ============
 Project Name
 ============
 A brief description of the project.
 
 Section 1
 ==========
 Installation or "quick start" information can go here.
 
 Subsection
 ----------
 Some details can go here.
 
<<<<Documentation>>>>
-> Can come in many forms (e.g Sphinx)
-> It should be east to find
-> README.rst should be in project root
    -> Common convention
    -> Often refers to docs directory

<<<src and sys.path>>>>
    project_name/
        src/
            package_name/
                __init__.py
                
NOTE: if project_name/ in the sys.path ... then package_name/ is not importable.

"""
