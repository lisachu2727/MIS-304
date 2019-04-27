#Tzu-Chuan Chu

#Importing tkinter and messagebox
import tkinter
from tkinter import messagebox

#Declaring cake price and tax constants
TAX = 0.07
CHOCOLATE = 5.00
BUTTER = 7.50

#Declaring class cake  
class cake:

    #Defining init function
    def __init__(self):
        #Initializing main window
        self.main_window = tkinter.Tk()

        #Initializing frames
        self.label_frame = tkinter.Frame(self.main_window)
        self.choice_frame = tkinter.Frame(self.main_window)
        self.quantity_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        
        #Label for chocolate cake
        self.cake_label1 = tkinter.Label(self.label_frame,
                                         text = 'A - Chocolate Icing Cake')
        self.cake_label1.pack(side = 'top')

        #Label for butter cake
        self.cake_label2 = tkinter.Label(self.label_frame,
                                         text = 'B - Butter Cake')
        self.cake_label2.pack(side = 'top')

        #Entry box for choice
        self.choice_label = tkinter.Label(self.choice_frame,
                                          text = 'Please enter a choice: ')
        self.choice_entry = tkinter.Entry(self.choice_frame,
                                          width = 10)
        self.choice_label.pack(side = 'left')
        self.choice_entry.pack(side = 'left')
        
        #Entry box for quantity
        self.quantity_label = tkinter.Label(self.quantity_frame,
                                            text = 'Please enter a quantity: ')
        self.quantity_entry = tkinter.Entry(self.quantity_frame,
                                            width = 10)
        self.quantity_label.pack(side = 'left')
        self.quantity_entry.pack(side = 'left')
        
        #Buttons in bottom frame
        self.purchase_button = tkinter.Button(self.button_frame,
                                              text = 'Purchase',
                                              command = self.purchaseButton)
        self.purchase_button.pack(side = 'left')
                                              
        self.quit_button = tkinter.Button(self.button_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        self.quit_button.pack(side = 'left')

        #Packing frames
        self.label_frame.pack(side = 'top')
        self.choice_frame.pack(side = 'top')
        self.quantity_frame.pack(side = 'top')
        self.button_frame.pack(side = 'top')

        #Looping program
        tkinter.mainloop()

    #Defining function for purchase button
    def purchaseButton(self):

        #Retrieving quantity from entry box
        quantity = int(self.quantity_entry.get())

        #Decision making for valid quantity and chocolate cake
        if self.choice_entry.get() == 'A' and quantity > 0:
            #Calculating costs
            cost = quantity * CHOCOLATE * (1 + TAX)
            #Message box
            tkinter.messagebox.showinfo('Purchase',
                                        'The price for ' + str(quantity) +
                                        ' chocolate icing cake(s) is $' +
                                        str(format(cost,'.2f')))

        #Decision making for valid quantity and butter cake                                             
        elif self.choice_entry.get() == 'B' and quantity > 0:
            #Calculating costs
            cost = quantity * BUTTER * (1 + TAX)
            #Message box
            tkinter.messagebox.showinfo('Purchase',
                                        'The price for ' + str(quantity) +
                                        ' butter cake(s) is $' +
                                        str(format(cost,'.2f')))

        #Decision making for invalid entries
        else:
            tkinter.messagebox.showinfo('Error', 'Invalid input. Try Again.')

#Running program
my_cake = cake()
                                       
        
