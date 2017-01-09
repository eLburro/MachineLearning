import numpy as np

def calculate_distances(directory):
    #correlations =
    #np.corrcoef(a1,a2)
    return 1

max_users = 943+1 # from corpus_analysis and adding one for out of bounds prevention
filename = "movie_lens.csv"

movies = {}
for line in open(filename, "r", encoding="utf-8"):
    line = line.strip()
    cols = line.split('|')
    user = int(cols[0])
    movieName = cols[1]
    rating = int(cols[2])

    # create the movie vectors with all ratings
    if movieName in movies:
        movies[movieName][user] = rating
    else:
        movies[movieName] = np.zeros((max_users,), dtype=np.int)

calculate_distances(movies)


# 5. Why can correlation be used as a similarity measure?

# 6. Write a function computing the similarity between all the movies of the corpus.

# 7. What is the complexity of computing the similarity between all the movies of the corpus?

# 8. What are the five movies the most similar to Scream (1996) and Stargate (1994)?

# 9. How can the quality of the developed system be evaluated?





