from exceptions import FailedToInitComponentExceptuion

info_prefix_value = "[Info]"
warn_prefix_value = "[Warn]"
debug_prefix_value = "[Debug]"
error_prefix_value = "[Error]"



class ILog():
    def Info(self, value):
        raise NotImplementedError()
    def Warn(self, value):
        raise NotImplementedError()
    def Debug(self, value):
        raise NotImplementedError()
    def Error(self, value):
        raise NotImplementedError()

class FileLog(ILog):
    def __init__(self,filename):
        try:
            self.file = open(filename,'w+')
        except Exception as e:
            print(e.__str__())
            raise FailedToInitComponentExceptuion()

    def Info(self, value):
        self.write_to_file(info_prefix_value,value)
    def Warn(self, value):
        self.write_to_file(warn_prefix_value, value)
    def Debug(self, value):
        self.write_to_file(debug_prefix_value, value)
    def Error(self, value):
        self.write_to_file(error_prefix_value, value)

    def write_to_file(self, prefix, value):
        self.file.writelines(str.format("{0} {1}",prefix, value))

class ConsoleLog(ILog):
    def Info(self, value):
        self.write_to_console(info_prefix_value,value)
    def Warn(self, value):
        self.write_to_console(warn_prefix_value, value)
    def Debug(self, value):
        self.write_to_console(debug_prefix_value, value)
    def Error(self, value):
        self.write_to_console(error_prefix_value, value)

    def write_to_console(self, prefix, value):
        print(str.format("{0}:{1}",prefix, value),end='\n')

