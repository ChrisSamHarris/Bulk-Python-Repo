import requests
import xlsxwriter
from bs4 import BeautifulSoup
 
# Download/Access the IMDb Page
response = requests.get(url="https://www.imdb.com/chart/top/?ref_=nv_mv_250")
imdb_page = response.text
 
# Soup the IMDb Page
soup = BeautifulSoup(imdb_page, 'html.parser')
 
# Get the list of all anchor tags and rating tags
all_a_list = soup.select("td.titleColumn a")
all_rating_list = soup.select("td.imdbRating strong")
 
# Create empty list for movie name and rating
movie_name_list = []
movie_rating_list = []
 
# Append the name of each movie to the movie_name_list
for a in all_a_list:
    movie_name_list.append(a.text)
 
# Append the rating of each movie to the movie_rating_list
for rating in all_rating_list:
    movie_rating_list.append(rating.text)
 
# Create an empty workbook and an empty worksheet
workbook = xlsxwriter.Workbook("Top 250 Movies of All Time.xlsx")
worksheet = workbook.add_worksheet()
 
# Initialize the rows and columns
row = 1
columnA = 0
columnB = 1
columnC = 2
 
# Name the headings of the columns
worksheet.write("A1", "Rank")
worksheet.write("B1", "Movie Name")
worksheet.write("C1", "IMDb Rating")
 
# Run a for loop to append the rank, movie, and rating to a new row everytime the loops runs
for x in range(len(movie_name_list)):
    worksheet.write(row, columnA, x + 1)
    worksheet.write(row, columnB, movie_name_list[x])
    worksheet.write(row, columnC, movie_rating_list[x])
    row += 1
 
# Close the workbook
workbook.close()