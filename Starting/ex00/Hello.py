#You need to modify the string of each data object to display the following greetings: 
#"Hello World", "Hello <country of your campus>", "Hello <city of your campus>", "Hello <nme iof your campus>"

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set =  {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

# list_tuple = list(ft_tuple)
# list_tuple[1] ="Armenia!"
# ft_tuple = tuple(list_tuple)

ft_tuple = (ft_tuple[0], "Armenia!")

ft_set.remove("tutu!")
ft_set.add("Yerevan!")

ft_dict["Hello"] = "42Yerevan!" 

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)