import pytest
import pandas as pd
from pandas.testing import assert_frame_equal
import logging

from utils import df_utils

logger = logging.getLogger(__name__)


@pytest.fixture
def duplicates_df():
    return pd.DataFrame(
        data=[
            ['A', 'a', 'x', 1],
            ['A', 'b', 'x', 1],
            ['A', 'c', 'x', 1],
            ['B', 'a', 'x', 1],
            ['B', 'b', 'x', 1],
            ['B', 'c', 'x', 1],
            ['A', 'a', 'y', 1],
            ['A', 'a', 'y', 1]
        ],
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )


@pytest.fixture
def no_duplicates_df():
    return pd.DataFrame(
        data=[
            ['A', 'a', 'x', 1],
            ['B', 'b', 'y', 2],
            ['C', 'c', 'z', 3]
        ],
        columns=['col_1', 'col_2', 'col_3', 'col_4']
    )


def test_check_duplicates_with_duplicates(duplicates_df):
    result = df_utils.check_duplicates(duplicates_df, ['col_1', 'col_2', 'col_3'])
    assert result['count'] == 2
    expected_samples = pd.DataFrame({
        'col_1': ['A'],
        'col_2': ['a'],
        'col_3': ['y'],
        'number_of_duplicates': [2]
    })
    assert_frame_equal(result['samples'], expected_samples)


def test_check_duplicates_without_duplicates(no_duplicates_df):
    result = df_utils.check_duplicates(no_duplicates_df, ['col_1', 'col_2', 'col_3'])
    assert result['count'] == 0


def test_check_duplicates_with_non_existing_column(no_duplicates_df):
    with pytest.raises(KeyError):
        df_utils.check_duplicates(no_duplicates_df, ['invalid_column'])
