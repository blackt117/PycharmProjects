def readFile():
    with open ('nile.csv','r') as file:
        for line in file:
            line =line.strip('\n')
            line = line.split(',')
            print(f'{line[0]:<8}{line[1]}')

readFile()