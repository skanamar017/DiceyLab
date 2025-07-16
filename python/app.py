import random

class Bins:
    def __init__(self, min_bin: int, max_bin: int):
        self.min_bin=min_bin
        self.max_bin=max_bin
        
        #if using dictionaries
        '''
        self.bins={}
        for i in range(self.min_bin, self.max_bin+1):
            self.bins[i]=0
        '''
        self.bins=[]
        for i in range(self.min_bin, self.max_bin+1):
            self.bins.append(0)


    def get_bin(self, bin_num: int):
        return self.bins[bin_num-self.min_bin]

    def increment_bin(self, bin_num: int):
        self.bins[bin_num-self.min_bin]+=1



class Dice:
    def __init__(self, rolls: int):
        self.rolls=rolls

    def roll(self):
        return random.randrange(1, 7)

    def toss_and_sum(self):
        sum=0
        for i in range(self.rolls):
            sum+=self.roll()
        return sum


class Simulation:
    def __init__(self, Dies: int, Tosses: int):
        self.Dies=Dies
        self.Tosses=Tosses
        self.sim_bins=Bins(self.Dies, self.Dies*6)
        self.die_roll=Dice(Dies)


    def run_simulation(self):
        #call a dice and bins object here
        for i in range(self.Tosses):
            score=self.die_roll.toss_and_sum()
            self.sim_bins.increment_bin(score)
        
        return self.sim_bins
    
    def print_results(self):
        results=""
        for index, bin in enumerate(self.sim_bins.bins):
            results+=f"{index+self.Dies:>3} : {bin:>9}: {round(bin/self.Tosses, 2):<4} {"*"*((bin*100)//self.Tosses)}\n"

        return results


            



def main():

    print("\nDice")
    craps=Dice(2)
    craps_toss=craps.toss_and_sum()
    print(craps_toss)

    yatzee=Dice(5)
    yatzee_toss=yatzee.toss_and_sum()
    print(yatzee_toss)

    print("\nBins")
    results = Bins(2, 12)  # for bins from 2..12
    print(results.bins)
    #results.set_bins()
    number_of_tens = results.get_bin(10)  # returns the number of tens in the 10 bin
    results.increment_bin(10)  # should increment bin # 10
    number_of_tens = results.get_bin(10)
    print(number_of_tens)
    print(results.bins)



    print("\nSimulation")
    sim = Simulation(3, 1000000)

    finals=sim.run_simulation()

    print(finals.bins)

    printings=sim.print_results()

    print(printings)

if __name__ == "__main__":
    main()
