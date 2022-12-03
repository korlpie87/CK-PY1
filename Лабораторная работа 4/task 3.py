def delete(list_, index=None):
    del_list_ = ()

    if not index:
        del_list_ = list_[:-1]
    else:
        del_list_ = list_[:index] + list_[index+1:]
    return del_list_


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
