import os, sys
from setuptools import find_packages, setup


PYTHON3 = sys.version_info > (3, )
HERE = os.path.abspath(os.path.dirname(__file__))


def readme():
    with open(os.path.join(HERE, 'README.md')) as f:
        return f.read()


def get_version():
    with open(os.path.join(HERE, 'gmail_cli/__init__.py'), 'r') as f:
        content = ''.join(f.readlines())
    env = {}
    if PYTHON3:
        exec(content, env, env)
    else:
        compiled = compile(content, 'get_version', 'single')
        eval(compiled, env, env)
    return env['__version__']


setup(
    name='gmail-cli',
    version=get_version(),
    description='Command-line grep for GMail',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        "Topic :: System :: Distributed Computing",
        "Topic :: System :: Networking",
    ],
    keywords='GMail CLI grep',
    url='https://github.com/ckandoth/gmail-cli',
    author='Cyriac Kandoth',
    author_email='ckandoth@gmail.com',
    license='Apache',
    packages=find_packages(),
    scripts=['bin/gmail-grep'],
    install_requires=['google-api-python-client'],
    include_package_data=True,
    zip_safe=False
)
