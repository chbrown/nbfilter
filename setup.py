import setuptools

setuptools.setup(
    name='nbfilter',
    version='1.0.0',
    author='Christopher Brown',
    author_email='io@henrian.com',
    description='Filter .ipynb (nbformat) files to improve integration with version control systems (VCS)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chbrown/nbfilter',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'nbformat>=4',
    ],
    zip_safe=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
    ),
)
