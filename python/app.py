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

    def get_index(self, value: int):
        return self.bins.index(value)+self.min_bin

    def increment_bin(self, bin_num: int):
        self.bins[bin_num-self.min_bin]+=1



class Dice:
    def __init__(self, sides: int, rolls: int):
        self.sides=sides
        self.rolls=rolls

    def __str__(self):
            if self.rolls==1:
                return f"Rolled a {self.sides}-sided die 1 time"
            return f"Rolled a {self.sides}-sided die {self.rolls} time"

    def roll(self):
        return random.randrange(1, self.sides+1)

    def toss_and_sum(self):
        sum=0
        for i in range(self.rolls):
            sum+=self.roll()
        return sum


class Simulation:
    def __init__(self, Sides: int, Dies: int, Tosses: int):
        self.Sides=Sides
        self.Dies=Dies
        self.Tosses=Tosses

        self.sim_bins=Bins(self.Dies, self.Dies*self.Sides)
        self.die_roll=Dice(self.Sides, self.Dies)

    def calculateMinMax(self):
        print(f"There are {self.Dies*self.Sides-self.Dies+1} bins total")

    def run_simulation(self):
        #call a dice and bins object here
        for i in range(self.Tosses):
            score=self.die_roll.toss_and_sum()
            self.sim_bins.increment_bin(score)
        
        return self.sim_bins
    
    def print_results(self):
        results=""
        for index, bin in enumerate(self.sim_bins.bins):
            results+=f"{index+self.Dies:>2} : {bin:>8}: {round(bin/self.Tosses, 2):<4} {"*"*((bin*100)//self.Tosses)}\n"

        return results


            



def main():

    print("\nDice() Testing\n")
    craps=Dice(6, 2)
    for i in range(10):
        print(f"Roll {i} for craps is {craps.toss_and_sum()}")
        if craps.toss_and_sum() in range(craps.rolls, craps.sides*craps.rolls):
            print(f"Roll {i} is within range\n")
    print("\n")
    yatzee=Dice(6, 5)
    for i in range(50):
        print(f"Roll {i} for yatzee is {yatzee.toss_and_sum()}")
        if craps.toss_and_sum() in range(craps.rolls, craps.sides*craps.rolls):
            print(f"Roll {i} is within range\n")





    print("\nBins() Testing \n")
    results = Bins(2, 12)  # for bins from 2..12
    print(f"Bins at start: {results.bins}")
    for i in range(100):
        roll=craps.toss_and_sum() #from Dice() testing
        results.increment_bin(roll)
    for i in range(len(results.bins)):
        print(f"Bin {i+results.min_bin}'s total is {results.get_bin(i)}")
    print(f"Bins at end: {results.bins}")




    print("\nSimulation() Testing \n")
    
    print("Test 1")
    sim1 = Simulation(6, 2, 20)
    sim1.calculateMinMax()
    finals1=sim1.run_simulation()
    print(finals1.bins)
    printings1=sim1.print_results()
    print(printings1)
    
    print("Test 2")
    sim2 = Simulation(8, 3, 1000000)
    sim2.calculateMinMax()
    finals2=sim2.run_simulation()
    print(finals2.bins)
    printings2=sim2.print_results()
    print(printings2)

if __name__ == "__main__":
    main()
