import re
import sys
import nbformat


def _delete(d, *keys):
    for key in keys:
        if key in d:
            del d[key]


def _clear(d, *keys):
    for key in keys:
        if key in d:
            if hasattr(d[key], 'clear'):
                d[key].clear()
            else:
                d[key] = None


def trim_trailing_whitespace(source):
    '''
    Trim whitespace from end of lines in `source`
    '''
    # \s is too greedy: it might capture newlines despite re.M flag
    return re.sub(r'[ \t]+$', '', source, flags=re.MULTILINE)


def clean_notebook(notebook, trim=False):
    '''
    Clean all output from `notebook`, which is a
    nbformat.notebooknode.NotebookNode (https://git.io/NotebookNode)
    '''
    _delete(notebook['metadata'], 'signature')
    for worksheet in notebook.get('worksheets', [notebook]):
        # clean all output from this worksheet, in-place
        _delete(worksheet['metadata'], 'widgets')
        for cell in worksheet['cells']:
            # clean all output from this cell, in-place
            _clear(cell, 'outputs', 'execution_count')
            # `prompt_number` was renamed to `execution_count` as of nbformat v4
            # (see https://github.com/jupyter/nbformat/commit/7faa614)
            _delete(cell, 'prompt_number')
            if 'metadata' in cell:
                _delete(cell['metadata'], 'collapsed', 'scrolled')
            if trim:
                # the 'source' field is a list of strings in the JSON serialization,
                # but it's parsed into a single string by nbformat.read
                cell['source'] = trim_trailing_whitespace(cell['source'])


def clean_file(fp_in, fp_out, trim=False):
    '''
    Clean all output from a file, writing the result to fp_out.
    '''
    notebook = nbformat.read(fp_in, nbformat.NO_CONVERT)
    clean_notebook(notebook, trim)
    nbformat.write(notebook, fp_out, nbformat.NO_CONVERT)


def main():
    from . import __version__
    import argparse
    parser = argparse.ArgumentParser(
        description='Filter .ipynb (nbformat) files')
    parser.add_argument('-v', '--version',
                        action='version',
                        version=__version__)
    parser.add_argument('-t', '--trim',
                        action='store_true',
                        help='trim trailing whitespace')
    parser.add_argument('-i', '--input',
                        help='input file (default: /dev/stdin)',
                        type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('-o', '--output',
                        help='output file (default: /dev/stdout)',
                        type=argparse.FileType('w'),
                        default=sys.stdout)
    opts = parser.parse_args()
    clean_file(opts.input, opts.output, opts.trim)


if __name__ == '__main__':
    exit(main())
