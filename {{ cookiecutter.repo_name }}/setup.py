from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    packages=find_packages(''),
    package_dir={"": "src"},
    packages=['{{ cookiecutter.project_name }}',
        '{{ cookiecutter.project_name }}.features',
        '{{ cookiecutter.project_name }}.visualization',
        '{{ cookiecutter.project_name }}.data',
        ],
    package_dir={'{{ cookiecutter.project_name }}': '{{ cookiecutter.project_name }}'},
)
