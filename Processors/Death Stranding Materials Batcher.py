# 2/1/2023 - Death Stranding Materials Batcher
# This script takes a 'total materials needed' amount and gives the player the size and amount of batches to bring.

## [Challenges]
## To maximize amounts while minimizing batches, make it so that the program loops through the list backwards. And if the lowest amount equals twice the amount of the previous amount. Remove the smallest batch and append to the previous batch. Repeat until there are no unnecessary batches.

from math import trunc

# Variables
metals = [1000, 800, 600, 400, 200, 100, 50]
ceramics = [800, 640, 480, 320, 160, 80, 40]

material_list = "- Ceramic\n- Metal"

user_input = ""
materials = None
amount = 0


def calculate_batches(mat_list, amount):
    initial_amount = amount
    current_total = amount
    batches = []
    clean_list = []
    recommended_sum = 0
    for batch in mat_list:
        if amount >= batch:
            batches.append((batch, trunc(amount / batch)))
            amount = amount - (batch * trunc(amount / batch))
    if 0 < amount < mat_list[len(mat_list) - 1]:
        if batches[len(batches) - 1][0] == mat_list[len(mat_list) - 1]:
            batches[len(batches) - 1] = (mat_list[len(mat_list) - 1],
                                         batches[len(batches) - 1][1] + 1)
        else:
            batches.append((mat_list[len(mat_list) - 1], 1))
    # If there are two of the smallest batch numbers, remove them and add to the previous batch size amount
    if batches[len(batches) - 1][0] == mat_list[len(mat_list) -
                                                1] and batches[len(batches) -
                                                               1][1] == 2:
        batches.pop()
        print("smallest batch popped.")
        if batches[len(batches) - 1][0] == mat_list[len(mat_list) - 2]:
            print("Adding to the 2nd smallest batch.")
            batches[len(batches) - 1] = (mat_list[len(mat_list) - 2],
                                         batches[len(batches) - 1][1] + 1)
        else:
            print("Adding 2nd smallest batch to recommended batches.")
            batches.append((mat_list[len(mat_list) - 2], 1))
    for item in batches:
        recommended_sum = recommended_sum + (item[0] * item[1])
        clean_list.append((str(item[0]) + " x " + str(item[1])))
        print(
            str(item[0]) + ": " + str(item[1]) + " (" + f"{current_total:,}" +
            " - " + f"{item[0] * item[1]:,}" + " = " +
            f"{current_total - (item[0] * item[1]):,}" + ")")
        current_total = current_total - (item[0] * item[1])
    if recommended_sum == initial_amount:
        print("Perfect batch, no surplus\n")
    else:
        print(f"Surplus: {recommended_sum:,} - {initial_amount:,} = {recommended_sum - initial_amount:,}")
    print("[Paste List Below:]\n" + ', '.join(clean_list))


# User Menu
while True:
    try:
        user_input = input("Select a Material:\n" + material_list +
                           "\n(Quit)\n\n").lower()
    except Exception:
        print("Invalid input. Select One:\n" + material_list + "\n(Quit)\n\n")
    if user_input == "metal":
        material = metals
    elif user_input == "ceramic":
        material = ceramics
    elif user_input == "quit":
        print("Ending program.")
        break
    else:
        print("Select a Material:\n" + material_list + "\n\n")
    amount = int(input("\nEnter the amount needed:\n"))
    calculate_batches(material, amount)
