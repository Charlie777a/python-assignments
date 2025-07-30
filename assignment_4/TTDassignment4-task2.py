with open('output.txt','w') as file1:
    line1= file1.write(input(f"Entre text to write in the file: "))
    print("Data successfully written to output.txt.")

with open('output.txt','a') as file2:
    line2=file2.write('\n')
    line3=file2.write(input(f"\nEnter additional text to append: "))
    print("Data successfully appended\n\n")

with open('output.txt','r') as file3:
    print("final content of 'output.txt' file:")
    print(file3.read())


   