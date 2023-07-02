from datetime import datetime

import pytest
from src.calc_diff import calc_diff


class FakeDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        return datetime(2021, 11, 3, 9, 22, 29, tzinfo=tz)


class TestCalcDiff:
    @pytest.fixture
    def set_calcdiff_time_now(self, mocker):
        # mocker.patch('datetime.now', return_value=datetime(2014, 6, 2, 9, 22, 00))
        # mocker.patch.object('datetime.now', )
        mocker.patch("src.calc_diff.datetime", FakeDatetime)

    def test_fixed_start_and_end_static(self):
        case = {
            "start_time": "2021-11-03T09:22:28+00:00",
            "end_time": "2021-11-03T09:22:29+00:00",
        }
        result = calc_diff(case)
        expected = 1
        assert result == expected

    def test_fixed_stard_none_end(self, set_calcdiff_time_now):
        case = {
            "start_time": "2021-11-03T09:22:28+00:00",
            "end_time": None,
        }
        result = calc_diff(case)
        expected = 1
        assert result == expected

    def test_should_return_0_for_the_same_start_and_end(self):
        case = {
            "start_time": "2021-11-03T09:22:28+00:00",
            "end_time": "2021-11-03T09:22:28+00:00",
        }
        result = calc_diff(case)
        expected = 0
        assert result == expected

    def test_should_return_minus_for_end_earlier_than_start(self):
        case = {
            "start_time": "2021-11-03T09:22:28+00:00",
            "end_time": "2021-11-03T09:22:20+00:00",
        }
        result = calc_diff(case)
        expected = -8
        assert result == expected
