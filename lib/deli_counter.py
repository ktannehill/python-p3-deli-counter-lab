def line(list):
    if len(list) == 0:
        print("The line is currently empty.")
    else:
        current_line = ["The line is currently:"]
        for index in range(len(list)):
            current_line.append(f"{index + 1}. {list[index]}")
        print(" ".join(current_line))

def take_a_number(list, name):
    list.append(name)
    print(f"Welcome, {name}. You are number {list.index(name) + 1} in line.") 


def now_serving(list):
    if len(list):
        print(f"Currently serving {list[0]}.")
        list.pop(0)
    else:
        print("There is nobody waiting to be served!")