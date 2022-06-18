print("calceulator daily sell progit and cost for two person!!!")
print('''
 .                                                            ,
  |`.                                                        ,'|
  \_`-._                                                  _,-'_/
 ./ \-._`-._                                          _,-'_,-/ \,
 \._/._ `._>`-.__                                __,-'<_,' _,\_,/
 /_ \_.`-._\_-._ `--__                      __--' _,-_/_,-',_/ _\
  /._`\_./ _`_./`.-._ `-.                ,-' _,-,'\,_'_ \,_/'_,\
   \._`/ _/ _`_./  _/`\_ `.            ,' _/'\_  \,_'_ \_ \'_,/
    /._`/ _/ _`_./` _/ `\_ `\_      _/' _/' \_ '\,_'_ \_ \'_,\
     \._`/ _/ _`_./` __/  >.  `-.,-'  ,<  \__ '\,_'_ \_ \'_,/
       /_`/._/._`_./` __.`.-\_.-`'-._/-,',__ '\,_'_,\_,\'_\
             `\._`_./`\._/_/'    _   `\_\_,/'\,_'_,/'
                                /_\
                                \./
                              __/(__
                             / `--' \
                            / _    _ \
                            \'|    |`/
                             \|____|/
                             \/ -] \/
                             /   |  \
                             |   |  |
                             |   |   \
                            /    |    \
                            \__,-`\___/
                            (_)     |__)             mic
''')
message="megdar daryafti x ra vard konid  ? "
daryaftix=float(input(message))
message="megdar daryafti y ra vard konid  ? "
daryaftiy=float(input(message))
message="megdar hazineh x  ra vard konid ? "
hazinehx=float(input(message))
message="megdar hazineh y  ra vard konid ? "
hazinehy=float(input(message))
message="megdar dastmozd ra as moshtari vard konid ? "
dastmozd=float(input(message))
#50 50 divion
hazineh=hazinehx+hazinehy
daryafti=daryaftix+daryaftiy
megdar_daryafti_kol=hazineh+dastmozd-daryafti
megdar_daryafti_kol_x=daryaftix-hazinehx
megdar_daryafti_kol_y=daryaftiy-hazinehy
message=f"megdar kol daryafti shoma as moshtari  brabar ast ba = {megdar_daryafti_kol} "
print(message)
print(f"x= {megdar_daryafti_kol_x} and y= {megdar_daryafti_kol_y}")
if megdar_daryafti_kol_x>megdar_daryafti_kol_y:
   a= (megdar_daryafti_kol_x+megdar_daryafti_kol_y)/2
   bazpardakht_be_y=megdar_daryafti_kol_x-a
   message=f"shakhseh x bayed {bazpardakht_be_y} be shakseh y bedahad"
   print(message)
else:
   a= (megdar_daryafti_kol_x+megdar_daryafti_kol_y)/2
   bazpardakht_be_x=megdar_daryafti_kol_y-a
   message=f"shakhseh y bayed {bazpardakht_be_x} be shakseh x bedahad"
   print(message)
        

