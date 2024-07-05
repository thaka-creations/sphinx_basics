# SPHINX BASICS

## Installing sphinx
pip install sphinx sphinx_rtd_theme

## Step 1: Sphinx quick install
Run the below command inside your docs folder
```
sphinx-quickstart
```

## Step 2: Editing conf.py file
Go to conf.py file and update path to os.path.abspath('../..')

Under extension path, update the extension below
```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]
```

## Step 3: Generating .rst files
Till now, your docs folder has index.rstwhich’ll be the landing page of your documentation. But we haven’t generated maths.rst, which has our python code.

Go to the parent folder sphinx_basics, and run the command:

```sphinx-apidoc -o docs/source maths/```

## Step 4: Including module.rst and generating html
Now, include the generated modules.rst file in your index.rst

```
Welcome to Math Documentation's documentation!
==============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```

And then we’re all set to generate the beautiful documentation, go inside of your docs folder and run the command
```make clean```

Now, suppose you did some changes to your code and now you want to rebuild that HTML, Go to your docs folder and write

```
make clean
make html
```




