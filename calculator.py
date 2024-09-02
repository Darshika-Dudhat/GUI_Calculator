from tkinter import *
import sympy as sp
import re

root = Tk()   # create root window
root.title("Calculator")  #set title for the window

root.geometry("310x390")  #set geometry for the calculator``

#root.config(bg="black")

frame = Frame(root)  #create frame inside root window
#frame.config(bg="black")
frame.pack()       # To set frame within the root


def validate_input(new_value):
    # Allow empty input
    if new_value == "":
        return True
    
    # Allow digits, arithmetic symbols, and a decimal point
    allowed_symbols = set("+-*/.%()'Cannot divide by zero'")
    if all(char.isdigit() or char in allowed_symbols for char in new_value):
        try:
            # Try to convert to float (ignoring cases where symbols make it invalid)
            float(new_value)
        except ValueError:
            pass  # Ignore if the string contains symbols like +, -, *, /
        return True
    return False

def on_button_click(symbol):
    current_text = entry.get()

    # does not allow enter two symbol at one position
    if current_text[-1].isdigit() or current_text[-1] == ")":
        entry.insert( END, symbol)
    elif not current_text[-1].isalpha():
        entry.delete(len(current_text) - 1,END)
        entry.insert( END, symbol) 

    # only allow one decimal point at a time
    if button_dot['state'] == DISABLED:
        button_dot.config(state=NORMAL)

def bracket_called(symbol):
    entry.insert(END,symbol)

validation = frame.register(validate_input)

entry = Entry(frame, validate="key",width=40, validatecommand=(validation, "%P"),justify='right', font=("arial",10))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=12,ipadx=10,ipady=10)

def button_click(value):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(value))

def button_click_dot(value):
    # only one deimal point at a time
    entry.insert(END,".")
    button_dot.config(state=DISABLED)

def clear_all():
    entry.delete(0,END)

def backspase():
    # remove last number or symbol
    current_text = entry.get()
    new_text = current_text[:-1]
    entry.delete(0, END)
    entry.insert(0, new_text)

def clear_last_digit():
    expression = entry.get()
    # Find the last whole number in the string
    last_number_match = re.search(r'\d+(?!.*\d)', expression)

    if last_number_match:
        # Position of the last number
        last_number_position = last_number_match.start()

        # Remove the last number 
        modified_expression = expression[:last_number_position]
        # modified_expression = expression[:last_number_position].rstrip("+-*/")
    else:
        # If no number is found, return the original expression
        modified_expression = expression

    entry.delete(0,END)
    entry.insert(0,modified_expression)
    
def equals():
    global expression
    try:
        expression = entry.get()
        result = sp.sympify(expression)
        if result == sp.zoo:
            error = "Cannot divide by zero"
            entry.delete(0, END)
            entry.insert(0,error)
        else:
            result = f"{result:.2f}"
            entry.delete(0, END)
            entry.insert(0,result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

def one_by_x():
    number = float(entry.get())
    if number == 0:
        entry.delete(0, END)
        entry.insert(0, "Cannot divide by zero")

    else:
        result = 1 / number
        entry.delete(0, END)
        entry.insert(0, f"{result:.2f}")

def square_of_variable():
    number = entry.get()

    x = sp.Symbol('x')
    expr = x**2
    evaluated_expr = expr.subs(x, number)
    result = float(evaluated_expr)
    entry.delete(0, END)
    entry.insert(0,result)

def square_root():
    number = int(entry.get())
    result = sp.sqrt(number)

    entry.delete(0, END)
    entry.insert(0,result)

def toggle_button():
    current_text = entry.get()
    if current_text:
        # Split the current value into parts: numbers and operators
        parts = re.split(r'([+\-*/%])', current_text)  # Split by operators, keep them in the list

        if parts[-1] in "+-/*%":
            parts.append('-')
        else:
            last_part = parts[-1]
            # If the last part starts with a '-', remove it
            if last_part.startswith('-'):
                parts[-1] = last_part[1:]
            else:
                # If the last part doesn't start with a '-', add a '-'
                parts[-1] = '-' + last_part

        # Reconstruct the expression from the parts
        new_text = ''.join(parts)
        entry.delete(0, END)
        entry.insert(0, new_text)

def factorial():
    number = entry.get()
    result = round(sp.factorial(number),2)

    entry.delete(0,END)
    entry.insert(0,result)

def absolute():
    number = entry.get()

    result = round(sp.Abs(number),2)
    entry.delete(0,END)
    entry.insert(0,result)
        
#Define Buttons

button_modulo = Button(frame, text="%", padx=7, pady=10, width=5, bg="lightblue",font=("arial",10,"bold"),command=lambda: on_button_click("%"))  
button_clear_last_digit = Button(frame, text="CE", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=clear_last_digit)  
button_clear_all = Button(frame, text="C", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=clear_all)  
button_backspace = Button(frame, text="⌫", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=backspase)  

button_left_bracket = Button(frame, text="(", padx=7, pady=10, width=5, bg="lightblue",font=("arial",10,"bold"),command=lambda: bracket_called("("))  
button_factorial = Button(frame, text="n!", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=factorial)  
button_right_bracket = Button(frame, text=")", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=lambda: bracket_called(")"))  
button_absolute = Button(frame, text="|x|", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=absolute)  

button_divide_value = Button(frame, text="1/x", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=one_by_x)  
button_square = Button(frame, text="x²", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=square_of_variable)  
button_square_root = Button(frame, text="√x", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=square_root)  
button_division = Button(frame, text="/", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=lambda: on_button_click("/"))  

button_seven = Button(frame, text="7", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(7))  
button_eight = Button(frame, text="8", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(8))  
button_nine = Button(frame, text="9", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(9))  
button_multiply = Button(frame, text="X", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=lambda: on_button_click("*")) 

button_four = Button(frame, text="4", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(4))  
button_five = Button(frame, text="5", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(5))  
button_six = Button(frame, text="6", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(6))  
button_minus = Button(frame, text="–", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=lambda: on_button_click("-"))

button_one = Button(frame, text="1", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(1))  
button_two = Button(frame, text="2", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(2))  
button_three = Button(frame, text="3", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(3)) 
button_plus = Button(frame, text="+", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=lambda: on_button_click("+"))  

button_toggle = Button(frame, text="+/-", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"),command=toggle_button)  
button_zero = Button(frame, text="0", padx=7, pady=10, width=5, bg="lightgrey", font=("arial",10,"bold"), command=lambda:button_click(0))  
button_dot = Button(frame, text=".", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=lambda:button_click_dot("."))  
button_equals = Button(frame, text="=", padx=7, pady=10, width=5, bg="lightblue", font=("arial",10,"bold"), command=equals)  

# To place the button inside frame within root

button_modulo.grid(row=1, column=0)
button_clear_last_digit.grid(row=1, column=1)
button_clear_all.grid(row=1, column=2)  
button_backspace.grid(row=1, column=3) 

button_left_bracket.grid(row=2, column=0)
button_factorial.grid(row=2, column=1)
button_right_bracket.grid(row=2, column=2)  
button_absolute.grid(row=2, column=3) 

button_divide_value.grid(row=3, column=0)
button_square.grid(row=3, column=1)
button_square_root.grid(row=3, column=2)  
button_division.grid(row=3, column=3) 

button_seven.grid(row=4, column=0)
button_eight.grid(row=4, column=1)
button_nine.grid(row=4, column=2)  
button_multiply.grid(row=4, column=3) 

button_four.grid(row=5, column=0)
button_five.grid(row=5, column=1)
button_six.grid(row=5, column=2)  
button_minus.grid(row=5, column=3) 

button_one.grid(row=6, column=0)
button_two.grid(row=6, column=1)
button_three.grid(row=6, column=2)  
button_plus.grid(row=6, column=3) 

button_toggle.grid(row=7, column=0)
button_zero.grid(row=7, column=1)
button_dot.grid(row=7, column=2)  
button_equals.grid(row=7,column=3) 
             
root.mainloop()