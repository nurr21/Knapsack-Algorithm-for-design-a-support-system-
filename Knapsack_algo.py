import pandas as pd

# Dataset of 20 devices
device_data = [
    {"name": "LED Street Lighting System", "cost": 15000, "savings": 4500, "score": 5},
    {"name": "Smart Building Thermostat", "cost": 4500, "savings": 1200, "score": 4},
    {"name": "High-Efficiency Heat Pump", "cost": 85000, "savings": 18000, "score": 5},
    {"name": "Solar Water Heater", "cost": 32000, "savings": 7500, "score": 5},
    {"name": "Sensor-controlled office lighting", "cost": 8000, "savings": 2200, "score": 4},
    {"name": "Variable Speed ​​HVAC System", "cost": 120000, "savings": 25000, "score": 4},
    {"name": "Triple Glazed Eco Windows", "cost": 65000, "savings": 9500, "score": 5},
    {"name": "Hand Dryers", "cost": 6000, "savings": 1100, "score": 3},
    {"name": "Magnetic Bearing Cooler", "cost": 250000, "savings": 48000, "score": 2},
    {"name": "Green Roof Thermal Insulation", "cost": 95000, "savings": 14000, "score": 5},
    {"name": "Low Flow Automatic Faucets", "cost": 12000, "savings": 1500, "score": 4},
    {"name": "Biomass Boiler System", "cost": 180000, "savings": 31000, "score": 5},
    {"name": "Uninterrupted Eco-UPS", "cost": 22000, "savings": 3000, "score": 3},
    {"name": "Regenerative Elevator Driver", "cost": 140000, "savings": 22000, "score": 4},
    {"name": "Smart Power Strips (Bundle)", "cost": 3500, "savings": 800, "score": 3},
    {"name": "Library LED Projectors", "cost": 18000, "savings": 5000, "score": 4},
    {"name": "Absorption Cooler", "cost": 40000, "savings": 6200, "score": 4},
    {"name": "Heat Recovery Ventilator", "cost": 55000, "savings": 11000, "score": 4},
    {"name": "High-Efficiency Air Compressor", "cost": 75000, "savings": 13500, "score": 3},
    {"name": "Solar Tube Solar System", "cost": 28000, "savings": 6000, "score": 5}
]

df = pd.DataFrame(device_data) # preproccessing of data as table for operations

# Z = E_i * S_i formulation applied for compute sustanability score
df['impact_value'] = df['savings'] * df['score']


print("====================================================")
print("  GREEN CITY PROJECT        ")
print("====================================================\n")
    
budget = int(input("Enter the budget (TRY): ")) # takes budget from user as integer
n = len(df) # n stores the total device number which is 20
    
dp = {}
for w in range(budget + 1):
    dp[w] = 0 # it sets the starting environmental score (Z) to 0 for every budget level from 0 to max,because before checking any devices, the initial benefit at any budget is zero. 
              # this serves as the mandatory baseline for the dynamic programming algorithm.
        
selected_at_w = {}# for follow the chosen devices, the devices that take in each budget step, store them.
for w in range(budget + 1):
    selected_at_w[w] = []
    
    
for i in range(n):
    cost = df.loc[i, 'cost'] # stores each devices cost
    value = df.loc[i, 'impact_value']# stores each devices Z values
        
        
    for w in range(budget, cost - 1, -1): #iterates backwards to prevent selecting the same device multiple times (0/1 Knapsack principle)
        if dp[w - cost] + value > dp[w]: # checks if buying the current device yields a higher score than the previous best combination at this budget
            dp[w] = dp[w - cost] + value #updates the maximum environmental value for the current budget step w
            selected_at_w[w] = selected_at_w[w - cost] + [i] #appends the current device's index to the winning list of the remaining budget path
                

final_indices = selected_at_w[budget] # I directly pulled the list of chosen device numbers for our budget from the dictionary
df_selected = df.iloc[final_indices] # I used .iloc tool to quickly look up and separate the rows of these chosen devices from the main list
    
# printing results on screen
print("\n-------------- CHOOSEN DEVICES ----------------")
for i in range(len(df_selected)):
    print(f"- {df_selected.iloc[i]['name']} | Cost: {df_selected.iloc[i]['cost']:,} TRY | Savings: {df_selected.iloc[i]['savings']:,} kWh | Score: {df_selected.iloc[i]['score']}/5")
        
print("====================================================")
print(f"Total Cost:                     {df_selected['cost'].sum():,} TRY")
print(f"Total Energy Saving:      {df_selected['savings'].sum():,} kWh")
print(f"Total Sustainability Score (Z): {df_selected['impact_value'].sum():,}")
print("====================================================")