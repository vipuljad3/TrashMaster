import time

def iterate(current_index, condition, id_list):
    if condition == 'NEXT':
        if current_index >= max(id_list):
            next_index = min(id_list)
            return(next_index)
        next_index = [min([m for m in id_list if m > current_index])][0]
        return(next_index)

    if condition == 'PREVIOUS':
        if current_index <= min(id_list):
            next_index = max(id_list)
            return(next_index)
        next_index = [max([m for m in id_list if m < current_index])][0]
        return(next_index)


def get_current_id(current_id_path):
    with open (current_id_path, 'r') as log:
        current_id = log.read()
        return(int(current_id))

def update_current_id(current_id_path, id):
    with open (current_id_path, 'w') as log:
        log.write(str(id))

def update_log(log_path, user):
    with open (log_path, 'a') as log:
        current_daytime = time.localtime() 
        current_daytime = time.strftime("%d-%m-%Y %H:%M:%S", current_daytime)
        logstr = f'\n{current_daytime}   {user}'
        logs = log.write(logstr)

def read_logs(log_path):
    with open (log_path, 'r') as log:
        logs = log.readlines()
        last_lines = logs[-10:]
    last_lines = [m.rstrip() for m in last_lines]
    return last_lines



print(read_logs('users/log.log'))
