immutable_var = 1, 2, 'Hello', 'World'
print(immutable_var)
#immutable_var[0] = 3
#print(immutable_var) #объект кортеж не поддерживает назначение элементов
mutable_list = ['стол', 'стул', 'кресло']
print(mutable_list)
mutable_list[0] = 'коридор'
mutable_list[1] = 'комната'
mutable_list[2] = 'санузел'
print(mutable_list)