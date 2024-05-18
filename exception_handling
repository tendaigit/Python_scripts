try:
  # Try to append to a file that is normally not writable
  # for anyone other than root 
  f = open("/etc/hosts", "w+")
except IOError as ex:
  # The variable "ex" will hold details about the error
  # that occurred
  print("Error appending to file: " + str(ex))
else:
  # If there was no exception, close the file.
  f.close()
