import os

def load_env_vars():
    path_to_env_file = os.path.dirname(os.path.abspath(__file__)) + '/.env'
    with open(path_to_env_file, 'r') as openfile:
        env_file = openfile.read()

    env_vars_list = env_file.split('\n')

    filtered_env_vars_list = list(filter(
        lambda env_var_record: env_var_record != '',
        env_vars_list
    ))

    for env_name_and_value_row in filtered_env_vars_list:
        if '=' not in env_name_and_value_row:
            raise Exception('values of environmental variables should be specified in .env file after "=" sign')

        env_name, env_val = env_name_and_value_row.split('=')
        os.environ[env_name] = env_val
