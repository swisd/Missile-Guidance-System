#file_actions.py


def writefile(data, location):
  f = open(location, "a")
  f.write(data)
  f.write(''
          '')
  f.close()