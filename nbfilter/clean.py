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


def clean_notebook(notebook):
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


def clean_file(fp_in, fp_out):
    '''
    Clean all output from a file, writing the result to fp_out.
    '''
    notebook = nbformat.read(fp_in, nbformat.NO_CONVERT)
    clean_notebook(notebook)
    nbformat.write(notebook, fp_out, nbformat.NO_CONVERT)


def main():
    clean_file(sys.stdin, sys.stdout)


if __name__ == '__main__':
    exit(main())
