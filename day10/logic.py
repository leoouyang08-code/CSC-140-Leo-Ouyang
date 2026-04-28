import random 
import numpy as np 

def run_bacteria_simulation(steps=1000, bias=1): ## simulation function with defaults

    x_path = [random.randint(0, 10)] #bacteria random coordinate
    y_path = [random.randint(0, 10)] 
    
    for i in range(steps):
        tumble = random.randint(-5, 5) #random vertical movement
        movement = tumble + bias #plus bias so it tends to move up
        
        new_x = x_path[-1] + 1 #x will always increase by 1 
        new_y = y_path[-1] + movement #y will change randomly 
        
        x_path.append(new_x) #always stores new positions
        y_path.append(new_y)
        
    return np.array(x_path), np.array(y_path) #returns them as numPy arrays