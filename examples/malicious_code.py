import os

# Dangerous operation: reading sensitive environment variables
secret_key = os.getenv("AWS_SECRET")
print(f"The secret key is: {secret_key}")
