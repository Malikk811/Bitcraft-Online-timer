
import math

restart = 1
while restart != "x":
    print("Please enter only numbers and actual Values or it won't work. \nPlease also note that the result will be a very close approximation and actual time spent may vary due to multiple factors such as server / client lag")

    max_stam = int(input("Enter your max stamina : "))
    tick_time = float(input("Enter your time per tick : "))
    tool_power = int(input("Enter your tool's power : "))
    craft_effort = int(input("Enter your craft effort : "))
    craft_tier = int(input("Enter your craft tier : "))

    stam_list = [0.75, 0.89, 1.03, 1.16, 1.28, 1.41, 1.52, 1.64, 1.75, 1.86] #stamina drain values for tiers 1-10

    stam_drain = stam_list[craft_tier - 1]

    def timer_calcs(max_stam, tick_time, tool_power, craft_effort, stam_drain):
        number_of_actions = round(craft_effort / tool_power ,2) 
        total_craft_time_sec = round(number_of_actions * tick_time ,2) 
        total_craft_time_min = round(total_craft_time_sec / 60 ,2) 
        #stam_left = abs(max_stam - stam_drain * number_of_actions) #absolute number to get rid of negative stamina left. Don't really have a use for it yet but DONT DELETE IT
        stam_cost = number_of_actions * stam_drain    
        math.ceil(stam_cost) #ceiled the value because you can't spend less than 1 stamina
        number_of_stops = stam_cost / max_stam
        math.floor(number_of_stops) #floored the value because 0.5 stop wouldn't make sense
        time_before_resuming_craft_sec = round(total_craft_time_sec / number_of_stops ,2) 
        time_before_resuming_craft_min = round(time_before_resuming_craft_sec / 60 ,2) 
        print(f'Your total crafting time will be : {math.floor(total_craft_time_min)} minutes and {round((total_craft_time_sec % 60), 2)} seconds.' )
        if stam_cost > max_stam:
            print(f'You will need to resume the craft every {math.floor(time_before_resuming_craft_min)} minutes and {round((time_before_resuming_craft_sec % 60), 2)} seconds.')

    timer_calcs(max_stam, tick_time, tool_power, craft_effort, stam_drain)
    restart = input("Press ENTER to continue or 'x' to exit : ")
