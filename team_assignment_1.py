"""
Erkinbek
11/13/2022
write a program to print a number of options presented to
the user and allow the user to select an option from the list.
"""
print("Choose the kitchen to make a choice\n"
      "1.Italian Cuisine\n"
      "2.British Cuisine\n"
      "3.The Mediterranean Food\n"
      "4.Indian Cuisine\n"
      "5.Central Asian Cuisine\n"
      "6.Traditional American\n")
order_id = int(input("My choice is "))

if order_id == 1:
      print(
      "We have amazing  foods:\n"
      "1.Spaghetti\n"
      "2.Napoletana Pizza\n"
      "3.Risotto\n"
      "4.Fiorentina Steak\n"
      "5.Polenta\n"
      "6.Lasagne\n")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type == 2:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 2:
      print(
      "Currently British chef offers:\n"
      "1.Shepherd's Pie\n"
      "2.Beef Wellington\n"
      "3.Fish and Chips\n"
      "4.Chicken Tikka Masala\n"
      "5.Steak and Kidney Pie\n"
      "6.Eton Mess")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type == 2:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 3:
      print(
      "Especially for you we cook:\n"
      "1.Pita\n"
      "2.Moussaka\n"
      "3.Greek Salad\n"
      "4.Baklava\n"
      "5.Dolmas\n"
      "6.Borek")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type == 2:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 4:
      print(
      "OMG spicy:\n"
      "1.Masala dosa\n"
      "2.Chaat\n"
      "3.Dal makhani\n"
      "4.Vada pav\n"
      "5.Stuffed paratha\n"
      "6.Dhokla")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type == 2:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 5:
      print(
      "Dishes with love:\n"
      "1.Manty\n"
      "2.Ash\n"
      "3.Samsa\n"
      "4.Kuurdak\n"
      "5.Besh barmak\n"
      "6.Shorpo")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 6:
      print(
      "Just in couple minutes:\n"
      "1.Burger\n"
      "2.Apple pie\n"
      "3.French Fries\n"
      "4.Hot Dogs\n"
      "5.Fried Chicken\n"
      "6.Grilled cheese")
      order_food = int(input("I wish "))
      order_type = int(input("1-delivery, 2-dine in "))
      if order_type == 1:
            print("Your order should be delivered the next 30 minutes.")
      elif order_type:
            print("Welcome please, take a seat!")
      elif order_type == 0:
            print("Goodbye")
elif order_id == 0:
      print("Goodbye")
