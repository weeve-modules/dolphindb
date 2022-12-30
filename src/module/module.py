"""
This file implements module's main logic.
Data outputting should happen here.

Edit this file to implement your module.
"""

import dolphindb as ddb
import numpy as np
import pandas as pd
from logging import getLogger
from .params import PARAMS

log = getLogger("module")

# Connect to DolphinDB servers
s = ddb.session()
if PARAMS['USERNAME'] and PARAMS['PASSWORD']:
    s.connect(PARAMS['HOST'], PARAMS['PORT'], PARAMS['USERNAME'], PARAMS['PASSWORD'])
else:
    s.connect(PARAMS['HOST'], PARAMS['PORT'])

# Prepare some helpful local variables for writing data to DB
s.run('tb = loadTable("{a}","{b}")'.format(a=PARAMS['DB_PATH'],b=PARAMS['TABLE_NAME']))


def module_main(received_data: any) -> str:
    """
    Send received data to the next module by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        str: Error message if error occurred, otherwise None.

    """

    try:
        # build pandas.DataFrame as it gives most flexibility with different DolphinDB databases and tables formats
        construct_dict = {}
        for i in range(len(PARAMS['COLUMNS'])):
            if type(received_data) == dict:
                if PARAMS['COLUMNS'][i] == PARAMS['DATE_COLUMN']:
                    # cast timestamp to datetime64[D]
                    construct_dict[PARAMS['COLUMNS'][i]] = np.array([received_data[PARAMS['LABELS'][i]]], dtype="datetime64[D]")
                else:
                    construct_dict[PARAMS['COLUMNS'][i]] = [received_data[PARAMS['LABELS'][i]]]
            else:
                if PARAMS['COLUMNS'][i] == PARAMS['DATE_COLUMN']:
                    construct_dict[PARAMS['COLUMNS'][i]] = np.array([d[PARAMS['LABELS'][i]] for d in received_data], dtype="datetime64[D]")
                else:
                    construct_dict[PARAMS['COLUMNS'][i]] = [d[PARAMS['LABELS'][i]] for d in received_data]
        df = pd.DataFrame(construct_dict)

        log.debug("Writing data...")
        script = 'tableInsert{tb}'
        s.run(script, df)

        return None

    except Exception as e:
        return f"Exception in the module business logic: {e}"
