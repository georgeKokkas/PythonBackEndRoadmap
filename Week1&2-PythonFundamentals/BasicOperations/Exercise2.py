# Create a list of your favorite movies and manipulate the list (add, remove, access elements).

movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "The Godfather Part II", "12 Angry Men", "Schindler's List"]
movies.append("The Lord of the Rings")
movies.remove("The Dark Knight")
second_movie = movies[1]

print(movies) # Ouput: ['The Shawshank Redemption', 'The Godfather', 'The Godfather Part II', '12 Angry Men', "Schindler's List", 'The Lord of the Rings']
print(second_movie) # Output: The Godfather