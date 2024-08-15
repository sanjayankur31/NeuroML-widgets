.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/sanjayankur31/neuroml_widgets/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

neuroml-widgets could always use more documentation, whether as part of the
official neuroml-widgets docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/sanjayankur31/neuroml_widgets/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `neuroml_widgets` for local development.

1. Fork the `neuroml_widgets` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/neuroml_widgets.git

3. It is best to use `virtual environments <https://docs.python.org/3/tutorial/venv.html>`__ when developing Python packages::

    $ python -m venv .venv ; source ./venv/bin/activate
    $ cd neuroml_widgets/
    $ pip install -e .[dev]   # for an editable install

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. Run all tests::

    $ pytest


6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Code style
~~~~~~~~~~

1. The source code uses spaces, and each tab is equivalent to 4 spaces.

2. We use the [reStructuredText (reST)
   format](https://stackoverflow.com/a/24385103/375067) for Python docstrings.
   Please document your code when opening pull requests.
   All methods/functions/modules *must* include docstrings that explain the parameters.

3. We use [ruff](https://pypi.org/project/ruff/) to format and lint our code. (See the section on pre-commit below.)

4. Please use [type hints](https://docs.python.org/3/library/typing.html) wherever applicable.
   You can set up type checkers such as [mypy](https://mypy.readthedocs.io/) to use type hints in your development environment/IDE.


        pip install mypy


Pre-commit
~~~~~~~~~~

A number of `pre-commit <https://pre-commit.com/>` hooks are used to improve code-quality.
Please run the following code to set up the pre-commit hooks:

    $ pre-commit install

The hooks will be run at each `git commit`.
Please see `.pre-commit-config.yaml` for information on what hooks we run.


Commit messages
~~~~~~~~~~~~~~~

Writing good commit messages makes things easy to follow.
Please see these posts:

- `How to write a Git commit message <https://cbea.ms/git-commit/>`__
- While not compulsory, we prefer `conventional commits <https://www.conventionalcommits.org/en/v1.0.0/>`__


Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. Please contribute pull requests against the `development` branch.
2. The pull request should include tests.
3. Please ensure that the automated build for your pull request passes.
4. Please write good commit messages (see the section above).

Tips
----

To run a subset of tests::

$ pytest tests.test_neuroml_widgets

Updating your pull request branch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Over time, as pull requests are reviewed, the `development` branch continues to move on with other changes.
Sometimes, it can be useful/necessary to pull in these changes to the pull request branch, using the following steps.

Add the upstream pyNeuroML repository as a remote::


    git remote add upstream https://github.com/NeuroML/pyNeuroML.git


Update your local copy of the `development` branch, and the remote copy in your fork::


    git checkout development
    git pull upstream development
    git push


Pull in changes from development to your branch::


    git checkout <feature branch being used for PR>
    git merge development


If there are merge conflicts, you will need to [resolve these](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging#_basic_merge_conflicts), since merging the feature branch in the pull request will also result in these.
After any merge conflicts have been resolved (or if there aren't any), you can
push your branch to your fork to update the pull request::


    git push


Code of Conduct
---------------

Please note that this project is released with a `Contributor Code of Conduct`_.
By participating in this project you agree to abide by its terms.

.. _`Contributor Code of Conduct`: CODE_OF_CONDUCT.rst
