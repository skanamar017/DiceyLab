import random

class Bins:
    def __init__(self, min_bin: int, max_bin: int):
        self.min_bin=min_bin
        self.max_bin=max_bin
        self.bins={}
        for i in range(self.min_bin, self.max_bin+1):
            self.bins[i]=0

    def get_bin(self, bin_num: int):
        return self.bins[bin_num]

    def increment_bin(self, bin_num: int):
        self.bins[bin_num]+=1



class Dice:
    def __init__(self, rolls: int):
        self.rolls=rolls

    def toss_and_sum(self):
        sum=0
        for i in range(self.rolls):
            sum+=random.randrange(1, 7)
        return sum


class Simulation:
    def __init__(self, numberOfDies: int, numberOfTosses: int):
        self.numberOfDies=numberOfDies
        self.numberOfTosses=numberOfTosses
        self.sim_bins=Bins(self.numberOfDies, self.numberOfDies*6)
        self.die_roll=Dice(numberOfDies)


    def run_simulation(self):
        #call a dice and bins object here
        for i in range(self.numberOfTosses):
            score=self.die_roll.toss_and_sum()
            self.sim_bins.increment_bin(score)
        
        return self.sim_bins
    
    def print_results(self):
        results=""
        for num in self.sim_bins.bins:
            results+=f"{num:>3} : {self.sim_bins.bins[num]:>9}: {round(self.sim_bins.bins[num]/self.numberOfTosses, 2):<4} {"*"*((self.sim_bins.bins[num]*100)//self.numberOfTosses)}\n"

        return results


            



def main():

    craps=Dice(2)
    craps_toss=craps.toss_and_sum()
    print(craps_toss)

    yatzee=Dice(5)
    yatzee_toss=yatzee.toss_and_sum()
    print(yatzee_toss)

    results = Bins(2, 12)  # for bins from 2..12
    print(results.bins)
    #results.set_bins()
    number_of_tens = results.get_bin(10)  # returns the number of tens in the 10 bin
    print(number_of_tens)
    results.increment_bin(10)  # should increment bin # 10
    number_of_tens = results.get_bin(10)
    print(number_of_tens)
    print(results.bins)


    print("simulation")
    sim = Simulation(3, 1000000)

    finals=sim.run_simulation()

    print(finals.bins)

    printings=sim.print_results()

    print(printings)

if __name__ == "__main__":
    main()
