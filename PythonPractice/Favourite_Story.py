#This is a dictionary which will store users favourite shows/movies...
responses = {} #Stores people names and results...
polling_results = True

while polling_results:
    name = input('Please enter your name: ')
    response = input('Please enter what is your favourite work of fiction: ')
    responses[name] = response
    repeated = input('Is there anyone else who wants to share...\nIf not please enter "n" and if yes please enter "y"')
    if repeated == "n".lower():
        polling_results = False

print("......Here is the list......")
for name, response in responses.items():
    print(f'{name.title()}\'s favourite work of fiction is {response}')

print("Thank You for filling out")