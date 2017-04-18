MOVIE WEBSITE
=============

<b>Author</b>: Natalie Butler

<b>Python Version</b>: Python 2.7.11

<b>Project</b>: python files generating a Movie Trailer html website


About
=====
This program provides a list of Natalie's favourite movies, where users can click on each movie image to view its individual trailer.

The python files enlists code that stores an array of data, including a list of movies, box art, imagery and movie trailer URL, allowing users to view the list of movies and watch trailers.

This readme file explains for viewers how the website is created with the interaction of 3 files called fresh_tomatoes.py, media.py and entertainment.py. 
The fresh_tomatoes.py file has been reconfigured to include both movie storyline and MPAA rating information. 


CONCEPT TO IMPLEMENTATION
=======================
The following project guidelines were provided:
1.	Create a data structure to store your favourite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer
2.	Create multiple instances of that Python Class to represent your favourite movies
3.	Generate a website that displays these movies, with the assistance of a Python module called fresh_tomatoes.py, which contains the function open_movies_page that displays the relevant information in a HTML file
 
Class Structure
===============

In order to build this website, a Class was created in media.py called Movie. A class in Python gives the ability to structure code in a clean and particular way. The following instance variables of the class Movie were created:
1.	title
2.	storyline
3.	poster image
4.	movie trailer
5.	rating

The screenshot below shows the class Movie and the instance variables in the file media.py:

![screen shot media py file](https://cloud.githubusercontent.com/assets/25575132/25083082/4517c070-2398-11e7-99cd-306c273e946a.png) 

Instance structure
==================
In entertainment_center.py, instances of the class Movie were created to include:
1.	Beauty and the Beast
2.	The Devil Wears Prada
3.	Hacksaw Ridge
4.	Troy
5.	Crazy Stupid Love
6.	Underworld: Blood Wars
7.	Furious 7
8.	Easy A
9.  The Big Short
10.	Lord of the Rings
11.	The Martian
12.	Iron Man

The screenshot below details some of the information in entertainment_center.py that gets passed into class Movie() when the entertainment_center.py is run through run module. Continue reading for further explanation:

![screen shot entertainment_center py code](https://cloud.githubusercontent.com/assets/25575132/25083154/c9e3b6ce-2398-11e7-81c4-8af0c2af450e.png)

HOW THE PROGRAM WORKS
=====================
This program works by the creation of a class called Movie in movie.py. __init__ is a constructor of that class, meaning it assigns values to instance variables that follow within that class. Instance variables in this code are title, storyline, poster_image_url, youtube_url and rating, which were listed above in Class Structure and seen in the screenshot. Meanwhile, self is a python keyword, which is known as the object being created. Whilst self is a convention and has no special meaning to Python, by not following this convention may be less readable to other programmers.

As you can see at the top of media.py, a pre-defined Python function called webbrowser is imported, whilst there are two (2) imports in entertainment_center.py, including fresh_tomatoes and import media.

Using ‘import media’ within entertainment.center.py links the two files together and the __init__ function gets called. To use beauty_and_the_beast as an example, the code uses self as the instance being created, which in this case is beauty_and_the_beast, and several pieces of information are assigned:

title = Beauty and the Beast

storyline = “A fairytale between a monstrous prince and a girl. The Beast must meet his true love before the last rose petal falls or he is stuck as a beast forever

poster_image = https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg

youtube_trailer = https://www.youtube.com/watch?v=OvW_L8sTu5E

rating = Rating: PG


As per Python documentation, the webbrowser module provides a high-level interface to permit displaying web-based documents to users, and can accept a URL as its argument. Within the code, the function show_trailer opens a youtube trailer by:
webbrowser.open(self.trailer_youtube_url), where,

- webbrowser is a pre-defined Python function

- .open() is similarly a pre-defined Python function that opens a webpage

- self is the object that is being passed through, whether it is beauty_and_the_beast or easy_a

- .trailer_youtube_url is each youtube_url that is initialized in the class Movie()


SETUP
=====

 1. Install Python. If you already have Python installed, go to 
    Step 2. Click on the following link to install Python:
    
    https://www.python.org/downloads/release/python-2711/
    
    Ensure you download correctly as per your computer requirements, ie: Mac OS X or Windows
 
 2. Download fresh_tomatoes.py
 
    Fresh tomatoes will allow the code to be uploaded to the internet browser
    
    
 3.  Download both media.py and entertainment_center.py

     Ensure all three of these files, including fresh_tomatoes.py are placed in the same file location
    


RUNNING THE PROGRAM
=======================

1.	Once you have completed set up, use the entertainment_center.py file to run the program. This is done in IDLE by clicking Run in the menu bar, followed by Run Module
2.	This will generate the HTML movie website via fresh_tomatoes.html, which is created when using the fresh_tomatoes.py file

Additional credit description
=============================

The following changes were made in order to gain additional recognition from Udacity. In relation to styling:
-	the header was changed from ‘Fresh Tomatoes Movie Trailers’ to ‘Natalie’s Favourite Movies’
-	a number of google fonts were included, such as Raleway for movie text, Righteous for the heading and Delius Swash Caps for the movie titles
-	an image was included in the header to provide a more appealing site (via background-image: url( .. ) )
-	a small movie icon was included on the website tab via a < link rel="icon" href= ".."> where .. is jpg link
-	changed the body of the website to include a black background color and white font 
-	the color of the h2 (movie titles) was altered to a light grey
-	the width of the header was changed to make it larger via .container {
-	the heading (Natalie’s favourite movies) is displayed in uppercase via text-transform, the font color changed to a shadow of green and a text shadow has been used to make this stand out infront of the header image
-	a ‘cell’ cursor appears when hovering over movie posters instead of the pre-selected pointer
-	when hovering over a poster image, the color was similarly changed to black from white so this is not highlighted and thus is more appealing
-	in addition to hovering, the main heading was changing color when a user hovered over this. This was altered to be the same color as the heading so no differentiation is made

In regard to functionality:
-	both movie_title_content and create_movie_titles_content(movies) were altered within fresh_tomatoes.py to allow the website to display a storyline and the MPAA rating
