"""
Convert scipy.sparse matrices between Python and R.

For a detailed comparison between the two languages‘,
sparse matrix environment, see this issue_.

.. _issue: https://github.com/flying-sheep/anndata2ri/issues/8

Here’s an overview over the matching classes

===================================================  ======================================================
R                                                    Python
===================================================  ======================================================
:rcls:`Matrix::dgCMatrix`                            :class:`~scipy.sparse.csc_matrix`\ ``(dtype=float64)``
:rcls:`Matrix::lgCMatrix`/:rcls:`Matrix::pgCMatrix`  :class:`~scipy.sparse.csc_matrix`\ ``(dtype=bool)``
:rcls:`Matrix::dgRMatrix`                            :class:`~scipy.sparse.csr_matrix`\ ``(dtype=float64)``
:rcls:`Matrix::lgRMatrix`/:rcls:`Matrix::pgRMatrix`  :class:`~scipy.sparse.csr_matrix`\ ``(dtype=bool)``
:rcls:`Matrix::dgTMatrix`                            :class:`~scipy.sparse.coo_matrix`\ ``(dtype=float64)``
:rcls:`Matrix::lgTMatrix`/:rcls:`Matrix::pgTMatrix`  :class:`~scipy.sparse.coo_matrix`\ ``(dtype=bool)``
:rcls:`Matrix::ddiMatrix`                            :class:`~scipy.sparse.dia_matrix`\ ``(dtype=float64)``
:rcls:`Matrix::ldiMatrix`                            :class:`~scipy.sparse.dia_matrix`\ ``(dtype=bool)``
===================================================  ======================================================
"""

from .conv import converter, activate, deactivate
from . import py2r, r2py


def py2rpy(obj: object):
    """
    Convert scipy sparse matrices objects to R sparse matrices. Supports:

    :class:`~scipy.sparse.csc_matrix` (dtype in {float32, float64, bool}) →
        :rcls:`Matrix::dgCMatrix` or :rcls:`Matrix::lgCMatrix`
    :class:`~scipy.sparse.csr_matrix` (dtype in {float32, float64, bool}) →
        :rcls:`Matrix::dgRMatrix` or :rcls:`Matrix::lgRMatrix`
    :class:`~scipy.sparse.coo_matrix` (dtype in {float32, float64, bool}) →
        :rcls:`Matrix::dgTMatrix` or :rcls:`Matrix::lgTMatrix`
    :class:`~scipy.sparse.dia_matrix` (dtype in {float32, float64, bool}) →
        :rcls:`Matrix::ddiMatrix` or :rcls:`Matrix::ldiMatrix`
    """
    return converter.py2rpy(obj)


def rpy2py(obj: object):
    """
    Convert R sparse matrices to scipy sparse matrices. Supports:

    :rcls:`Matrix::dgCMatrix`, :rcls:`Matrix::lgCMatrix`, or :rcls:`Matrix::pgCMatrix` →
        :class:`~scipy.sparse.csc_matrix` (dtype float64 or bool)
    :rcls:`Matrix::dgRMatrix`, :rcls:`Matrix::lgRMatrix`, or :rcls:`Matrix::pgRMatrix` →
        :class:`~scipy.sparse.csr_matrix` (dtype float64 or bool)
    :rcls:`Matrix::dgTMatrix`, :rcls:`Matrix::lgTMatrix`, or :rcls:`Matrix::pgTMatrix` →
        :class:`~scipy.sparse.coo_matrix` (dtype float64 or bool)
    :rcls:`Matrix::ddiMatrix` or :rcls:`Matrix::ldiMatrix` →
        :class:`~scipy.sparse.dia_matrix` (dtype float64 or bool)
    """
    return converter.rpy2py(obj)
