.. highlight:: shell

============
安装指南
============


稳定版本释放
----------------

如果需要安装 {{ cookiecutter.project_name }}, 在你的终端中运行以下命令：

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

如果你没有安装 `pip`_ , 以下链接 `Python installation guide`_ 能够指导你完成基础的准备工作。

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


源代码
------------

项目 {{ cookiecutter.project_name }} 的源代码可以从 `Github repo`_ 直接下载。

你也可以从以下的公共代码库克隆复制：

.. code-block:: console

    $ git clone git://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

或者选在下载压缩包 `tarball`_ ：

.. code-block:: console

    $ curl -OJL https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master

一旦你下载成功源代码的拷贝，可以使用以下的命令进行安装：

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tarball/master
