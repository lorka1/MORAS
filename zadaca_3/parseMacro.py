def _MV(self, a, b):
    cmd = ["@"+ a, "D=M", "@" + b, "M=D"]
    return cmd

def _SWP(self, a, b):
	cmd = ["@temp", "M=0", "@" + a, "D=M", "@temp", "M=D", "@" + b, "D=M", "@" + a, "M=D", "@temp", "D=M", "@" + b, "M=D"]
	return cmd

def _SUM(self, a, b, d):
	cmd = ["@" + a, "D=M", "@" + b, "D=D+M", "@" + d, "M=D"]
	return cmd

def _WHILE(self, a):
	self._count += 1
	cmd = ["(WHILE" + str(self._count) + ")", "@" + a, "D=M", "@END" + str(self._count), "D;JEQ"]
	return cmd
	

def _parse_macros(self):
    self._iter_macros(self._parse_macro)
    
def _parse_macro(self, line, p, o):
    if line[0] == "$":
        commandLine = line[1:] 
        commandLineSplit = commandLine.split("(")
        macroCommand = commandLineSplit[0]
		
        if len(commandLine) > 1:
            arguments = command[1]
            argumentList = arguments.replace(")", "").split(",")
            
            if(macroCommand == "MV"):
                cmd = self._MV(argumentList[0], argumentList[1])
                return cmd
            
            elif(macroCommand == "SWP"):
                cmd = self._SWP(argumentList[0], argumentList[1])
                return cmd
            
            elif(macroCommand == "SUM"):
                cmd = self._SUM(argumentList[0], argumentList[1])
                return cmd
            
            elif(macroCommand == "WHILE"):
                cmd = self._WHILE(argumentList[0], argumentList[1])
                return cmd
            
            else:
                self._flag = False
                self._line = o   
                self._errm = "Invalid command: " + macroCommand
    else:
        return line 
            
              