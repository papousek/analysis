#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import commands.all
import commands.ab
import commands.model
import commands.importance
import commands.anatomy
import commands.paper
import output
from spiderpig import run_spiderpig
from config import get_argument_parser
import os


BASE_DIR = os.path.dirname(__file__)


if __name__ == '__main__':
    run_spiderpig(
        namespaced_command_packages={
            'ab': commands.ab,
            'all': commands.all,
            'model': commands.model,
            'imp': commands.importance,
            'anatomy': commands.anatomy,
            'paper': commands.paper,
        },
        argument_parser=get_argument_parser(),
        setup_functions=[output.init_plotting]
    )
