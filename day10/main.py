import matplotlib.pyplot as plt 
from logic import run_bacteria_simulation 

def main():

    x_coords, y_coords = run_bacteria_simulation(steps=500, bias=1) #steps 500 isntead

    plt.plot(x_coords, y_coords, color='green', label='Bacterial Path')
    plt.title("Bacterial Chemotaxis Simulation") 
    plt.xlabel("Time/Steps") 
    plt.ylabel("Direction Toward Nutrients") 
    plt.grid(True) 
    plt.legend() 
    plt.show() 

if __name__ == "__main__":
    main()