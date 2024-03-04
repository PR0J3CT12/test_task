from django.utils.datastructures import MultiValueDictKeyError


def get_variable(variable_name, source_request):
    try:
        variable = source_request.GET[variable_name]
        return variable
    except MultiValueDictKeyError:
        return None
    except Exception as e:
        return None


def id_is_valid(id_):
    try:
        id_ = int(id_)
        return True
    except Exception as e:
        return False
