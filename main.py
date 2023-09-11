import matplotlib.pyplot as plt

# Carbon emissions data (in kgCO2e per activity per hour) 

CARBON_EMISSIONS = {

 'car': 0.2,

 'bus': 0.1,

 'bike': 0,

 'walk': 0,

 'ac': 0.5,

 'heating': 0.3,

 'electricity': 0.4,

 # Add more activities and their emissions data here

}

def calculate_carbon_footprint(activities):

 total_emissions = sum(CARBON_EMISSIONS.get(activity, 0) for activity in activities)

 return total_emissions
def visualize_carbon_footprint(emissions_data): 

 activities = list(emissions_data.keys()) 

 emissions = list(emissions_data.values()) 

 plt.bar(activities, emissions) 

 plt.xlabel('Activity') 

 plt.ylabel('Carbon Footprint (kgCO2e)') 

 plt.title('Carbon Footprint of Daily Activities') 

 plt.xticks(rotation=45) 

 plt.show() 

def main(): 

 print("Welcome to the Carbon Footprint Calculator!") 

 print("Enter the activities you engage in during a day (comma-separated).") 

 print("Activities: car, bus, bike, walk, ac, heating, electricity") 

 user_input = input("Activities: ").strip().lower() 

 user_activities = user_input.split(',') 

 carbon_footprint = calculate_carbon_footprint(user_activities) 

 print(f"\nYour estimated carbon footprint: {carbon_footprint:.2f} kgCO2e per day") 

 # Visualize the carbon footprint breakdown 

 emissions_data = {activity: CARBON_EMISSIONS.get(activity, 0) for activity in 

user_activities} 

 visualize_carbon_footprint(emissions_data) 

 # Tips to reduce carbon footprint 

 print("\nTips to Reduce Your Carbon Footprint:") 

 print("- Use public transportation or cycle instead of driving.") 

 print("- Walk for short distances.") 

 print("- Turn off AC/heating when not needed.") 
print("- Use energy-efficient appliances.")

 # Add more tips here based on real-world recommendations

if __name__ == "__main__":

 main()