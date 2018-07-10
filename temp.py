from connection import connection

c,conn=connection()
x=c.execute("UPDATE  user SET emailconfirm=TRUE WHERE email_verification_link='dfdfgdf' AND emailconfirm=0")
print(type(x))
y=c.execute("UPDATE  user SET emailconfirm=TRUE WHERE email_verification_link='127.0.0.1:5000/verify/$5$rounds=535000$N5VmA17h5lJvYzwZ$vEgI2obJzjGl2hT7wPDC18oNsKblpzL7iViev/EH718$5$rounds=535000$a8S85CL76dBDfchD$cULFk28ImElZuKn7gNkKygGHfEqsg6KcuCcmEw6TQY/' AND emailconfirm=0")
print(y)

#
# data_list = []
#
#
#
# def get_date():
#     c,conn = connection()
#     age =18
#     print (type(age))
#     c.execute("select * from user where uid=(%s)",[age])
#     global data_list
#     data_list = c.fetchone()
#     print(data_list)
#     c.close()
#
#
# get_date()
#
#
# dat = {'a': 1, 'b': ('ball')}
#
# dat['a'] = ['2','3']
#
# c, conn =connection()
#
# c.execute("select * from ((user inner join userdetails on userdetails.userdetilsid = user.user_details) inner join address on address.Addressid=user.user_address) where username = 'Cha14ran'")
#
#
# print(c.fetchall())

# def a():
#     class g:
#         pass
#     return g
# def b():
#     t=a()
#     f = t()
#
# b()

#
# a = {'username': "sriteja", "logged_in": "True", "temp":''}
#
# print(a)
#
# # a.clear()
# a['username'] = ''
# a['logged_in'] = ''
# a['temp'] = ''
#
# print(a)

# a = ''
# if a:
#     print ('yes')
# else: print('no')


# a={}
# a['user']='name'
# print(a)