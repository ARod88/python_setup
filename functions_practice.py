def hello():
    print("Hello user")

hello()

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

result = pack("orange", 13, [ 1, 2, 3])
print(result)

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[0]}")
            else: 
                print(f"Next I eat {food_list[i]}")

hello()
print(pack("arg1","arg2", "arg3"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["burger"])
eat_lunch(["orange","strawberry","burger","chips"])