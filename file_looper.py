class FileLooper():

    def __init__(self, open_file, num_loops=1, start_offset=0):
        self.open_file = open_file
        #TODO: allow arbitrary start point
        self.start_offset = start_offset
        self.current_offset = self.open_file.tell()
        self.num_loops = num_loops
        self.complete_loops = 0

    def add_loop(self, num_to_add=1):
        """coming back for more loops through the file"""
        self.num_loops += num_to_add

    def return_line(self):
        """ like File.readline """
        self.open_file.seek(self.current_offset)
        get_line = self.open_file.readline()
        if not get_line: #eof 
            self.complete_loops +=1
            #TODO: stil gives a "None" as last item
            if self.complete_loops == self.num_loops:
                return
            self.current_offset = 0
            self.open_file.seek(0)
            get_line = self.open_file.readline()
        self.current_offset += len(get_line)
        return get_line

    def line(self):
       """generator for lines, like "for line in File:" """
       while self.complete_loops < self.num_loops:
           yield self.return_line()
