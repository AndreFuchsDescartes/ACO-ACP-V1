# Main File
import configparser

# Initialize Variables
filepath = "C:\\Users\\User\\Documents\\ACP.ini"
parameterValueList = configparser.ConfigParser()

# Define Functions
def updateParameterValues(filepath):
    with open(filepath) as stream:
        parameterValueList.read_string("[top]\n" + stream.read()) # add 'top' as dummy header, since the file doesn'come with one
    
def applyParameterValues():
    with open(filepath, 'w') as configfile:
        parameterValueList.write(configfile)

## Read from File
updateParameterValues(filepath)
print(parameterValueList['top']['PlayableCharacterIndex'])

# Update Values of Variables based on File
parameterValueList.set('top','PlayableCharacterIndex','1')

# Edit Values of Variables based on File

# Apply Changes
applyParameterValues()