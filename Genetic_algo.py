"""
This code solves Travelers Salesman Problem by using Genetic Algorithm
"""

f = open("/content/Assignment 3 berlin52.txt", "r")

lines = f.readlines()

berlin = {}

for i in lines[6:-2]:# creates graph in a dictionary from text file
  line = i.split(" ")
  berlin[line[0]] = [float(line[1]),float(line[2])]

for i in berlin:
  print(i,berlin[i])

k = berlin.keys()

cit = []

for i in k:
  cit.append(i)

print(cit)


import random
import math

pop_size = 20



def create_individual():
  
  indiv =  random.sample(cit[1:],51)
  indiv.insert(0,"1")
  indiv.append("1")
  
  return [indiv,-1]

def fitness(ind):
  sum = 0
  for i in range(52):
    x = abs(float(berlin[ind[0][i]][0]) - float(berlin[ind[0][i+1]][0]))
    y = abs(float(berlin[ind[0][i]][1]) - float(berlin[ind[0][i+1]][1]))
    dist = math.sqrt((x*x)+(y*y))
    sum += dist
  return sum

def sorted_pop(pop):
  return sorted(pop, key=lambda x: x[1], reverse=False)
    

def create_pop():
  population = []
  for i in range(pop_size):
    indiv = create_individual()
    indiv[1] = fitness(indiv)
    population.append(indiv)
  return population


def select_par(pop):
  random.shuffle(pop)
  first_g = pop[:int(pop_size/2)]
  second_g = pop[int(pop_size/2):]
  

  first_g = sorted_pop(first_g)
  second_g = sorted_pop(second_g)

  return [first_g,second_g]

def two_rand():
  num1 = random.randint(1,51)
  num2 = random.randint(1,51)
  while num1 == num2:
    num2 = random.randint(1,51)

  if num1 > num2:
    return num2,num1
  else:
    return num1,num2



def two_rand2():
  diff = 3
  num1 = random.randint(1,51-diff)
  num2 = random.randint(1,51-diff)
  while  abs(num1-num2) <= diff:
    num2 = random.randint(1,51-diff)

  if num1 > num2:
    return num2,num1
  else:
    return num1,num2

def two_rand3():
  res = []
  num1 = random.randint(1,51)
  num2 = random.randint(1,51)
  num3 = random.randint(1,51)
  while num1 == num2 or num3 == num2:
    num2 = random.randint(1,51)
  while num1 == num3 or num3 == num2:
    num3 = random.randint(1,51)

  res.append(num1)
  res.append(num2)
  res.append(num3)
  res.sort()
  return res

  
def mutation(ind):
  new_list = ind[0].copy()  
  rand1,rand2 = two_rand()
  temp = new_list[rand1]

  new_list[rand1] = new_list[rand2]
  new_list[rand2] = temp
  new_ind = [new_list.copy(),fitness([new_list])]
  
  if ind[1]>new_ind[1]:
    return new_ind
  else:
    if random.randint(0,1000) < 10:
      return new_ind
    else:
      return ind

def mutation2(ind):

  diff = 3

  new_list = ind[0].copy()  
  rand1,rand2 = two_rand2()
  temp = new_list[rand1:rand1+diff].copy()


  for i in range(diff-1):
    new_list[rand1+i] = new_list[rand2+i]
    new_list[rand2+i] = temp[i]

  new_ind = [new_list.copy(),fitness([new_list])]

  
  
  if ind[1] > new_ind[1]:
    return new_ind
  else:
    if random.randint(0,1000) < 10:
      return new_ind
    else:
      return ind

def mutation3(ind):
  new_list = ind[0].copy()  
  rand1,rand2 = two_rand()
  temp = new_list[rand1:rand2]

  
  res_list = new_list[:rand1] + temp[::-1] + new_list[rand2:]

  new_ind = [res_list.copy(),fitness([res_list])]


  if ind[1]>new_ind[1]:
    return new_ind
  else:
    if random.randint(0,100) < 1:
      return new_ind
    else:
      return ind



def mutate(pop):
  
  new_ind = [pop[0].copy(),pop[1]]

  new_ind = mutation(new_ind)
  new_ind = mutation2(new_ind)
  new_ind = mutation3(new_ind)



  return [new_ind[0].copy(),new_ind[1]]


def crossed(ana,baba):
  cross_size=5
  idx1 = random.randint(1,51-cross_size)
  temp1 = ana[0][idx1:idx1+cross_size].copy()
  idx2 = 1
  c = 0

  gap = []

  for i in range(cross_size):
    gap.append('0')

  
  for i in baba[0][1:46]:
    if i not in temp1:
      c += 1
    else:
      idx2 += c
      c = 0
    if c == cross_size:
      break
      
  temp2 = baba[0][idx2:idx2+cross_size].copy()

  ana_rest = ana[0][:idx1]+ gap +ana[0][idx1+cross_size:]
  baba_rest = baba[0][:idx2]+ gap +baba[0][idx2+cross_size:]
  

  for i in range(len(temp1)):
    if temp1[i] in baba_rest:
      temp_idx = baba_rest.index(temp1[i])
      for k in temp2:
        if k not in temp1 and k not in baba_rest:
          rep = k
      baba_rest[temp_idx] = rep
    baba_rest[idx2+i] = temp1[i]

    if temp2[i] in ana_rest:
      temp_idx = ana_rest.index(temp2[i])
      for k in temp1:
        if k not in temp2 and k not in ana_rest:
          rep = k
      ana_rest[temp_idx] = rep
    ana_rest[idx1+i] = temp2[i]
  

  

  child1 = [ana_rest.copy(),fitness([ana_rest])]
  child2 = [baba_rest.copy(),fitness([baba_rest])]
  

 
  return [child1[0].copy(),child1[1]],[child2[0].copy(),child2[1]]




def cros_par(parents):
  total_pop = []
  par = []
  child = []
  for i in range(len(parents[1])):
    
    ana = parents[0][i].copy() 
    baba = parents[1][i].copy()


    child1, child2 = crossed(ana,baba)

    

    child1 = mutate(child1)
    child2 = mutate(child2)
   

    
    total_pop.append(ana)
    total_pop.append(baba)
    total_pop.append(child1.copy())
    total_pop.append(child2.copy())

    """par.append(ana)
    par.append(baba)
    child.append(child1.copy())
    child.append(child2.copy())"""



  total_pop = sorted_pop(total_pop)

  #par = sorted_pop(par)
  #child = sorted_pop(child)
  
  #res = total_pop[:pop_size]
  #res = par[:int(pop_size*0.9)] + child[:int(pop_size*0.1)]
  res = total_pop[:int(pop_size*0.8)]+random.sample(total_pop[int(pop_size*0.8):],int(pop_size*0.2))
  return res





def crossover(pop):

  parent_list = select_par(pop)

  crossed_pop = cros_par(parent_list)

  return crossed_pop




def opt():
  avg = 0

  population = create_pop()
  
  for i in range(1500):
    

    population = crossover(population)
    
    
    if i%100 == 0:
      print(i)
      
  for i in population:
    print(i)
    avg += i[1]
  
  print("Min:",population[0][1])

  
  return avg/pop_size
  
  
  
  
avg = 0
print("Avg:",opt())
#for i in range(10):
#  avg += opt()
#print(avg/10)

