try:
  file=open('sample.txt','r')
  print("Reading file content:")
  line1=file.readline()
  line2=file.readline()
  print(f"line 1:{line1.strip()}")
  print(f"line 2:{line2.strip()}")
 

except FileNotFoundError:
  print("The file'sample.txt' not found ")