import sys, traceback

####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
####YOU MAY NOT USE DICTIONARIES ANYWHERE IN THIS PROGRAM#####
###
###
### Type your name here: Tyler Black
###
##
## Look at the function main below to see how these functions are used
##
##
## Complete the functions below as directed in the docstring comments
##
##
## I will test your code by running the main function defined below.
##
##Obviously, as you write each function, you can test it individually
##using the Python shell
##
##
def initialize_portfolio(filename): #20 points
    """
    read the data contained in the named file
    and return a *list of tuples* representing the data
    For example: [('DD', 1085),('DIS', 1213), ('GE', 1781), ('GS',1913),......]
    """
    file = open(filename, 'r')
    list1=[]
    x=''
    y=''
    for line in file:
##        line = line.strip()
##        x=line[0:line.index(',')]
##        y=int(line[line.index(',')+1:])
##        list1.append((x,y))
        line = line.strip()
        z=line.split(',')
        z[1]=int(z[1])
        z=tuple(z)
        list1.append(z)
    print(list1)
    file.close()
    return list1
    #if you cannot get the above function to work, comment out
    #what you have worked on and hard code the return statement so you can
    #move forward, example below, u would need to replace the dots
    #with the rest of the text file data
    #return [('DD', 1085),('DIS', 1213), ('GE', 1781), ('GS',1913),......]
    

def print_portfolio(portfolio):  #20 points
    """
    Print the contents of the portfolio in a two-column format as shown below
    The first line is a header
    All the other lines show a stock symbol, and the number of shares
    held of that stock, with a tab "\t" character separating the two,
    like this:
    Symbol    Amount
    DIS       1213
    GE        1781
    GS        1913
    .....
    This function does not return anything
    """
    print("Symbol \t Amount")
    q=0
    for i in range(len(portfolio)):
        print(format(portfolio[i][q],"4"),"\t", format(portfolio[i][q+1],"^3"))
        q=0
    pass

def total_shares(portfolio): #20 points
    """
    return the total number of shares owned (across all stocks) in the portfolio
    """
    sum1=0
    q=1
    for i in range(len(portfolio)):
        sum1=sum1+portfolio[i][q]
    return sum1


def find_amount(portfolio, stock_symbol): #20 points
    """
    return the number of shares of the specified stock in the portfolio
    for example, find_amount(portfolio, "DIS") returns 1213
    """
    q=0
    for i in range(len(portfolio)):
        if stock_symbol == portfolio[i][q]:
            return portfolio[i][q+1]


def update_portfolio(portfolio, filename): # 20 points
    """
    Open the specified file, read the transactions in it,
    and update the portfolio accordingly
    Return the updated portfolio
    """
    # list2=[]
    # q=0
    # for i in range(len(portfolio)):
    #     list2.append([portfolio[i][q],portfolio[i][q+1]])
    #     q=0
    # file = open(filename, 'r')
    # q=0
    # for line in file:
    #     line=line.strip()
    #     t=line.split(',')
    #     if t[0]=="Buy":
    #         for i in range(len(list2)):
    #             if t[1] == list2[i][q]:
    #                 list2[i][q+1]=int(t[2])+list2[i][q+1]
    #     elif t[0]=='Sell':
    #         for i in range(len(list2)):
    #             if t[1] == list2[i][q]:
    #                list2[i][q+1]=list2[i][q+1]-int(t[2])
    #     q=0
    # q=0
    # list3=[]
    # for i in range(len(list2)):
    #     list3.append((list2[i][q],list2[i][q+1]))
    # file.close()
    # return list3
    with open(filename,'r') as file:
        for line in file:
            t=0
            line=line.strip()
            line = line.split(',')
            if line[0]=='Buy':
                for i in range(len(portfolio)):
                    if line[1]==portfolio[i][0]:
                        t=portfolio[i][1]+int(line[2])
                        portfolio[i]=portfolio[i][0],t,1
            else:
                for i in range(len(portfolio)):
                    if line[1]==portfolio[i][0]:
                        t=portfolio[i][1]-int(line[2])
                        portfolio[i]=portfolio[i][0],t,1
    print (portfolio)
    return portfolio
#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
#DO NOT MAKE ANY CHANGES TO THE main FUNCTION BELOW
def main():
    try:
        portfolio = initialize_portfolio("holdings.txt")
    except:
        print(">>>>>>>> initialize_portfolio has errors")
        traceback.print_exc()

    print("\nHere is your portfolio before any trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
        traceback.print_exc()
        
    try:
        print("\nThe total number of shares in the portfolio is ", total_shares(portfolio))
    except:
        print(">>>>>>>> total_shares has errors")
        traceback.print_exc()
        
    symbol = input("\nEnter a stock symbol(like IBM): ")

    try:
        print("\nBefore any trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>> find_amount has errors")
        traceback.print_exc()

    try:
        portfolio = update_portfolio(portfolio, "trades.txt")
    except:
        print(">>>>>>>> update_portfolio has errors")
        traceback.print_exc()
        
    print("\nHere is your portfolio after trades\n")
    
    try:
        print_portfolio(portfolio)
    except:
        print(">>>>>>>> print_portfolio has errors")
        traceback.print_exc()
    
    symbol = input("\nEnter a stock symbol(like IBM): ")
    
    try:
        print("\nAfter trades, you hold ", find_amount(portfolio, symbol)," shares of ", symbol)
    except:
        print(">>>>>>>>> find_amount has errors")
        traceback.print_exc()


#Run the main function     
main()
