from tkinter import *
from tkinter import scrolledtext

def display1():
    def close_window():
        new_window.destroy()

    new_window = Toplevel()
    new_window.title("Largest Prime Factor")
    new_window.attributes('-fullscreen', True)

    code = """ 
    n = int(input("Enter the Number: "))
    maxPrime = -1

    while n % 2 == 0:
        maxPrime = 2
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n // i

    if n > 2:
        maxPrime = n

    print("Max Prime Factor:", int(maxPrime))
    """

    code_display = scrolledtext.ScrolledText(new_window, font=('Arial', 20))
    code_display.pack(expand=True, fill='both')
    code_display.insert(END, code)

    button_exit = Button(new_window, text="Exit", command=close_window, font=('Arial', 25), width=25, bg="white", fg="red")
    button_exit.pack(pady=25)

def execute1():
    new_window = Toplevel()
    new_window.configure(bg="white")
    new_window.title("Prime Factor Calculation")
    
    label = Label(new_window, text='Enter the Number:', font=('Arial', 20), bg="white")
    label.pack()

    n_entry = Entry(new_window, font=('Arial', 20))
    n_entry.pack()

    def calculate_max_prime():
        try:
            num = int(n_entry.get())
            max_prime = -1
            
            while num % 2 == 0:
                max_prime = 2
                num //= 2

            for i in range(3, int(num**0.5) + 1, 2):
                while num % i == 0:
                    max_prime = i
                    num //= i

            if num > 2:
                max_prime = num

            result_label.config(text=f"Max Prime Factor: {max_prime}")

        except ValueError:
            result_label.config(text="Invalid Input! Please enter a valid number.")

    button = Button(new_window, text='Find Max Prime', font=('Arial', 20), command=calculate_max_prime, bg="white", fg="black")
    button.pack()

    result_label = Label(new_window, text="", font=('Arial', 20), bg="white")
    result_label.pack()

def display2():
    def close_window():
        new_window.destroy()

    new_window = Toplevel()
    new_window.title("List Manipulation")
    new_window.attributes('-fullscreen', True)

    code = """ 
    numbers = []
    n = int(input("Enter Size of the List: "))

    while n > 0:
        i = int(input("Enter the element to insert: "))
        numbers.append(i)
        n -= 1

    print("List:", numbers)

    while True:
        print("=====Menu=====")
        print("1. Insert at specific position  2. Remove value  3. Append value  4. Display list  5. Exit")
        choice = int(input("Enter the choice: "))

        if choice == 1:
            position = int(input("Enter the position: "))
            item = int(input("Enter the item: "))
            numbers.insert(position, item)

        elif choice == 2:
            position = int(input("Enter the position to remove: "))
            numbers.pop(position)

        elif choice == 3:
            item = int(input("Enter the item to append: "))
            numbers.append(item)

        elif choice == 4:
            print("List Content:", numbers)

        elif choice == 5:
            print("Exiting...")
            break
    """

    code_display = scrolledtext.ScrolledText(new_window, font=('Arial', 20))
    code_display.pack(expand=True, fill='both')
    code_display.insert(END, code)

    button_exit = Button(new_window, text="Exit", command=close_window, font=('Arial', 25), width=25, bg="white", fg="red")
    button_exit.pack(pady=25)

def execute2():
    new_window = Toplevel()
    new_window.configure(bg="white")
    new_window.title("List Operations")

    label = Label(new_window, text="Enter Space-Separated Numbers:", font=('Arial', 20), bg="white")
    label.pack()

    entry1 = Entry(new_window, font=('Arial', 20))
    entry1.pack()

    numbers = []

    def create_list():
        nonlocal numbers
        try:
            numbers = list(map(int, entry1.get().split()))
            result_label.config(text=f"List: {numbers}")
        except ValueError:
            result_label.config(text="Invalid Input! Enter space-separated numbers.")

    def insert_element():
        try:
            pos = int(entry2.get())
            val = int(entry3.get())
            numbers.insert(pos, val)
            result_label.config(text=f"Updated List: {numbers}")
        except (ValueError, IndexError):
            result_label.config(text="Invalid Position or Value!")

    def delete_element():
        try:
            pos = int(entry4.get())
            numbers.pop(pos)
            result_label.config(text=f"Updated List: {numbers}")
        except (ValueError, IndexError):
            result_label.config(text="Invalid Position!")

    def append_element():
        try:
            val = int(entry5.get())
            numbers.append(val)
            result_label.config(text=f"Updated List: {numbers}")
        except ValueError:
            result_label.config(text="Invalid Value!")

    entry2, entry3, entry4, entry5 = Entry(new_window, font=('Arial', 20)), Entry(new_window, font=('Arial', 20)), Entry(new_window, font=('Arial', 20)), Entry(new_window, font=('Arial', 20))

    Button(new_window, text="Create List", font=('Arial', 20), command=create_list, bg="white").pack()
    Button(new_window, text="Insert", font=('Arial', 20), command=insert_element, bg="white").pack()
    Button(new_window, text="Delete", font=('Arial', 20), command=delete_element, bg="white").pack()
    Button(new_window, text="Append", font=('Arial', 20), command=append_element, bg="white").pack()

    result_label = Label(new_window, text="", font=('Arial', 20), bg="white")
    result_label.pack()

# Main Window
window = Tk()
window.configure(bg="white")
window.attributes('-fullscreen', True)
window.title("RV College of Engineering")

Label(window, text='RV COLLEGE OF ENGINEERING', font=('Comic Sans', 20, 'bold'), bg="white").pack()

Label(window, text="Program to find the largest prime factor:", font=('Arial', 30, 'bold'), bg="white").place(x=0, y=100)
Button(window, text='Display Program', font=('Comic Sans', 20, 'bold'), command=display1, bg="white").place(x=50, y=150)
Button(window, text='Execute', font=('Comic Sans', 20, 'bold'), command=execute1, bg="white").place(x=50, y=220)

Label(window, text="Program for list operations:", font=('Arial', 30, 'bold'), bg="white").place(x=0, y=270)
Button(window, text='Display Program', font=('Comic Sans', 20, 'bold'), command=display2, bg="white").place(x=50, y=320)
Button(window, text='Execute', font=('Comic Sans', 20, 'bold'), command=execute2, bg="white").place(x=50, y=390)

window.mainloop()
