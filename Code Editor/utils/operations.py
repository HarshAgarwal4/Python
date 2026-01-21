class operationsClass:
    def __init__(self , parent):
        self.parent = parent
    
    def cut(self):
        self.parent.T_AREA.event_generate("<<Cut>>")

    def copy(self):
        self.parent.T_AREA.event_generate("<<Copy>>")

    def paste(self):
        self.parent.T_AREA.event_generate("<<Paste>>")

    def undo(self):
        self.parent.T_AREA.event_generate("<<Undo>>")

    def redo(self):
        self.parent.T_AREA.event_generate("<<Redo>>")

    def selectAll(self):
        self.parent.T_AREA.event_generate("<<SelectAll>>")
