import requests


# Json-list with candidate:
def load_candidates_json() -> list:
    """
    :return: candidats_json: json-list with candidate
    """

    candidate = requests.get('https://jsonkeeper.com/b/P49G')
    candidates_json = candidate.json()

    return candidates_json


candidate_list = load_candidates_json()


# information about the candidate id:
def get_candidate_id(candidates_id) -> list:
    """
    :param candidates_id: id candidates
    :return: candidate_id: information about the candidate
    """
    return [candidate_id for candidate_id in candidate_list if candidate_id['id'] == candidates_id]


# information about the candidate name:
def get_candidate_name(candidates_name) -> list:
    """
    :param candidates_name:  name candidates
    :return: information about the candidate
    """
    return [candidate_name for candidate_name in candidate_list if candidate_name['name'] == candidates_name]


# List candidates with this name(maybe not full):
def search_candidate(candidate_name_not_full) -> list:
    """
    :param candidate_name_not_full: name candidates (maybe not full)
    :return: candidate_name_search: list candidates with this name (maybe not full)
    """
    return [candidate_name_search for candidate_name_search in candidate_list if candidate_name_not_full in candidate_name_search['name']]


# List candidates with this skill:
def search_candidate_skill(candidate_skill_not_full):
    """
    :param candidate_skill_not_full: skill
    :return: list candidates about this skill
    """
    return [candidate_skill_search for candidate_skill_search in candidate_list if candidate_skill_not_full in candidate_skill_search['skills'].lower()]
