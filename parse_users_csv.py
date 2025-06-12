import pandas as pd

def read_users(path):
    df = pd.read_csv(path)
    df = df[df["Active"] == 1]
    return df

def write_users(path, data):
    data.to_csv(path,index = False)

def delete_user(path, user_id) :
    data = read_users(path)
    data = data[data.id != user_id]
    print(data)
    write_users(path, data)

def add_user(path, user_name, email):
    data =  read_users(path)
    max_key = data['id'].max()+1
    dict = {'id': max_key, 'Name': user_name, 'Email': email, 'Active': 1}
    data = data.append(dict, ignore_index = True)
    print(data)
    write_users(path, data)

def edit_user(path, user_id , new_name , new_email):
    data =  read_users(path)
    data['Name'][data['id'] == user_id] = new_name
    data['Email'][data['id'] == user_id] = new_email
    write_users(path, data)

