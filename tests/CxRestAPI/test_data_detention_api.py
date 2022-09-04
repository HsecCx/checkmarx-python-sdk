# encoding: utf-8

"""
    tests.test_data_detention_api

    :copyright Checkmarx
    :license MIT

"""
import time

from CheckmarxPythonSDK.CxRestAPISDK import DataRetentionAPI


def test_define_data_retention_date_range():
    data_retention_api = DataRetentionAPI()
    start_date = "2022-01-23"
    end_date = "2022-01-24"
    duration_limit_in_hours = 1
    data_retention = data_retention_api.define_data_retention_date_range(start_date, end_date, duration_limit_in_hours)
    assert data_retention is None


def test_stop_data_retention():
    data_retention_api = DataRetentionAPI()
    result = data_retention_api.stop_data_retention()
    time.sleep(5)
    assert result is True


def test_define_data_retention_by_number_of_scans():
    data_retention_api = DataRetentionAPI()
    number_of_successful_scans_to_preserve = 10
    duration_limit_in_hours = 1
    data_retention = data_retention_api.define_data_retention_by_number_of_scans(number_of_successful_scans_to_preserve,
                                                                                 duration_limit_in_hours)
    assert data_retention is None


def test_define_data_retention_by_rolling_date():
    data_retention_api = DataRetentionAPI()
    num_days = 3
    duration_limit_in_hours = 1
    data_retention = data_retention_api.define_data_retention_by_rolling_date(num_days, duration_limit_in_hours)
    assert data_retention is None


def test_delete_all_scans_older_than_num_of_months():
    data_retention_api = DataRetentionAPI()
    num_months = 6
    duration_limit_in_hours = 1
    data_retention = data_retention_api.define_data_retention_by_rolling_months(num_months, duration_limit_in_hours)
    assert data_retention is None
