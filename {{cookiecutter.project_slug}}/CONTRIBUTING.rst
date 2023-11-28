.. highlight:: shell

============
贡献的记录
============

欢迎贡献，我们将不胜感激！ 每一点点的贡献都会帮助到这个项目，进而帮助到更多的人。
我们会永远会感激并记录您的功劳。

您可以通过多种方式做出贡献：

贡献的不同方式
------------------

报告当前系统的 Bug
~~~~~~~~~~~~~~~~~~~~

提交Bug https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues.

如果您要报告错误，请包括：

* 您的操作系统名称和版本。
* 有关本地设置的任何可能有助于故障排除的详细信息。
* 重现错误的详细步骤。

修复当前系统的 Bugs
~~~~~~~~~~~~~~~~~~~~

查看 GitHub 问题以查找错误。 任何带有“bug”和“need help”标签的问题，都向任何想要实现它的人开放。

实现正在开发的功能特性
~~~~~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

书写当前系统的说明文档
~~~~~~~~~~~~~~~~~~~~~~~

{{ cookiecutter.project_name }} could always use more documentation, whether as part of the
official {{ cookiecutter.project_name }} docs, in docstrings, or even on the web in blog posts,
articles, and such.

提交使用中的反馈
~~~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

开始贡献你的力量和智慧！
---------------------------

Ready to contribute? Here's how to set up `{{ cookiecutter.project_slug }}` for local development.

1. Fork the `{{ cookiecutter.project_slug }}` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/{{ cookiecutter.project_slug }}.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv {{ cookiecutter.project_slug }}
    $ cd {{ cookiecutter.project_slug }}/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ flake8 {{ cookiecutter.project_slug }} tests
    $ python setup.py test or pytest
    $ tox

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

拉取请求指南
------------

在提交拉取请求之前，请检查它是否符合这些指导原则：

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.5, 3.6, 3.7 and 3.8, and for PyPy. Check
   https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/pull_requests
   and make sure that the tests pass for all supported Python versions.

技巧
-------

运行测试的子集::

{% if cookiecutter.use_pytest == 'y' -%}
    $ pytest tests.test_{{ cookiecutter.project_slug }}
{% else %}
    $ python -m unittest tests.test_{{ cookiecutter.project_slug }}
{%- endif %}

部署
---------

一个提示，用于提醒维护人员如何部署。
确保所有更改都已提交(包括HISTORY.rst中的一个条目)。
然后运行::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags

如果测试通过，Travis将部署到PyPI。
