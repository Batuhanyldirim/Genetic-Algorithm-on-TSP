# Genetic-Algorithm-on-TSP


### Important Operations of the Algorithm

Genetic algorithm mimics the natural process of evolution. In order to represent it, code uses a population and tries to find solution over generations by using natural biologic phenomena such as;

*  **Creation of the Population**
> A population createdrandomlyin order to calculate different possible solutions in one generation

*  **Fitness function**
> Fitness function has an essential important for the algorithm since it defines if an individual is successful or not.Fitness is calculated according to distance traveled by individual

*  **Parent Selection**
> Parent selection also is important since we want some sort of randomness and also we want to get best individuals offspring’s. In this algorithm population shuffled and divided in twoparts. This two parts sorted according to fitness and best, second best, third best paired respectively trough the last individuals.

*  **Crossover**
> Crossover operation copies parents and changes random parts of them and avoids duplications in new individuals. This allows new generations to exchange good and bad sides and when it is time to select new population, good exchanged individuals will survive in the next generation so algorithm will mimic natural selection.

*  **Mutation**
> Mutation operation has 3 different mutation and it is applied to try random solutions over individuals to not stuck in a certain point. First mutation randomly swamps position of two cities in an individual. Mutation 2 swamps two 3 length parts of an individual randomly without any confliction. Mutation 3 reverses a random portion of the individual. All mutations checks if the new individual is better after mutation and saves mutation if it is better. If it is not better it saves the individual with %1 chance.

*  **New population selection**
> There are 3 different selection types for new generations. Actively used selection operation is it selects best of 0.8 of population from both parents and children. The rest 0.2 portion is randomly selected from remaining population.




### Representation of an Individual

An individual represented by a 2d integer vector. Visual representation of the vector is;

![image](https://user-images.githubusercontent.com/41572446/121980668-a4dd1580-cd8c-11eb-850d-1fc105f5743b.png)


First layer of the vector contains city codes and the order corresponds the route. For example, in this case the tour is starts from city C1and continuous with city C2and C3and goes on like that. This is the representation of the route. There are 53 cities in the first layer because the individual need to turn backthe same city where it started. Also because of the problem definition C1always equals to 1 but C2does not have to equal to 2.The second layer of the vector is stores the fitness value of the given individual. This fitness shows the total length of the route. In this example, the route length is Fiunit.So, there is an example solution for the problem with 8321.8029 units fitness value.

![image](https://user-images.githubusercontent.com/41572446/121980715-bde5c680-cd8c-11eb-9ee9-de1b044ea73c.png)



### Fitness Function

The fitness of an individual is calculated as the total distance of the rout. An individual has 53 cities in first layer of individual vector. We are calculating and summing the distance between iterative cities in the vector. 

![image](https://user-images.githubusercontent.com/41572446/121980794-e1a90c80-cd8c-11eb-83bb-cdde0dd93388.png)

This is the fitness function which 𝐶𝑖,𝑥corresponds to the ithcity’s x coordinate on the vector and 𝐶𝑖,𝑦corresponds to the ithcity’s y coordinate on the vector. So we can sum all the routes distance and we have one extra calculation to find turn back to starting point.




### Parameters Used in the Algorithm
Parameters in the algorithm are;

*  **Population size**
> Adjusts the population size and it is 20 in defended code.

*  **Iteration number**
> Adjusts how many generations we will go through and it is 1500 in defended code

*  **Difference in mutation 2**
> This adjusts the length of the portion that will swamped in an individual. It is 1 in defended code

*  **Crossover rate**
> Crossover rate is not linked with a direct parameter but directly stated as 1 so every individual has a crossover.

*  **Mutation rate**
> Also mutation rate is not linked with a direct parameter but stated as 1 so every individual facesmutation but it does not saved with %99 chance if new individual does not has a better fitness.


### Performance of the population over generations
This is the graph of populations average performance over generations;

![image](https://user-images.githubusercontent.com/41572446/121981187-7f044080-cd8d-11eb-8da4-2ca916158677.png)


This is the graph of populations best individual’s performance over generations;

![image](https://user-images.githubusercontent.com/41572446/121981147-71e75180-cd8d-11eb-98b7-5d32dc8afa9e.png)




