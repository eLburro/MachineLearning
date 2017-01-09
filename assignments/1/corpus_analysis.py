import matplotlib.pyplot as plt
import numpy as np

filename = "movie_lens.csv"

# 1. How many ratings and users are there in the corpus?
print("1.")

count = 0
users = {}
for line in open(filename, "r", encoding="utf-8"):
    line = line.strip()
    cols = line.split('|')
    users[cols[0]] = 1

    count += 1

print("Number of ratings: {0}\n"
      "Number of users: {1}".format(count, len(users)))


# 2. How many movie are there in the corpus? When has the most recent movie been released?
print("\n\n2.")

lastYear = 0
movies = {}
for line in open(filename, "r", encoding="utf-8"):
    line = line.strip()
    cols = line.split("|")
    movie = cols[1].strip()

    if movie[-5:-1].isdigit():
        year = int(float(movie[-5:-1]))

        if lastYear < year:
            lastYear = year

    movies[movie] = 1

print("Number of movies: {0}\n"
      "Last movie release: {1}".format(len(movies), lastYear))


# 3. & 4. Represent the distribution of ratings &
# Describe the number of ratings per user by computing the mean and
# standard deviation of the number of ratings per user.
# What is the largest and smallest number of ratings for one user?
print("\n\n3. & 4.")

ratings = []
smallest = 10
biggest = 0
for line in open(filename, "r", encoding="utf-8"):
    line = line.strip()
    cols = line.split("|")
    rating = int(cols[2])

    if smallest > rating: smallest = rating
    if biggest < rating: biggest = rating

    ratings.append(rating)

mean = np.mean(ratings)
deviation = np.std(ratings)

print("Ratings mean: {0}\n"
      "Ratings standard deviation: {1}\n"
      "Lagrest rating: {2}\n"
      "Smallest rating: {3}".format(mean, deviation, biggest, smallest))

plt.plot([1,2,3,4,5], [ratings.count(1), ratings.count(2), ratings.count(3), ratings.count(4), ratings.count(5)],
         color='blue',
         lw=2)

plt.title('Distribution of ratings')
plt.ylabel('user ratings')
plt.xlabel('rating [1-5]')
plt.grid(True)
plt.show()