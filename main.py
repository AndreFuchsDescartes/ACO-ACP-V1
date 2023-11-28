# Main File
import configparser

# Initialize Variables
filepath = "C:\\Users\\User\\Documents\\ACP.ini"

## Read from File

config = configparser.ConfigParser()
with open(filepath) as stream:
    config.read_string("[top]\n" + stream.read()) # add 'top' as dummy header, since the file doesn'come with one
print(config['top']['PlayableCharacterIndex'])

# Update Values of Variables based on File

# Edit Values of Variables based on File

# Apply Changes
