from split_settings.tools import include
from decouple import config

# Include the base settings file
include('base.py')

# Include the environment-specific settings file based on the environment
if 'Development' in config('ENV_NAME'):
    include('development.py')
elif 'Production' in config('ENV_NAME'):
    include('production.py')

# other security or credentials files...    