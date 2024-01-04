def calculateavg():
    sum=0
    Grades=[]
    with open('Grades.csv','r') as file:
    #     for line in file:
    #         line = line.strip('\n')
    #         line = line.split(',')
    #         Grades.append(line[1])
    # del Grades[0]
    # for index in Grades:
    #     sum = sum +float(index)
    # print(sum/len(Grades))
    # print(Grades)
        line = file.readline().strip()
        print(line)
        counter=1
        gradecounter = 0
        while line !='':
            line = line.split(',')
            if counter !=1:
                sum=sum+float(line[1])
                gradecounter=gradecounter + 1
            line = file.readline().strip()
            counter = counter + 1
        print(sum/gradecounter)
calculateavg()