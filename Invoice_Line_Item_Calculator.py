# Johannes Dzidzienyo - CIS 261003-VA016-1232-001 - Week 6 Part 1 Lab

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid price. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity. Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    answer = "y"
    while answer.lower() == "y":
        # get the price and quantity
        price = get_price()
        quantity = get_quantity()
    
        # calculate the total
        total = price * quantity

        # display the results
        print()
        print("PRICE:    ", f"{price: .2f}")
        print("QUANTITY: ", quantity)
        print("TOTAL:    ", f"{total: .2f}")
        answer = input("To enter another line ite, type (y). To quit, type (n): ")
        print()
        
    print("Goodbye!")


if __name__ == "__main__":
    main()
