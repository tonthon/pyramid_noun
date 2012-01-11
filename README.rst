Pyramid Noun : Scaffold for pyramid projects
============================================

Overview
--------

pyramid_noun is a package providing a default scaffolder for creating web apps.
Some default choices are made ::

     sqlalchemy as orm
     mako as templating engine
     LAB js to import javascript
 
Installation
------------

Obtain the source code from the git repository:

.. code-block:: text
    
    git clone https://github.com/tonthon/pyramid_noun.git

Install it with your setup.py

.. code-block:: text

   cd pyramid_noun
   python setup.py develop

Generating your project
-----------------------

.. code-block:: text
    
    $myvenv/bin/pcreate -s pyramid_noun MyProject


This will create a project called MyProject containing a package myproject.
This generated package which will become your definitive software needs to be installed.

.. code-block:: text

    cd MyProject
    python setup.py develop
