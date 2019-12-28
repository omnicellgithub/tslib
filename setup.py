from setuptools import setup

setup(
    name='tslib',
    version='0.1',
    description='none',
    url='https://github.com/jehangiramjad/tslib',
    author='Vishal Misra',
    author_email='vishal.misra@columbia.edu',
    license='Private',
    package_dir = {
            'tslib': 'tslib',
            'tslib.src': 'tslib\\src',
            'tslib.tests': 'tslib\\tests'},
    packages=['tslib', 'tslib.src',
                  'tslib.tests'],    
    python_requires='>=3.6',
    install_requires=[
    ],
    zip_safe=False
)
