"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

# __all__参数，只用于指定 from package import * 时，导入的包是哪些，不需要的包可以先不导入；
# __all__ 可以在模块级别暴露接口，形式如下：
# __all__ = ["foo", "bar"] 形式都是 list类型
# __all__ = [
# "foo",
# "bar",
# "egg",
# ]
# 这样修改一个暴露的接口只修改一行，方便版本控制的时候看 diff
