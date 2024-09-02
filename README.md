This is the GUI Calculator, used for user friendly calculation for hard to easy calculation.
Here different libraries used which are tkinter, sympy and regular expression.
Sympy is used instead of eval, beacue it is more safer and secure than eval(), becaue eval() at the back end programmin connect to the system which is less secure.
Different widgets are used for the UI design like buttons and Text.
Button are widgets that have many properties like text, padx, pady, font, bg, command. By using them button are looks more attractive.
Text widget has same propert as button..grid() method is used for placing those widget on the frame.
Different functions are made for implementing logic.
validate_input()-> used for validate the user input.
on_button_click()-> used for enter the perticular  value in the text field.
button_click()-> used for enter different number in the text field.
button_click_dot()-> Enter the dot in the text field,and also validate that user can't enter .. at the single timme.
clear_all()-> clear the whole Text are.
backspase()-> clear the latest digit from the text field.
clear_last_digit()-> remove the whole last number from the text field.
equals()-> Computes the expresstion that user give to evaluate.
one_by_x()-> compute the 1/x operation.
square_of_variable()-> Finds the square of a number using .subs(x, number) method.
square_root()-> Calculate the square root using sp.sqrt(number), where sp is intialized as sympy
toggle_button()-> This button converts positive number to negative, and vise a versa.
factorial()-> Finds the factorial of a number using sp.factorial() method.
absolute()-> Finds the absolute value of a number using sp.Abs(number)
