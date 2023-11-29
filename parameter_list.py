class ParameterList:
    import os.path

    def __init__(self) -> None:
        self.list = []
        pass

    def parse(self, filepath):

        if not self.os.path.isfile(filepath):
            print('File does not exist.')
        else:
            # Open the file and read its content.
            with open(filepath) as f:
                content = f.read().splitlines()

            # Display the file's content line by line.
            for line in content:
               line = line.replace('= ','')
               self.list.append(line.split())
               
        #print(self.list,"\n")
        pass
    
    def set(self,parameter, value):
        for i, sublist in enumerate(self.list):
            if parameter in sublist:
                self.list[i][1] = value
        pass
    
    def applyTo(self, filepath):
        entry = ""
        for param in self.list:
            entry = entry + param[0] + " = " + param[1] + "\n"
            
        with open(filepath, "w") as text_file:
            text_file.write(entry)
        print(entry)
        pass



