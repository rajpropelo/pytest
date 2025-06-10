import os

# Keywords to match typical DB connection keys (assuming MySQL)
mysql_env_keys = ['HOST', 'PORT', 'USER', 'USERNAME', 'PASS', 'PASSWORD', 'DATABASE', 'NAME', 'URI', 'URL']

print("MySQL-related environment variables (without prefix):\n")

for key, value in os.environ.items():
    if key.upper() in mysql_env_keys:
        print(f"{key} = {value}")
