frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split()) # Imprime uma lista de strings separados> ['Olá,', 'bem', 'vindo', 'a', 'este', 'treinamento!']

print(frase.split(',')) # Separando por virgula ['Olá', ' bem vindo a este treinamento!']

print(frase.split('-')) # vai separar por traço ['Olá, bem', 'vindo a este treinamento!']

nomes = 'david, aline, arthur, dani, rodrigo, miguel, leticia'
print(nomes.split(','))
# resposta: ['david', ' aline', ' arthur', ' dani', ' rodrigo', ' miguel', ' leticia']

print(nomes.split(',', 3)) # Aqui serve para separar os três primeiros do resto>
# ['david', ' aline', ' arthur', ' dani, rodrigo, miguel, leticia']

#JUNTANDO
print(','.join(nomes))
# d,a,v,i,d,,, ,a,l,i,n,e,,, ,a,r,t,h,u,r,,, ,d,a,n,i,,, ,r,o,d,r,i,g,o,,, ,m,i,g,u,e,l,,, ,l,e,t,i,c,i,a
print('-'.join(nomes))
# d-a-v-i-d-,- -a-l-i-n-e-,- -a-r-t-h-u-r-,- -d-a-n-i-,- -r-o-d-r-i-g-o-,- -m-i-g-u-e-l-,- -l-e-t-i-c-i-a
print(' '.join(nomes))
#d a v i d ,   a l i n e ,   a r t h u r ,   d a n i ,   r o d r i g o ,   m i g u e l ,   l e t i c i a


