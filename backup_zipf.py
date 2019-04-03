import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re
import fileinput

from numpy.polynomial.polynomial import polyfit

from collections import Counter

from numpy import array, polyval

from math import log, exp


name = input("Filename: ")



def showPlot():
    
    f = plt.figure(200)
    words = re.findall(r'\w+', open(name).read().lower())
    res = Counter(words).most_common(50)

    print("Top 50 most Common words...")

    numbers = []
    labels = []
    anotha = []

    index = 1
    print("Index", '\t\t\t', "Word", '\t\t\t', "Frequency")
    print("-------------------------------------------------------------")
    for k,v in res:
        print(index,'\t\t\t', k,'\t\t\t', v)
        numbers.append(index*v)
        labels.append(index)
        anotha.append(v)
        index += 1




    #labels = [float(i) for i in labels]
    anotha = [float(i) for i in anotha]

    print(labels)
    print(anotha)

    list_x = labels
    list_y = anotha


    x = list_x
    y = list_y


    logx = np.log(x)
    logy = np.log(y)


    const = polyfit(logx,logy,1)
    b, m = polyfit(x, y, 1)    

    list_x = array(list_x)
    list_y = array(list_y)

    #plt.plot(list_x, np.exp(polyval(const, logx)))

    plt.plot(list_x, (np.exp(b) + np.exp(m*list_x)), '-')


    plt.xlabel('Ranks')
    plt.ylabel('Frequency')
    plt.title('Log-Log graph for Word freq. vs rank')
    plt.xticks(ticks=list_x,labels=labels)

    #plt.figure(figsize=(w,h), dpi=d)
    plt.loglog(list_x,list_y,'.')
    f.show()


def showPlot2a():

    g = plt.figure(100)
    words = re.findall(r'\w+', open(name).read().lower())
    res = Counter(words).most_common(50)

    numbers = []
    labels = []
    anotha = []
    perc = []
    totalSum = 0
    index = 0
    for k,v in res:
        print(index,'\t\t', k,'\t\t', v)
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