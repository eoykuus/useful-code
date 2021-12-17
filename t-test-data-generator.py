import random
import numpy as np

# Data generation tool for a given number of participants, mean score and standard deviation
def create_group(number, mu, sigma):
    numbers_list = list(range(1,number+1))
    
    # Creates a normal distribution for a given number of participants
    dataset = list(np.random.normal(mu, sigma, number))

    data_exp = {}
    data_cont = {}
    
    # Selects the scores to put into experiment and control groups
    for score in dataset:
        subject_name = None
        if score < mu-sigma or score < mu: 
            while subject_name == None:
                subject_no = random.randint(1,number+1)
                if subject_no in numbers_list:
                    subject_name = f"subject_{subject_no}"
                    numbers_list.remove(subject_no)
            data_exp[subject_name] = score
                
        elif score >= mu+sigma or score >= mu + sigma/2:
            while subject_name == None:
                subject_no = random.randint(1,number+1)
                if subject_no in numbers_list:
                    subject_name = f"subject_{subject_no}"
                    numbers_list.remove(subject_no)
            data_cont[subject_name] = score
    
    # Makes experiment and control group size same.
    counter = abs(len(data_exp) - len(data_cont))
    
    if len(data_exp) < len(data_cont):
        while counter != 0:
            data_cont.popitem()
            counter = counter - 1
            
    else:
        while counter != 0:
            data_exp.popitem()
            counter = counter -1 
    
    tot_data = {}
    tot_data["experiment"] = data_exp
    tot_data["control"] = data_cont
    
    return tot_data
