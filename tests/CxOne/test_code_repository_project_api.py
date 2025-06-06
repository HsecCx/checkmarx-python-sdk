import os
from CheckmarxPythonSDK.CxOne import (
    import_code_repository,
    retrieve_import_status,
)

from CheckmarxPythonSDK.CxOne.dto import (
    SCMImportInput,
    Scm,
    ScmOrganization,
    ProjectSettings,
    ScmProject,
    Scanner,
)


def test_import_code_repository():
    scm_import_input = SCMImportInput(
        scm=Scm(token=os.getenv("GITHUB_TOKEN")),
        organization=ScmOrganization(org_identity="HappyY19", monitor_for_new_projects=False),
        default_project_settings=ProjectSettings(
            web_hook_enabled=False,
            decorate_pull_requests=False,
            scanners=[
                Scanner(scanner_type="sast", incremental=False),
                Scanner(scanner_type="sca", auto_pr_enabled=False),
                Scanner(scanner_type="apisec"),
                Scanner(scanner_type="kics"),
            ]
        ),
        scan_projects_after_import=False,
        projects=[
            ScmProject(
                scm_repository_url="https://github.com/HappyY19/cxclipy",
                protected_branches=["main"],
                branch_to_scan_upon_creation="main"
            ),
            ScmProject(
                scm_repository_url="https://github.com/HappyY19/JavaVulnerableLab",
                protected_branches=["master"],
                branch_to_scan_upon_creation="master"
            )
        ]
    )
    import_response = import_code_repository(scm_import_input)
    assert import_response is not None

    process_id = import_response.get("processId")
    status_response = retrieve_import_status(process_id=process_id)
    assert status_response is not None


def test_retrieve_import_status():
    process_id = 'affcc535-9df1-456a-9eea-9dde3876921a'
    status_response = retrieve_import_status(process_id=process_id)
    assert status_response is not None
