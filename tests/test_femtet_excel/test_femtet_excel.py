import os
from pyfemtet.opt import FEMOpt

from pyfemtet.opt.interface._femtet_excel import FemtetWithExcelSettingsInterface

import pytest


def test_femtet_with_excel_settings():

    os.chdir(os.path.dirname(__file__))

    fem = FemtetWithExcelSettingsInterface(
        femprj_path='sample.femprj',
        input_xlsm_path='sample.xlsm',
        input_sheet_name='sample',
        parametric_output_indexes_use_as_objective={0: 'minimize'}
    )

    femopt = FEMOpt(fem=fem)

    femopt.optimize(n_trials=4, n_parallel=2, confirm_before_exit=False)
