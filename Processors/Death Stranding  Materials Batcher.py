# 2/1/2023 - Death Stranding Materials Batcher
# This script takes a 'total materials needed' amount and gives the player the size and amount of batches to bring.

from math import trunc

metals = [1000, 800, 600, 400, 200, 100, 50]
ceramics = [800, 640, 480, 320, 160, 80, 40]


def calculate_batches(mat_list, amount):
  initial_amount = amount
  batches = []
  sum = 0
  for batch in mat_list:
    if amount >= batch:
      batches.append((batch, trunc(amount / batch)))
      amount = amount - (batch * trunc(amount / batch))
  if amount > 0 and amount < mat_list[len(mat_list) - 1]:
    if batches[len(batches) - 1][0] == mat_list[len(mat_list) - 1]:
      batches[len(batches) - 1] = (mat_list[len(mat_list) - 1],
                                   batches[len(batches) - 1][1] + 1)
    else:
      batches.append((mat_list[len(mat_list) - 1], 1))
  for item in batches:
    sum = sum + (item[0] * item[1])
    print(str(item[0]) + ": " + str(item[1]))
  print("Surplus: " + str(sum) + " - " +
        str(initial_amount).format("###,###") + " = " +
        str(sum - initial_amount))
  if sum == initial_amount:
    print("Perfect batch, no surplus.")


# Variables
user_input = ""
materials = None
amount = 0

while True:
  try:
    user_input = input("Select a Material:\nMetal\nCeramic\n\n").lower()
  except Exception:
    print("Invalid input. Select 'Metal' or 'Ceramic'.")
  if user_input == "metal":
    material = metals
    break
  elif user_input == "ceramic":
    material = ceramics
    break
  else:
    print("Type 'Metal' or 'Ceramic'")

amount = int(input("Enter the amount needed:\n"))
calculate_batches(material, amount)
