# coding: utf-8
from password_tools import get_enc_password


def get_update_dict_by_list(update_list, json_data):
    update_dict = {}
    for item in update_list:
        v = json_data.get(item)
        if v:
            if item == 'password':
                update_dict[item] = get_enc_password(v)
            else:
                update_dict[item] = v
    return update_dict
