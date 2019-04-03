import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re
import fileinput

from numpy.polynomial.polynomial import polyfit

from collections import Counter

from numpy import array

from math import log, exp



name = input("Filename: ")


#LOG-LOG graph for rank vs frequency
def showPlot():
    
    f = plt.figure(200)
    words = re.findall(r'\w+', open(name).read().lower())
    res = Counter(words).most_common(150)

    print("Top 50 most Common words...")

    numbers = []
    labels = []
    anotha = []


    print("Index", '\t\t\t\t', "Word", '\t\t\t\t', "Frequency")
    print("-------------------------------------------------------------")
    index = 1
    for k,v in res:
        if(index<51):
            print(index,'\t\t\t\t', k,'\t\t\t\t', v)
        numbers.append(index*v)
        labels.append(index)
        anotha.append(v)
        index += 1





    #labels = [float(i) for i in labels]
    anotha = [float(i) for i in anotha]

    #print(labels)
    #print(anotha)

    list_x = labels
    list_y = anotha


    x = list_x
    y = list_y



    w = 10
    h = 10
    d = 10


    logx = np.log(x)
    logy = np.log(y)


    b, m = polyfit(list_x,list_y,1)

    list_x = array(list_x)
    list_y = array(list_y)


    



    #plt.plot(list_x, (b+m*list_x), '-')

    coeffs = np.polyfit(logx, logy, deg=3)
    poly = np.poly1d(coeffs)

    yfit = lambda x: np.exp(poly(np.log(x)))
    #plt.loglog(x,yfit(x),'-')           #plotting the best fit curve
    plt.xlabel('Ranks')
    plt.ylabel('Frequency')
    plt.title('Log-Log graph for Word freq. vs rank (150 words)')
    plt.xticks(ticks=list_x,labels=labels)

    #plt.figure(figsize=(w,h), dpi=d)
    plt.loglog(list_x,list_y,'.')        #Scatter plot
    f.show()


def showPlot2a():

    g = plt.figure(100)
    words = re.findall(r'\w+', open(name).read().lower())
    res = Counter(words).most_common(75)

    numbers = []
    labels = []
    anotha = []
    perc = []
    totalSum = 0
    index = 0
    for k,v in res:
        #print(index,'\t\t', k,'\t\t', v)
        numbers.append(index*v)
        totalSum += v
        labels.append(index)
        anotha.append(v)
        index += 1
    
    for a in anotha:
        perc.append(a/totalSum*100)



    plt.rcParams.update({'font.size': 10})
    y_pos = np.arange(len(labels)+1)


    labels2 = []
    for i in labels:
        labels2.append(i+1)

    plt.yticks(y_pos, labels2)



#    for i,v in enumerate(perc):
#        plt.text(i-0.75, v+0.2, str(v)[:5], color='black')

    for i,v in enumerate(perc):
        plt.text(v, i-0.25, str(v)[:4], color='black')   


   #plt.gca().invert_yaxis()
    plt.title('Rank vs Frequency %')
    plt.xlabel('Frequency in %')
    plt.ylabel('Ranks')
    plt.barh(labels,perc)
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    g.show()


showPlot2a()
showPlot()
input("Press Enter to continue...")
