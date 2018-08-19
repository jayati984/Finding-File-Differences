"""
Find differences in file contents.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    "\n" not in line1
    "\n" not in line2
    if line1 == line2:
        return IDENTICAL
    if len(line1) == len(line2):
        shorter = line1
        longer = line2
    elif len(line1) > len(line2):
        shorter = line2
        longer = line1
    else:
        shorter = line1
        longer = line2
    index = len(shorter)
    num = 0
    if longer[0:index] == shorter[:]:
        return index
    for num in range(len(shorter)):
        if line1[num] != line2[num]:
            return num
        else:
            num += 1

#print(singleline_diff("Testing", "Test"))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """

    if idx > len(line1):
        return ""
    if idx > len(line2):
        return ""
    if idx < 0:
        return ""
    if "\n" in line1:
        return ""
    if "\n" in line2:
        return ""
    if "\r" in line1:
        return ""
    if "\r" in line2:
        return ""
    result = line1 + '\n' + ('=' * idx) + '^' + '\n' + line2 + '\n'
    return result

#print(singleline_diff_format('Test', 'Exam', 3))


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    num = 0
    number = 0
    if len(lines1) > len(lines2):
        shorter = len(lines2)
        short = lines2
        longs = lines1
        difference = len(lines1) - len(lines2)
    else:
        shorter = len(lines1)
        short = lines1
        longs = lines2
        difference = len(lines2) - len(lines1)

    if len(lines1) != len(lines2):
        for items in short:
            if lines1[num] == lines2[num]:
                num += 1
        listIndex = shorter
        lineIndex = 0
        return (listIndex, lineIndex)

    if len(lines1) == len(lines2):
        for items in lines1:
            if lines1[number] != lines2[number]:
                result = singleline_diff(lines1[number], lines2[number])
                return (number, result)
            else:
                number += 1
        return (IDENTICAL, IDENTICAL)

#print(multiline_diff(["line1","line2"],["line1","line2", "line3"]))


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    File1 = open(filename, "rt")
    readFile = File1.read()
    File1.close()

    splitList = list(readFile.split('\n'))
    resultList = splitList[:-1]
    return resultList


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    read1 = get_file_lines(filename1)
    read2 = get_file_lines(filename2)
    smaller = min(len(read1), len(read2))
    for lines in range(smaller):
        (line_number, index) = multiline_diff(read1, read2)
    if (line_number != -1) and (index != -1):
        end_str = "Line " + str(line_number) + ":\n" + read1[line_number] + "\n" + "="*(index) + "^" + "\n" + read2[line_number] + "\n"
        return end_str
    else:
        return "No differences\n"
