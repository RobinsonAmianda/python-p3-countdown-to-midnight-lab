# your code goes here!
import time 
def countdown(number = 10):
    while number > 0:
        print(f"{number} SECONDS(S)!")
        number = number - 1
    print("HAPPY NEW YEAR!")

print("```console")    
def countdown_with_sleep(number = 10):
    while number > 0:
        print(f"# => {number} SECONDS(S)!")
        time.sleep(1)
        number = number - 1
    print("# => HAPPY NEW YEAR!")
    print("```")
countdown_with_sleep(10)