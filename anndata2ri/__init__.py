"""
Converter between Python’s AnnData and R’s SingleCellExperiment.
"""


from get_version import get_version

__author__ = "Philipp Angerer"
__version__ = get_version(__file__)

del get_version


try:  # This is so that flit can import this. There must be a better way.
    from .conv import converter, activate, deactivate
    from . import py2r, r2py


    def py2rpy(obj: object):
        """
        Convert Python objects to R interface objects. Supports:

        - :class:`~anndata.AnnData` → :rcls:`SingleCellExperiment::SingleCellExperiment`
        """
        return converter.py2rpy(obj)


    def rpy2py(obj: object):
        """
        Convert R interface objects to Python objects. Supports:

        - :rcls:`SingleCellExperiment::SingleCellExperiment` → :class:`~anndata.AnnData`
        - :rcls:`S4Vectors::DataFrame` → :class:`~pandas.DataFrame`
        """
        return converter.rpy2py(obj)
except ImportError as e:
    import warnings

    warnings.warn(str(e), ImportWarning)
