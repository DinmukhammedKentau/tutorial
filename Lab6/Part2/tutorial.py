numbers=[1,2,3,4,5]
newNumbers=list(map(lambda x:x*2,numbers))
print(newNumbers)
newFilteredNumbers=list(filter(lambda x:(x%2==0),numbers))
print(newFilteredNumbers)

"""map - numbers ти шакыру ушин керек"""
"""map - озине функцияны жане списокты кабылдайды
map(function,list)"""
"""LAMBDA -  деген типо функцияны шакыру дегенмен бирдей"""
#FILTER деген тура мап сиякты массив шакыратын кызмет аткарады бирак
#ол if  дегенмен журеди