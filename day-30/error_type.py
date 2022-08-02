########## File Not Found

# with open("daata.tx") as file:
#     file.read()
# expect FileNotFoundError: [Errno 2] No such file or directory: 'daata.tx'

###########KeyError
a_dictionary = {"key": "value"}
# value=a_dictionary["non_exist_key"]
#KeyError: 'non_exist_key'
a_dictionary|={"name":"emilia"}
# dest = dict(list(orig.items()) + list(extra.items()))✅✅

##########index_error
list=[1,2,3,4]
# list[4]

###########Type_Error
text="abx"
print(text+5)