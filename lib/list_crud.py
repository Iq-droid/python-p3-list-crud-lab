#creating an empty list
def create_an_empty_list():
    return []

#creating a list with elements
def create_a_list():
    return [88, "Omar", .32, 1/3]

#adding an element to end 
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

#adding an element to start of the list
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

#removing last item
def remove_element_from_end_of_list(l):
    l.pop()
    return l

#removing first element
def remove_element_from_start_of_list(l):
    del l[0]
    return l

#retrieving value of first element
def retrieve_first_element_from_list(l):
    return l[0]

#retrieving an element of a given index
def retrieve_element_from_index(l, index):
    return l[index]

#retrieving last element from list
def retrieve_last_element_from_list(l):
    return l[-1]
