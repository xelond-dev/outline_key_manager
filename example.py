import outline_key_manager as okm
from config_reader import config
import urllib3

urllib3.disable_warnings() # Ignore urllib3 warnings

okm.init(config.outline_api.get_secret_value(), debug=True) # Init
okm.get_all_keys() # Get all keys
okm.new_key(name="Example1") # Create new key
okm.get_key("Example1") # Get information about key
okm.rename_key("Example1", "NewExampleName") # Rename from Example1 to NewExampleName
okm.set_limit("NewExampleName", 2048) # Set limit to 2GB
okm.remove_limit("NewExampleName") # Remove limit
okm.remove_key("NewExampleName") # Remove key