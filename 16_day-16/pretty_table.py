from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_column("Actress",
                 ["Meryl Streep", "Ingrid Bergman", "Vivien Leigh",
                  "Bette Davis", "Jodie Foster", "Katharine Hepburn",
                  "Elizabeth Taylor", "Kate Winslet", "Hilary Swank",
                  " Naomi Watts"])
table.add_column("age", ["22, 1949, USA",
                         " August 29, 1915,Sweden",
                         " November 5, 1913 ,British India",
                         "April 5, 1908 , USA",
                         " November 19, 1962, USA",
                         "May 12, 1907 , USA",
                         "February 27, 1932 , UK",
                         "October 5, 1975 , UK",
                         "July 30, 1974 , USA",
                         "September 28, 1968 , UK"])
table.add_column("died", ["live",
                          " August 29, 1982 (age 67), UK",
                          "July 8, 1967 (age 53) , UK",
                          "October 6, 1989 (age 81), France",
                          "live",
                          " June 29, 2003 (age 96) , USA",
                          "March 23, 2011 (age 79) , USA",
                          "live", "live", "live"])
print(table.align) #c center r right l left
table.align='r'
print(table)
