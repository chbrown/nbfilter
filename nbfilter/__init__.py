__version__ = 'N/A'

try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution('nbfilter').version
except Exception:
    pass
