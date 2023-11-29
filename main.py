# Main File

from parameter_list import ParameterList

# Initialize Variables
filepath = "C:\\Users\\User\\Documents\\ACP.ini"
parameters = ParameterList()

# Define Functions
def updateParameterValues(filepath):
    parameters.parse(filepath)
    
def applyParameterValues():
    parameters.applyTo(filepath)
    pass
 
## Read from File
updateParameterValues(filepath)


# Update Values of Variables based on File


# Edit Values of Variables based on File
parameters.set('PlayableCharacterIndex','2')


# Apply Changes
applyParameterValues()