import logging
from typing import List, Dict

from pandas import DataFrame

logger = logging.getLogger(__name__)


def check_duplicates(df: DataFrame, columns: List) -> Dict:
    """ Performs duplication checks in a DataFrame on given columns.
    :param df: DataFrame
    :param columns: List of columns
    :return: Dictionary containing count and samples.
    """
    try:
        df_duplicates = df[df.duplicated(subset=columns, keep=False)]
        count = len(df_duplicates)
        samples = df_duplicates.groupby(columns).size().reset_index(name='number_of_duplicates')
        return {'count': count, 'samples': samples}
    except KeyError as e:
        logger.error(f"Column name does not exist in dataframe {e}")
        raise
    except Exception as e:
        logger.error(f"Error in finding duplicates. Manual intervention is required {e}")
        # TODO Inform to development team - Integrate with slack , msteams or email.
        raise


def display(results: Dict, columns: List):
    """
    :param results: Dictionary contains count and samples.
    :param columns: columns list
    :return: none
    """
    logging.info(f"Duplicate total number of count {results.get('count')} for {columns}")
    logging.info(f"Dataframe with columns and number of duplicates...")
    logging.info(results.get('samples').head(5))
