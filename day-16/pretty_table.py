from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_column("Actress",
                 ["Meryl Streep", "Ingrid Bergman", "Vivien Leigh",
                  "Bette Davis", "Jodie Foster", "Katharine Hepburn",
                  "Elizabeth Taylor", "Kate Winslet", "Hilary Swank",
                  " Naomi Watts"])
table.add_column("age", ["June 22, 1949 in Summit, New Jersey, USA",
                         " August 29, 1915 in Stockholm, Sweden",
                         " November 5, 1913 in Darjeeling, Bengal Presidency, British India [now West Bengal, India]",
                         "April 5, 1908 in Lowell, Massachusetts, USA",
                         " November 19, 1962 in Los Angeles, California, USA",
                         "May 12, 1907 in Hartford, Connecticut, USA",
                         "February 27, 1932 in Hampstead, London, England, UK",
                         "October 5, 1975 in Reading, Berkshire, England, UK",
                         "July 30, 1974 in Lincoln, Nebraska, USA",
                         "September 28, 1968 in Shoreham, Kent, England, UK"])

table.add_column("died", ["live",
                          " August 29, 1982 (age 67) in Chelsea, London, England, UK",
                          "July 8, 1967 (age 53) in Belgravia, London, England, UK",
                          "October 6, 1989 (age 81) in Neuilly-sur-Seine, Hauts-de-Seine, France",
                          "live",
                          " June 29, 2003 (age 96) in Old Saybrook, Connecticut, USA",
                          "March 23, 2011 (age 79) in Los Angeles, California, USA",
                          "live", "live", "live"])
print(table)
