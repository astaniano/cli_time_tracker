import os

def load_env_vars():
    with open('./.env', 'r') as openfile:
        env_file = openfile.read()

    env_vars_list = env_file.split('\n')

    filtered_env_vars_list = list(filter(
        lambda env_var_record: env_var_record != '',
        env_vars_list
    ))

    for row in filtered_env_vars_list:
        if '=' not in row:
            raise Exception('values of environmental variables should be specified in .env file after "=" sign')

        env_name, env_val = row.split('=')
        os.environ[env_name] = env_val 
