import matplotlib.pyplot as plt

def histplot(x,bins_a):
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    plt.hist(x, bins_a)

    plt.show()
    plt.title('Total volume of avocado sold over the last couple years')
    plt.xlabel('years')
    plt.ylabel('volume')


def timeplot(volume,year):
    plt.plot(volume,year)
    plt.ylabel('year')
    plt.xlabel('volume')

    plt.show()