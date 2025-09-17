from sortedcontainers import SortedList
from typing import List
import collections
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_food_rated = collections.defaultdict(lambda: SortedList())
        self.food_rated = {}
        self.food_cuisine = {}
        for food, rating, cuisine in zip(foods,ratings,cuisines):
            self.food_rated[food] = rating
            self.food_cuisine[food] = cuisine
            self.cuisine_food_rated[cuisine].add((-rating,food))
            

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = -self.food_rated[food]
        self.food_rated[food] = newRating
        self.cuisine_food_rated[self.food_cuisine[food]].remove((oldRating, food))
        self.cuisine_food_rated[self.food_cuisine[food]].add((-newRating,food))
        

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_food_rated[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)