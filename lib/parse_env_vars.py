import os

def parse_env_vars_file(env_vars_file):
    lines_of_env_file = env_vars_file.split('\n')

    filtered_env_vars_list = list(filter(
        lambda line: line != '' and not line.startswith('#'),
        lines_of_env_file
    ))

    env_vars = dict()

    for env_name_and_value_row in filtered_env_vars_list:
        if '=' not in env_name_and_value_row:
            raise Exception('Could not parse .env file, please look into the source code')

        env_name, env_val = env_name_and_value_row.split('=')
        env_vars[env_name] = env_val

    return env_vars


# fills os.environ with values from @path_to_env_file
def load_env_vars(path_to_env_file):
    with open(path_to_env_file, 'r') as env_file:
        env_file = env_file.read()

    env_vars = parse_env_vars_file(env_file)

    for env_var_name in env_vars:
        os.environ[env_var_name] = env_vars[env_var_name]

