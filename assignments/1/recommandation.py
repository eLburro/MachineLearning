import numpy as np

def cov(v1, v2):
    mean1 = sum(v1) / len(v1)
    mean2 = sum(v2) / len(v2)

    return sum([(e1 - mean1) * (e2 - mean2) for e1,e2 in zip(v1, v2)]) / len(v1) - 1


def corr(v1, v2):
    try:
        res = cov(v1, v2) / np.sqrt(cov(v1, v1) * cov(v2, v2))
        res = (1 + res) / 2

        return res

    except ZeroDivisionError:
        return 0.0


def simi(movie1, movie2):
    movie1_users = movies[movie1]
    movie2_users = movies[movie2]

    common_users = set(movie1_users.keys())
    common_users.update(movie2_users.keys())

    rates_vec1 = [movie1_users.get(u, 0) for u in common_users]
    rates_vec2 = [movie2_users.get(u, 0) for u in common_users]

    return corr(rates_vec1, rates_vec2)


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

#calculate_distances(movies)


# 5. Why can correlation be used as a similarity measure?

# 6. Write a function computing the similarity between all the movies of the corpus.

# 7. What is the complexity of computing the similarity between all the movies of the corpus?

# 8. What are the five movies the most similar to Scream (1996) and Stargate (1994)?

# 9. How can the quality of the developed system be evaluated?





