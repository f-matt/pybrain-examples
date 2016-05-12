from pyevolve import G1DList
from pyevolve import GSimpleGA

def eval_func(chromosome):
    print chromosome.getInternalList()
    score = 0.0
    # iterate over the chromosome
    for value in chromosome:
        if value==0:
            score += 1
    return score

def run_ga():
    
    genome = G1DList.G1DList(20)
    genome.setParams(rangemin=0, rangemax=10)
    genome.evaluator.set(eval_func)
    ga = GSimpleGA.GSimpleGA(genome)
    
    ga.evolve(freq_stats=10)
        
    print "best individual: "
    print ga.bestIndividual().getInternalList()
