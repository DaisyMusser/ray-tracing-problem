MAX_COLOR = 255

class Ppm:
    def __init__(self, c):
        self.canvas = c
        # First three lines are the header
        self.lines = ["P3\n", 
                      "{w} {h}\n".format(w=c.width, h=c.height),
                      "255\n"]
        for row in c.grid:
            line = ""
            for color in row:
                line += "{c} ".format(c=color.toString(MAX_COLOR))
            # Remove space at end of line
            line = line.rstrip()
            line += "\n"
            self.lines.append(line)

    # Returns a specified range of lines as string
    # Really just for testing
    def getLines(self, start, end): # 0, 2
        span = end - start          # 2
        str_lines = ""
        for i in range(span + 1):
            str_lines += "{l}".format(l=self.lines[start + i])
        return str_lines

    # Returns first 3 lines as string
    def getHeader(self):
        return self.getLines(0, 2)

    # Returns all lines concat into string
    def dump(self):
        return "".join(self.lines)
        
