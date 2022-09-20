# encoding: utf-8
import time

from CheckmarxPythonSDK.CxPortalSoapApiSDK import (
    add_license_expiration_notification,
    create_new_preset, create_scan_report,
    delete_preset,
    export_preset,
    export_queries,
    get_compare_scan_results,
    get_import_queries_status,
    get_query_collection,
    get_query_id_by_language_group_and_query_name,
    get_preset_list,
    get_server_license_data,
    get_server_license_summary,
    delete_project,
    delete_projects,
    get_version_number,
    get_version_number_as_int,
    get_path_comments_history,
    get_user_profile_data,
    get_queries_categories,
    get_name_of_user_who_marked_false_positive_from_comments_history,
    import_preset,
    import_queries,
    lock_scan,
    unlock_scan,
    get_results_for_scan,
    get_result_path,
)


def test_add_license_expiration_notification():
    response = add_license_expiration_notification()
    assert response.get("IsSuccesfull") is True


def test_create_new_preset():
    response = create_new_preset(query_ids=[343], name="ddd10")
    assert response['IsSuccesfull'] is True


def test_create_scan_report():
    response = create_scan_report(
        scan_id=1000005,
        report_type='PDF',
        results_per_vulnerability_maximum=500,
        display_categories_all=False,
        display_categories_ids=list(range(30, 62))
    )
    assert response["IsSuccesfull"] is True
    assert response["ID"] > 0


def test_delete_preset():
    response = delete_preset(preset_id=120006)
    assert response["IsSuccesfull"] is True


def test_delete_project():
    response = delete_project(project_id=3)
    assert response["IsSuccesfull"] is True


def test_delete_projects():
    response = delete_projects(project_ids=[8], flag="OnlyAllowedProjects")
    assert response["IsSuccesfull"] is True


def test_export_preset():
    response = export_preset(preset_id=100000)
    assert response.get("Preset") is not None
    # with open("preset.xml", "wb") as out_file:
    #     out_file.write(response.get("Preset"))


def test_export_queries():
    response = export_queries(queries_ids=[100000, 100001, 100002, 100003, 100004])
    assert response is not None
    # with open("query.xml", "wb") as out_file:
    #     out_file.write(response.get("Queries"))


def test_get_compare_scan_results():
    old_scan_id = 1050162
    new_scan_id = 1050164
    response = get_compare_scan_results(old_scan_id=old_scan_id, new_scan_id=new_scan_id)
    assert response is not None

def test_get_path_comments_history():
    scan_id = 1000022
    path_id = 5
    label_type = 'Remark'
    response = get_path_comments_history(scan_id=scan_id, path_id=path_id, label_type=label_type)
    assert response.get("IsSuccesfull") is True


def test_get_user_profile_data():
    response = get_user_profile_data()
    assert response.get("ProfileData") is not None


def test_get_queries_categories():
    response = get_queries_categories()
    assert len(response["QueriesCategories"]) > 1


def test_get_query_collection():
    response = get_query_collection()
    assert response is not None


def test_get_query_id_by_language_group_and_query_name():
    response = get_query_id_by_language_group_and_query_name(query_name="Find_URL_Query_String_Creating_URI")
    assert isinstance(response, int)

    response = get_query_id_by_language_group_and_query_name()
    assert isinstance(response, list)

    response = get_query_id_by_language_group_and_query_name(package_type_name="Corp")
    assert isinstance(response, list)


def test_get_name_of_user_who_marked_false_positive_from_comments_history():
    scan_id = 1010002
    path_id = 1
    response = get_name_of_user_who_marked_false_positive_from_comments_history(scan_id=scan_id, path_id=path_id)
    assert response is not None


def test_get_preset_list():
    response = get_preset_list()
    assert response["IsSuccesfull"] is True


def test_get_result_path():
    response = get_result_path(scan_id=1000006, path_id=1)
    assert response["IsSuccesfull"] is True

def test_get_results_for_scan():
    response = get_results_for_scan(scan_id=1000006)
    assert response["IsSuccesfull"] is True

def test_get_server_license_data():
    lic = get_server_license_data()
    assert lic is not None


def test_get_server_license_summary():
    lic = get_server_license_summary()
    assert lic is not None


def test_get_version_number():
    version = get_version_number()
    assert version is not None


def test_get_version_number_as_int():
    version = get_version_number_as_int()
    assert version > 800


def test_import_preset():
    imported_file_path = r"C:\Users\HappyY\Documents\SourceCode\GitHub\checkmarx-python-sdk\tests\preset.xml"
    response = import_preset(imported_file_path=imported_file_path)
    import_query_status = response.get("importQueryStatus")
    print("importQueryStatus: {}".format(import_query_status))
    request_id = response.get("requestId")
    while import_query_status not in ["Failed", "Succeeded"]:
        response = get_import_queries_status(request_id=request_id)
        import_query_status = response.get("importQueryStatus")
        print("importQueryStatus: {}".format(import_query_status))
        time.sleep(1)
    print("importQueryStatus: {}".format(import_query_status))
    assert import_query_status == "Succeeded"


def test_import_queries():
    imported_file_path = r"C:\Users\HappyY\Documents\SourceCode\GitHub\checkmarx-python-sdk\tests\query.xml"
    response = import_queries(imported_file_path=imported_file_path)
    import_query_status = response.get("importQueryStatus")
    print("importQueryStatus: {}".format(import_query_status))
    request_id = response.get("requestId")
    while import_query_status not in ["Failed", "Succeeded"]:
        response = get_import_queries_status(request_id=request_id)
        import_query_status = response.get("importQueryStatus")
        print("importQueryStatus: {}".format(import_query_status))
        time.sleep(1)
    print("importQueryStatus: {}".format(import_query_status))
    assert import_query_status == "Succeeded"


def test_lock_scan():
    scan_id = 1040138
    response = lock_scan(scan_id=scan_id)
    assert response.get("IsSuccesfull") is True


def test_unlock_scan():
    scan_id = 1040138
    response = unlock_scan(scan_id=scan_id)
    assert response.get("IsSuccesfull") is True
