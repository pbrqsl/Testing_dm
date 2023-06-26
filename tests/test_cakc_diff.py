import pytest
from src import calc_diff
from src.calc_diff import calc_diff
from datetime import datetime, date
from freezegun import freeze_time


class TestCalcDiff:
    @pytest.fixture
    def set_calcdiff_time_now(self, mocker):
        mocker.patch('datetime.now', return_value=datetime(2014, 6, 2, 9, 22, 00))
        mocker.patch.object('datetime.now', )
    def test_fixed_start_and_end_static(self):
        case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': '2021-11-03T09:22:29+00:00',
        }
        result = calc_diff(case)
        expected = 1
        assert result == expected


    @freeze_time("2021-11-03T09:22:29")
    def test_fixed_stard_none_end(self):
        case = {
            'start_time': '2021-11-03T09:22:28+00:00',
            'end_time': None,
        }
        result = calc_diff(case)
        expected = 1
        assert result == expected

    def test_fixed_stard_none_end2(self, set_calcdiff_time_now):
        case = {
            'start_time': '2021-11-03T09:22:28+00:00',
            'end_time': None,
        }
        result = calc_diff(case)
        expected = 1
        assert result == expected




