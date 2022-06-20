import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time

# Generates an array of random numbers of given length
def generate_random_array(length):
    randomlist = random.sample(range(-2147483648 , 2147483648 ), length)
    return randomlist

# Clears log shown
def clear_log():
    process_log.configure(state=NORMAL)
    process_log.delete('1.0', END)
    process_log.insert(tk.END, "Process Log")
    process_log.configure(state=DISABLED)


# Logs text
def log_message(message):
    process_log.configure(state=NORMAL)
    process_log.insert(tk.END, "\n"+message)
    process_log.see(tk.END)
    process_log.configure(state=DISABLED)


# Gets selected algorithm

gui = tk.Tk()
gui.title('Search Algorithms')
gui.geometry("600x700")

# Adding UI
var = StringVar()
label = Label( gui, textvariable=var)
var.set("Please select a search algorithm")
label.place(x = 40, y = 20)


# Update compare UI based on selected algorithm
def updateCompareAlgorithms():
    value = search_algo.get()
    if value == 1:
        print("Disabled linear search in compare")
        linear_search_var.set(0)
        linear_search_comp.configure(state=DISABLED)
        binary_search_sort_comp.configure(state=NORMAL)
        binary_search_tree_comp.configure(state=NORMAL)
        red_black_comp.configure(state=NORMAL)
    elif value == 2:
        binary_search_sort_var.set(0)
        print("Disabled binary search sorted in compare")
        linear_search_comp.configure(state=NORMAL)
        binary_search_sort_comp.configure(state=DISABLED)
        binary_search_tree_comp.configure(state=NORMAL)
        red_black_comp.configure(state=NORMAL)

    elif value == 3:
        binary_search_tree_var.set(0)
        print("Disable binary search tree in compare")
        linear_search_comp.configure(state=NORMAL)
        binary_search_sort_comp.configure(state=NORMAL)
        binary_search_tree_comp.configure(state=DISABLED)
        red_black_comp.configure(state=NORMAL)

    elif value == 4:
        red_black_var.set(0)
        print("Disabled red-black in compare")
        linear_search_comp.configure(state=NORMAL)
        binary_search_sort_comp.configure(state=NORMAL)
        binary_search_tree_comp.configure(state=NORMAL)
        red_black_comp.configure(state=DISABLED)

# Radio button
search_algo = IntVar()
linear_search = Radiobutton(gui, text="Linear Search", variable = search_algo, value = 1, command = updateCompareAlgorithms).place(x = 40,y = 40)
binary_search_in_sorted = Radiobutton(gui, text="Binary search in sorted array", variable = search_algo, value = 2, command = updateCompareAlgorithms).place(x = 220,y = 40)
binary_search_tree = Radiobutton(gui, text="Binary search tree", variable = search_algo, value = 3, command = updateCompareAlgorithms).place(x = 40,y = 60)
red_black = Radiobutton(gui, text="Red-Black Tree", variable = search_algo, value = 4, command = updateCompareAlgorithms).place(x = 220,y = 60)

search_algo.set(1)

input_size_var = tk.StringVar()

# Add input field to get array length
input_size = Label(gui, text = "Input size").place(x = 40,y = 90)
size_entry = tk.Entry(gui,textvariable = input_size_var, width = 31).place(x = 40,y = 110)


def radio_button():
    type = input_type.get()
    if type == 1:
        input_array_val.set("An array of random integers will be generated")
        input_array.config(state='disabled')
    else:
        input_array_val.set('')
        input_array.config(state='normal')


# Get input type
input_type_label = Label(gui, text="Input type").place(x=40, y=140)
input_type = IntVar()
generate_radio = Radiobutton(gui, text="Generate Random", variable = input_type, value = 1, command = radio_button).place(x = 40,y = 160)
manual_radio = Radiobutton(gui, text="Manual Input", variable = input_type, value = 2, command = radio_button).place(x = 190,y = 160)
input_type.set(1)
# Input for manual entry

input_array_val = tk.StringVar()
# Add input field to get array length
input_array_label = Label(gui, text = "Enter input values separated by space")
input_array_label.place(x = 40,y = 190)
input_array = tk.Entry(gui,textvariable = input_array_val, width = 31)
input_array.place(x = 40,y = 210)
input_array_val.set("An array of random integers will be generated")
input_array.config(state='disabled')


# Search element
search_val = tk.StringVar()
search_label = Label(gui, text="Enter search element").place(x=40, y = 250)
search_field = tk.Entry(gui,textvariable = search_val, width = 31).place(x = 40,y = 270)


# Linear Search

def linear_search(array, key):
    print("Linear Search")
    start_time = time.time()

    index = -1

    for pos, element in enumerate(array, start = 0):
        if element == key:
            index = pos
            break

    end_time = time.time()
    print("Execution time: ", end_time-start_time)

    if index != -1:
        log_message("\nElement found in list at index"+str(index+1))
    else:
        log_message("\nElement not found in list.")


    print("Execution time", end_time-start_time)

    log_message("Execution time: "+str(end_time-start_time))

def binary_search_sort(array, key):
    # Sorting array
    array.sort()
    print("Binary search sorted array")
    start_time  = time.time()

    start = 0
    end = len(array) - 1
    mid = 0

    index = -1

    while start <= end:

        mid = (end + start) // 2


        if array[mid] < key:
            start = mid + 1


        elif array[mid] > key:
            end = mid - 1

        else:
            index = mid
            break

    end_time = time.time()
    print("Execution time", end_time-start_time)

    if index != -1:
        log_message("\nElement found in list at index"+str(index+1))
    else:
        log_message("\nElement not found in list.")


    print("Execution time", end_time-start_time)

    log_message("Execution time: "+str(end_time-start_time))

def binary_search_tree(array, key):

    print("Binary search tree")
    start_time  = time.time()

    class Node:
        def __init__(self, element):
            self.left = None
            self.value = element
            self.right = None

    def insert_element(root, element):
        if root is None:
            return Node(element)
        else:
            if root.value == element:
                return root
            elif root.value < element:
                root.right = insert_element(root.right, element)
            else:
                root.left = insert_element(root.left, element)

        return root

    def search_element(root, key):
        return_status = False
        if root:
            if root.value == key:
                print("Element found")
                return True
            else:
                return_status = search_element(root.left, key)
                if return_status:
                    return return_status
                return_status = search_element(root.right, key)

                if return_status:
                    return return_status

        return return_status

    i = 0
    root = Node(array[i])
    for index in array:
        if i == 0:
            i = i+1
            continue
        else:
            root = insert_element(root, index)

    search_status = search_element(root, key)

    end_time = time.time()

    if search_status:
        log_message("\nElement found in list.")
    else:
        log_message("\nElement not found in list.")


    print("Execution time", end_time-start_time)

    log_message("Execution time: "+str(end_time-start_time))

def red_black(array, key):
    print("Red black Tree")
    print(array)
    class Node():
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.left = None
            self.right = None
            self.color = 1

    class RedBlackTree():
        def __init__(self):
            self.node = Node(0)
            self.node.color = 0
            self.node.left = None
            self.node.right = None
            self.root = self.node

        # Insert value to tree
        def insert_value(self, value):
            node = Node(value)
            node.parent = None
            node.value = value
            node.left = self.node
            node.right = self.node
            node.color = 1

            leaf = None
            root_ = self.root

            while root_ != self.node:
                leaf = root_
                if node.value < root_.value:
                    root_ = root_.left
                else:
                    root_ = root_.right

            node.parent = leaf
            if leaf == None:
                self.root = node
            elif node.value < leaf.value:
                leaf.left = node
            else:
                leaf.right = node

            if node.parent == None:
                node.color = 0
                return

            if node.parent.parent == None:
                return

            self.balance_tree(node)

        # Balance tree
        def balance_tree(self, k):
            while k.parent.color == 1:
                if k.parent == k.parent.parent.right:
                    u = k.parent.parent.left
                    if u.color == 1:
                        u.color = 0
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        k = k.parent.parent
                    else:
                        if k == k.parent.left:
                            k = k.parent
                            self.rotate_right(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.rotate_left(k.parent.parent)
                else:
                    u = k.parent.parent.right

                    if u.color == 1:
                        u.color = 0
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        k = k.parent.parent
                    else:
                        if k == k.parent.right:
                            k = k.parent
                            self.rotate_left(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.rotate_right(k.parent.parent)
                if k == self.root:
                    break
            self.root.color = 0

        # Rotate left
        def rotate_left(self, root_):
            leaf = root_.right
            root_.right = leaf.left
            if leaf.left != self.node:
                leaf.left.parent = root_

            leaf.parent = root_.parent
            if root_.parent == None:
                self.root = leaf
            elif root_ == root_.parent.left:
                root_.parent.left = leaf
            else:
                root_.parent.right = leaf
            leaf.left = root_
            root_.parent = leaf
        # Rotate right
        def rotate_right(self, root_):
            leaf = root_.left
            root_.left = leaf.right
            if leaf.right != self.node:
                leaf.right.parent = root_

            leaf.parent = root_.parent
            if root_.parent == None:
                self.root = leaf
            elif root_ == root_.parent.right:
                root_.parent.right = leaf
            else:
                root_.parent.left = leaf
            leaf.right = root_
            root_.parent = leaf

        # Search tree
        def search_tree(self, node, key):
            if node == None or key == node.value:
                return node

            if key < node.value:
                return self.search_tree(node.left, key)
            return self.search_tree(node.right, key)


    rbt = RedBlackTree()


    for element in array:
        rbt.insert_value(element)

    start_time = time.time()
    search_status = rbt.search_tree(rbt.root, key)

    end_time = time.time()

    if search_status:
        log_message("\nElement found in list.")
    else:
        log_message("\nElement not found in list.")


    print("Execution time", end_time-start_time)

    log_message("Execution time: "+str(end_time-start_time))



# Button to search
def searchElement():
    # Clear existing log message
    clear_log()
    # Validating inputs
    input_size = input_size_var.get().strip()

    type = input_type.get()

    input_elements = input_array_val.get().strip()

    search_element = search_val.get()
    search_array = []
    if not input_size or not int(input_size):
        print("Invalid input size")
        tk.messagebox.showerror("Error", "Invalid input size")
        return

    input_size = int(input_size)

    if not search_element or not int(search_element):
        print("Invalid search element")
        tk.messagebox.showerror("Error", "Invalid search element. Please enter an integer.")
        return

    search_element = int(search_element)


    if type == 1:
        # Generate random input_array
        search_array = generate_random_array(input_size)

    elif type == 2:
        try:
            # Convert to array
            search_array = input_elements.split()
            search_array = list(map(int, search_array))
        except Exception as error:
            print("An error occured", error)
            tk.messagebox.showerror("Error", "Invalid input. Please enter integers separated by space.")
            return

    # Check if length matches input size
    array_length = len(search_array)
    if input_size == array_length:
        # Get search algorithm
        print("Search element")
        search_type = search_algo.get()

        if search_type == 1:
            clear_log()
            log_message("\nSearching for element using Linear Search...")
            linear_search(search_array, search_element)

        elif search_type == 2:
            log_message("\nSearching for element using Binary Search in sorted list...")
            binary_search_sort(search_array, search_element)

        elif search_type == 3:

            log_message("\nSearching for element using Binary Tree Search...")
            binary_search_tree(search_array, search_element)


        elif search_type == 4:
            log_message("Searching for element using Red-Black Search...")
            red_black(search_array, search_element)

        # Compare with other algorithms selected
        if linear_search_var.get() == 1:
            log_message("\nComparing with Linear Search Algorithm...")
            linear_search(search_array, search_element)

        if binary_search_sort_var.get() == 1:
            log_message("\nComparing with Binary Search Sort...")
            binary_search_sort(search_array, search_element)

        if binary_search_tree_var.get() == 1:
            log_message("\nComparing with Binary Search Tree...")
            binary_search_tree(search_array, search_element)

        if red_black_var.get() == 1:
            log_message("\nComparing with Red-Black Search...")
            red_black(search_array, search_element)

    else:
        tk.messagebox.showerror("Error", "Input size does not match array size.")
        return

# Compare alogorithm UI

compare_val = tk.StringVar()
compare_label = Label(gui, text="Compare selected algorithm with").place(x=40, y = 310)



linear_search_var = IntVar()
binary_search_sort_var = IntVar()
binary_search_tree_var = IntVar()
red_black_var = IntVar()


linear_search_comp = Checkbutton(gui, text = "Linear Search", variable = linear_search_var, onvalue = 1, offvalue = 0)
binary_search_sort_comp = Checkbutton(gui, text = "Binary Search in sorted", variable = binary_search_sort_var, onvalue = 1, offvalue = 0)
binary_search_tree_comp = Checkbutton(gui, text = "Binary Search Tree", variable = binary_search_tree_var, onvalue = 1, offvalue = 0)
red_black_comp = Checkbutton(gui, text = "Red-Black Tree", variable = red_black_var, onvalue = 1, offvalue = 0)

linear_search_comp.place(x = 40, y = 330)
binary_search_sort_comp.place(x = 220, y = 330)
binary_search_tree_comp.place(x = 40, y = 350)
red_black_comp.place(x = 220, y = 350)

linear_search_comp.configure(state=DISABLED)


button = tk.Button(gui, text ="Search Element", command = searchElement).place(x = 40,y = 390)

process_log = Text(gui, height = 15, width = 75)
process_log.place(x = 40, y = 420)

log_message("Process Log")

gui.mainloop()
