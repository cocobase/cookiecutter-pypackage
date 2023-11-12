.. highlight:: shell

============
安装指南
============


Stable release
--------------

如果需要安装 {{ cookiecutter.project_name }}, 在你的终端中运行以下命令：

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

如果你没有安装 `pip`_ , 以下链接 `Python installation guide`_ 能够指导你完成基础的准备工作。

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
