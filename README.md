# `nbfilter`

[![PyPI version](https://badge.fury.io/py/nbfilter.svg)](https://pypi.org/project/nbfilter/)

Filter `.ipynb` ([`nbformat`](https://github.com/jupyter/nbformat)) files to improve integration with version control systems (VCS), specifically git.


## Setup

Install from [PyPI](https://pypi.python.org/pypi/nbfilter):

```sh
pip install nbfilter
```

### Use from the command line:

```sh
python -m nbfilter.clean < research.ipynb | sponge research.ipynb
```


### Integrate into `git`:

From your repository's root directory:

Run the following command to implement a filter called `ipynbfilter` in your `.git/config` settings:
```sh
git config filter.ipynbfilter.clean 'python -m nbfilter.clean'
```

Then run one of the following command sequences to trigger it for all files with the `.ipynb` extension:
```sh
printf '*.ipynb filter=ipynbfilter\n' >> .gitattributes # Apply filter for all contributors
git add .gitattributes
```
_or_:
```sh
printf '*.ipynb filter=ipynbfilter\n' >> .git/info/attributes # Apply filter for just me
```

To apply it to files that are already under source control (for example, so that diffing subsequent changes produces more intelligible results):
```sh
git add --renormalize . # (re-)apply filters to all files currently under source control
```
_or_:
```sh
git add --renormalize research.ipynb # (re-)apply filters to a single file
```


## References / alternatives

* Min RK's [`nbstripout` gist](https://gist.github.com/minrk/6176788) that started it all (licensed as "Public Domain").
  > git pre-commit hook for stripping output from IPython notebooks
* [`nbstripout`](https://github.com/kynan/nbstripout) is a [PyPI-published](https://pypi.org/project/nbstripout/) package that provides all its functionality through a `nbstripout` console script.

* StackOverflow question: [Using IPython notebooks under version control](https://stackoverflow.com/q/18734739)
* [Making Git and Jupyter Notebooks play nice](http://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/)
  uses [`jq`](https://stedolan.github.io/jq/) instead of Python to do the JSON modifications, for the sake of speed.
* [Jupyter notebooks and version control](http://droettboom.com/blog/2018/01/18/diffable-jupyter-notebooks/)
  discusses alternatives to the `.ipynb` file format that would natively improve `git diff`'ing
  (specifically, YAML with some additional constraints).


## License

Copyright (c) 2018 Christopher Brown. [MIT Licensed](LICENSE.txt).
