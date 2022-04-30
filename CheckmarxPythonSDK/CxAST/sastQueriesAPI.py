from .httpRequests import get_request
from .utilities import get_url_param, type_check, list_member_type_check
from .dto import QueriesResponse, Preset

query_url = "/api/queries"


def get_list_of_the_existing_query_repos():
    """

    Returns:
        list of QueriesResponse
    """
    relative_url = query_url
    response = get_request(relative_url=relative_url)
    queries = response.json()
    return [
        QueriesResponse(
            name=item.get("name"),
            is_active=item.get("isActive"),
            last_modified=item.get("lastModified"),
        ) for item in queries
    ]


def get_sast_queries_presets(project_id=None):
    """

    Args:
        project_id (str):

    Returns:
        list of Preset
    """
    relative_url = query_url + "/presets"
    relative_url += get_url_param("project-id", project_id)
    response = get_request(relative_url=relative_url)
    presets = response.json()
    return [
        Preset(
            preset_id=item.get("id"),
            name=item.get("name"),
        ) for item in presets
    ]


def get_sast_query_description(ids):
    """

    Args:
        ids (list of int): list of query ids

    Returns:
        list of descriptions associated to each of the given query ids
    """
    type_check(ids, list)
    list_member_type_check(ids, int)

    relative_url = query_url + "/descriptions?"
    relative_url += get_url_param("ids", ids)
    response = get_request(relative_url=relative_url)
    presets = response.json()
