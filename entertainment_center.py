"""stores details of a list of movies and displays them on a HTML website"""
import fresh_tomatoes
import media

""" 12 instances of the class Movie are created, where media.py initializes the instances
with title, storyline, poster image, youtube trailer and MPAA rating"""

beauty_and_the_beast = media.Movie("Beauty and the Beast",
                                   "A fairytale between a monstrous prince and a girl."
                                   " The Beast must meet his true love before the last"
                                   " rose petal falls or he is stuck as a beast forever",
                                   "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                                   "https://www.youtube.com/watch?v=OvW_L8sTu5E",
                                   "Rating: PG")

the_devil_wears_prada = media.Movie("The Devil Wears Prada",
                                    "A recent college graduate scores an assistant job in"
                                    " a high end firm. Upon landing the job at the prestigious"
                                    " Runway magazine, Andy questions her ability to survive",
                                    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                    "https://www.youtube.com/watch?v=XTDSwAxlNhc",
                                    "Rating: PG-13")

hacksaw_ridge = media.Movie("Hacksaw Ridge",
                            "Based on the true story of Pfc. Desmond. T Doss, a man goes to"
                            " war without a weapon by refusing to bear arms during WWII on "
                            " religious grounds",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
                            "https://www.youtube.com/watch?v=tEjh7-thFok",
                            "Rating: R")

troy = media.Movie("Troy",
                   "An epic battle between the ancient kingdoms of Troy and Sparta, in a"
                   " land kept by the Gods. Achillies leads his Myrmidons along with the"
                   " rest of the Greek army", 
                   "https://s-media-cache-ak0.pinimg.com/236x/9b/86/4e/9b864ed83234c02623f3ec0b6c0ad57c.jpg",
                   "https://www.youtube.com/watch?v=znTLzRJimeY",
                   "Rating: R")

crazy_stupid_love = media.Movie("Crazy Stupid Love",
                                "Cal hits the dating scene after his wife is unfaithful"
                                " with the help of Jacob Palmer, a player who takes him under"
                                " his wing and teaches Cal his ways",
                                "https://s-media-cache-ak0.pinimg.com/736x/1f/e9/93/1fe9935848cb1b51cb25cf2cc89bcfc5.jpg",
                                "https://www.youtube.com/watch?v=EnXeKRRHLE0",
                                "Rating: PG-13")

underworld_blood_wars = media.Movie ("Underworld: Blood Wars",
                                    "In the 5th installment of Underworld, Death Dealer"
                                    " Selene embarks on a Quest with allies to try end"
                                    " the eternal war between Vampires and Lycans",
                                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI5Njk0NTIyNV5BMl5BanBnXkFtZTgwNjU4MjY5MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                     "https://www.youtube.com/watch?v=r6FxROAHJH4",
                                     "Rating: R")

furious_7 = media.Movie ("Furious 7",
                         "After defeating international terrorist Owen Shaw, the Furious"
                         " crew are targets of revenge by Shaw's brother. A government agent"
                         " offers to help in an exchange",
                         "http://www.ohhaitrebor.com/wp-content/uploads/2015/07/62-Furious-7.jpg",
                         "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                         "Rating: PG-13")

easy_a = media.Movie ("Easy A",
                      "Pressured by her popular best friend to spill details of her boring"
                      " weekend, Olive, an innocent teen, decides to lie about losing her virginity",
                      "https://natashastander.files.wordpress.com/2014/03/easy-a-official-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=sE-hZ8OQzAU",
                      "Rating: PG-13")

the_big_short = media.Movie ("The Big Short",
                             "In 2008, Wall Street guru Michael Burry realizes that a number "
                             " of subprmie home loans are in danger of defaulting",
                             "http://www.breckcreate.org/wp-content/uploads/2016/01/Film-The-Big-Short-Poster.jpg",
                             "https://www.youtube.com/watch?v=LWr8hbUkG9s",
                             "Rating: R")
                                     
lord_of_the_rings = media.Movie ("Lord of the Rings",
                                 "The Fellowship of the Ring is formed to take the One Ring into Mordor to destroy it",
                                 "https://i.jeded.com/i/the-lord-of-the-rings-the-fellowship-of-the-ring.18694.jpg",
                                 "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                 "Rating: PG-13")

the_martian = media.Movie ("The Martian",
                           "When astronauts blast off from Mars, they leave behind Mark Watney, "
                           " who must find a way to survive",
                           "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                           "https://www.youtube.com/watch?v=ej3ioOneTy8",
                           "Rating: PG-13")

iron_man = media.Movie ("Iron Man",
                        "A billionaire industrialist and inventor Tony Stark is conducting "
                        " weapons tests overseas when terrorists kidnap him to make them a devastating weapon",
                        "http://3.bp.blogspot.com/_3N0VetpYvQE/S-LK4UlN7yI/AAAAAAAADIc/6Hpr7LccXJk/s1600/Iron_Man_6.jpg",
                        "https://www.youtube.com/watch?v=6_KN6Y4nI8w",
                        "Rating: PG-13")

# the abovelisted movies are now included within a list [ ]
movies = [beauty_and_the_beast, the_devil_wears_prada, hacksaw_ridge, troy, crazy_stupid_love, underworld_blood_wars, furious_7, easy_a, the_big_short, lord_of_the_rings, the_martian, iron_man]
# opens the movie website in a new window, detailing the information above
fresh_tomatoes.open_movies_page(movies)




