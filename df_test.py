import logging.config
from typing import Dict

import pandas as pd

from utils import df_utils

logging.config.fileConfig('log_conf.yaml', disable_existing_loggers=False)

logging.info("Preparing a sample dataframe...")
df_1 = pd.DataFrame(
    data=[
        ['A', 'a', 'x', 1],
        ['A', 'b', 'x', 1],
        ['A', 'c', 'x', 1],
        ['B', 'a', 'x', 1],
        ['B', 'b', 'x', 1],
        ['B', 'c', 'x', 1],
        ['A', 'a', 'y', 1],
    ],
    columns=['col_1', 'col_2', 'col_3', 'col_4']
)
logging.info("Sample dataframe created.")

columns = ['col_1']
result: Dict = df_utils.check_duplicates(df_1, columns=columns)
df_utils.display(result, columns=columns)

columns = ['col_1', 'col_2']
result: Dict = df_utils.check_duplicates(df_1, columns)
df_utils.display(result, columns=['col_1', 'col_2'])

columns = ['col_1', 'col_2', 'col_3']
result: Dict = df_utils.check_duplicates(df_1, columns=columns)
df_utils.display(result, columns=columns)
