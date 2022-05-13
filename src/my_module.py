## Classes

class Hotel:
    def __init__(self, name, concept, pricesRegular, pricesRewards):
        self.name = name ## Nome do Hotel
        self.concept = concept ## Conceito do Hotel
        self.pricesRegular = pricesRegular ## Preços para Cliente regular (Dicionário contendo os preços em dias de semana e finais de semana)
        self.pricesRewards = pricesRewards ## Preços para Cliente premiun (Dicionário contendo os preços em dias de semana e finais de semana)

## Variáveis Globais

Lkwd = Hotel('Lakewood', 3 , {'weekday': 110, 'weekend': 90}, {'weekday': 80, 'weekend': 80})
Bdwd = Hotel('Bridgewood', 4 , {'weekday': 160, 'weekend': 60}, {'weekday': 110, 'weekend': 50})
Rdwd = Hotel('Ridgewood', 5 , {'weekday': 220, 'weekend': 150}, {'weekday': 100, 'weekend': 40})

Hotels = {'Lkwd': Lkwd, 'Bdwd': Bdwd, 'Rdwd': Rdwd}


def get_cheapest_hotel(input):   #DO NOT change the function's name
    global Hotels

    type, dates = input.split(':')
    dates = dates.split(',')
    days = [x.split('(')[1][0:-1] for x in dates]
    
    Total_Costs = {}

    for hotel in Hotels:
        Total_Costs[hotel] = 0
    
    for day in days:
        if day == 'sat' or day == 'sun':
            if type == 'Regular':
                for hotel in Hotels:
                    Total_Costs[hotel] += Hotels[hotel].pricesRegular['weekend']
            elif type == 'Rewards':
                for hotel in Hotels:
                    Total_Costs[hotel] += Hotels[hotel].pricesRewards['weekend']
        else:
            if type == 'Regular':
                for hotel in Hotels:
                    Total_Costs[hotel] += Hotels[hotel].pricesRegular['weekday']
            elif type == 'Rewards':
                for hotel in Hotels:
                    Total_Costs[hotel] += Hotels[hotel].pricesRewards['weekday']

    print(Total_Costs)
    
    min_cost = 99999

    for hotel in Hotels:
        if min_cost > Total_Costs[hotel]:
            min_cost = Total_Costs[hotel]
            cheapest = hotel
        elif min_cost == Total_Costs[hotel] and Hotels[hotel].concept > Hotels[cheapest].concept:
            cheapest = hotel

    cheapest_hotel = Hotels[cheapest].name
    return cheapest_hotel
