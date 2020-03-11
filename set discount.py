def car():
    car_prices=eval(input("Enter car prices:")
    discountset={}
    for i in car_prices:
                    discount=i*(20/100)
                    discountset.add(discount)
    print(discountset)
car()
    
