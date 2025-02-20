import re
from pathlib import Path

from opt import History
from pyfemtet.opt.interface._base import FEMInterface
from pyfemtet.opt.interface._surrogate._singletaskgp import PoFBoTorchInterface
from pyfemtet.opt.interface._excel_interface import (
    ExcelInterface, is_cell_value_empty, ParseAsObjective, ScapeGoatObjective,
    ParseAsConstraint, search_c, search_r
)


class PoFBoTorchInterfaceWithExcelSettingsInterface(
    PoFBoTorchInterface,
    ExcelInterface,
    FEMInterface,
):

    def __init__(
            self,

            # SurrogateModel
            history_path: str = None, train_history: History = None,
            _output_directions: dict[int, str | float] | list[str | float] = None,

            # Excel
            input_xlsm_path: str or Path = None,
            input_sheet_name: str = None,
            output_xlsm_path: str or Path = None,
            output_sheet_name: str = None,
            constraint_xlsm_path: str or Path = None,
            constraint_sheet_name: str = None,
            procedure_name: str = None,
            procedure_args: list or tuple = None,
            connect_method: str = 'auto',  # or 'new'
            procedure_timeout: float or None = None,
            setup_xlsm_path: str or Path = None,
            setup_procedure_name: str = None,
            setup_procedure_args: list or tuple = None,
            teardown_xlsm_path: str or Path = None,
            teardown_procedure_name: str = None,
            teardown_procedure_args: list or tuple = None,
            related_file_paths: list[str or Path] = None,
            visible: bool = False,
            display_alerts: bool = False,
            terminate_excel_when_quit: bool = None,
            interactive: bool = True,
            use_named_range: bool = True,
    ):
        PoFBoTorchInterface.__init__(
            self,
            history_path,
            train_history,
            _output_directions,
        )

        ExcelInterface.__init__(
            self,
            input_xlsm_path,
            input_sheet_name,
            output_xlsm_path,
            output_sheet_name,
            constraint_xlsm_path,
            constraint_sheet_name,
            procedure_name,
            procedure_args,
            connect_method,  # or 'new'
            procedure_timeout,
            setup_xlsm_path,
            setup_procedure_name,
            setup_procedure_args,
            teardown_xlsm_path,
            teardown_procedure_name,
            teardown_procedure_args,
            related_file_paths,
            visible,
            display_alerts,
            terminate_excel_when_quit,
            interactive,
            use_named_range,
        )
