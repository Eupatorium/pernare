option = int(input("Write 1 to find calculate and 2 to calculate perimeter"))

if 1 == option:

  print("Select the shape for which the area needs to be calculated")

  print("1. Rectangle")
  print("2. Square")
  print("3. Circle")
  print("4. Triangle")
  print("5. Trapezium")

  choice=int(input("Enter your choice: "))

  if choice == 1:
    l = int(input("Enter Length"))
    b = int(input("Enter breadth"))
    areaone = l*b
    print ("Your area is", areaone)

  elif choice==2:
    l = int(input("Enter the length"))
    areatwo = l*l
    print ("Your area is", areatwo)

  elif choice==3:
    radius = int(input("Enter a radius"))
    areathree = 3.14*radius*radius
    print ("Your area is", areathree)

  elif choice==4:
    b = int(input("Enter a base"))
    h = int(input("Enter a height"))
    areafour = 0.5*b*h
    print ("Your area is", areafour)

  elif choice==5:
    a = int(input("Enter first length"))
    b = int(input("Enter second length"))
    h = int(input("Enter height"))
    areafive = 0.5*(a+b)*h
    print("Your area is",areafive)

  else:
    print ("Wrong choice")

if 2==option:

  print("Select the shape for which the perimeter needs to be calculated")
  
  print("1. Rectangle")
  print("2. Square")
  print("3. Circle")
  print("4. Triangle")
  print("5. Trapezium")

  choice=int(input("Enter your choice: "))

  if choice==1:
    l = int(input("Enter Length"))
    b = int(input("Enter breadth"))
    perone = 2*(l+b)
    print ("Your perimeter is", perone)

  elif choice==2:
    l = int(input("Enter the length"))
    pertwo = 4*l
    print ("Your perimeter is", pertwo)
    
  elif choice==3:
    radius = int(input("Enter a radius"))
    perthree = 2*3.14*radius
    print ("Your perimeter is", perthree)

  elif choice==4:
    l = int(input("Enter a length"))
    b = int(input("Enter a base"))
    s = int(input("Enter a side"))
    perfour = l+b+s
    print ("Your perimeter is", perfour)

  elif choice==5:
    a = int(input("Enter first side"))
    b = int(input("Enter second side"))
    c = int(input("Enter third side"))
    d = int(input("Enter fourth side"))
    perfive = a+b+c+d
    print ("Your perimeter is", perfive)
  
  else:
    print ("Wrong choice")





