def switcher(x):

    try:
        if x.whoami() == 'Yandex':
            return Yandex.crawl(x)
        elif x.whoami() == 'Taxovichkof':
            return Taxovichkof.crawl(x)
        elif x.whoami() == 'Gett':
            return Gett.calc(x)
        elif x.whoami() == 'Vezet':
            return Vezet.crawl(x)
        elif x.whoami() == 'Five':
            return Five.crawl(x)
    except:
        return 'switch error'

def main():
    #start = input('start point: ')
    #finish = input('target point: ')
    start = 'Орджоникидзе 15'
    finish = 'Звенигородская 22'

    timer = datetime.now()

    park = [Yandex(start, finish),
            #Taxovichkof(start, finish),
            Gett(start, finish),
            Vezet(start, finish),
            Five(start, finish), ]

    pool = Pool(processes=len(park))
    price = pool.map(switcher, park)

    end = datetime.now()
    total = end - timer
    # print(f'time used: {str(total)[:7]}')
    # print(f'{park[0].whoami():<12} : {price[0]:>4}')
    # print(f'{park[1].whoami():<12} : {price[1]:>4}')
    # print(f'{park[2].whoami():<12} : {price[2]:>4}')
    # print(f'{park[3].whoami():<12} : {price[3]:>4}')
    # print(f'{park[4].whoami():<12} : {price[4]:>4}')
    return [str(total)[:7], price]


if __name__ == '__main__':
    from datetime import datetime
    from multiprocessing import Pool

    from classes.yandex import Yandex
    from classes.taxovichkof import Taxovichkof
    from classes.gett import Gett
    from classes.vezet import Vezet
    from classes.five_mils import Five
    main()
else:
    from datetime import datetime
    from multiprocessing import Pool

    from crawler.classes.yandex import Yandex
    from crawler.classes.taxovichkof import Taxovichkof
    from crawler.classes.gett import Gett
    from crawler.classes.vezet import Vezet
    from crawler.classes.five_mils import Five
