from CheckmarxPythonSDK.CxOne.scaAPI import ScaAPI


def test_get_projects():
    projects = ScaAPI().get_all_projects()
    assert projects is not None


def test_get_number_of_vulnerabilities_risks_by_scan_id():
    result = ScaAPI().get_number_of_vulnerabilities_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                     is_exploitable_path_enabled=False)
    assert result is not None


def test_get_number_of_supply_chain_risks_by_scan_id():
    result = ScaAPI().get_number_of_supply_chain_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_number_of_outdated_packages_by_scan_id():
    result = ScaAPI().get_number_of_outdated_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_number_of_legal_risks_by_scan_id():
    result = ScaAPI().get_number_of_legal_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_vulnerabilities_risks_by_scan_id():
    result = ScaAPI().get_vulnerabilities_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                           take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_vulnerabilities_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                  take=10, skip=10)
    assert second_result is not None


def test_get_supply_chain_risks_by_scan_id():
    result = ScaAPI().get_supply_chain_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                        take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_supply_chain_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                               take=10, skip=10)
    assert second_result is not None


def test_get_legal_risks_by_scan_id():
    result = ScaAPI().get_legal_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                 take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_legal_risks_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                        take=10, skip=10)
    assert second_result is not None


def test_get_direct_third_party_packages_by_scan_id():
    result = ScaAPI().get_direct_third_party_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                 take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_direct_third_party_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                        take=10, skip=10)
    assert second_result is not None


def test_get_transitive_third_party_packages_by_scan_id():
    result = ScaAPI().get_transitive_third_party_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                     take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_transitive_third_party_packages_by_scan_id(
        scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
        take=10, skip=10)
    assert second_result is not None


def test_get_number_of_packages_by_scan_id():
    result = ScaAPI().get_number_of_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_number_of_direct_third_party_packages_by_scan_id():
    result = ScaAPI().get_number_of_direct_third_party_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_number_of_transitive_third_party_packages_by_scan_id():
    result = ScaAPI().get_number_of_transitive_third_party_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_number_of_packages_used_for_accessing_saas_services():
    result = ScaAPI().get_number_of_packages_used_for_accessing_saas_services(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None


def test_get_container_packages_by_scan_id():
    result = ScaAPI().get_container_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                        take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_container_packages_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                               take=10, skip=10)
    assert second_result is not None


def test_get_container_vulnerabilities_by_scan_id():
    result = ScaAPI().get_container_vulnerabilities_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                               take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_container_vulnerabilities_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                      take=10, skip=10)
    assert second_result is not None


def test_get_package_licenses_by_scan_id():
    result = ScaAPI().get_package_licenses_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                      take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_package_licenses_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                             take=10, skip=10)
    assert second_result is not None


def test_get_down_stream_remediation_by_scan_id():
    result = ScaAPI().get_down_stream_remediation_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                             take=10, skip=0)
    assert result is not None
    second_result = ScaAPI().get_down_stream_remediation_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7",
                                                                    take=10, skip=10)
    assert second_result is not None


def test_get_scan_info_by_scan_id():
    result = ScaAPI().get_scan_info_by_scan_id(scan_id="d201a795-e2f0-44bf-8f5a-d6a5eb1c28b7")
    assert result is not None
