
try:
   file=open("data.txt" )
   a_dictionary = {"key": "value"}
   value = a_dictionary["non_exist_key"]
except FileNotFoundError:
    file=open("data.txt",mode="w")
    file.write("sample something")
except KeyError as error_m:
    print(f"key error{error_m} happen please make edit")
else:
    print(file.read())

finally:
    file.close()