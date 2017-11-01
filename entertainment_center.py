import media
import fresh_tomatoes

###############################################################################
####Create object instances that contain movie title, synopsis, rating,    ####
####poster art, trailer, and duration of film                              ####
###############################################################################
hobo_with_a_shotgun = media.Movie("Hobo With A Shotgun",
                                  "Hobo cleans up crime "
                                  "in suburban hellscape.",
                                  "M",
                                  "http://media.aintitcool.com/media/legacy/images2009/hobowithashotgunposter.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=ssHEAOrAdCU",  # NOQA
                                  "2 hours")

the_room = media.Movie("The Room",
                       "I really have no idea...",
                       "R",
                       "http://media-cache-ec0.pinimg.com/736x/f2/a3/00/f2a300825312e25a030cbf1308872343.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=2NOlzW8hx5A",
                       "2 hours")

american_hippy_in_israel = media.Movie("An American Hippy in Israel",
                                       "Ex Vietnam war vet goes to Israel",
                                       "R",
                                       "http://dv7x0kxajngdw.cloudfront.net/movies/images/an-american-hippie-in-israel_110334.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=5auUkEFpsL0",  # NOQA
                                       "2 hours")

the_last_airbender = media.Movie("The Last Airbender",
                                 "M. Night Shyamalan must be stopped.",
                                 "PG13",
                                 "http://3.bp.blogspot.com/_5wXI1-YmtQs/TIK70tI4J8I/AAAAAAAAA20/amvwomZq1vA/s1600/MWC-2010-08-21-TheLastAirbender%282010%29.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=ZMoGFeMmhKA",
                                 "2 hours")
troll_2 = media.Movie("Troll 2",
                      "A movie about goblins.",
                      "R",
                      "https://s-media-cache-ak0.pinimg.com/564x/0c/29/0b/0c290bd12130a92f7e363d5273b4fcf7.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=CkNB0w1fYKk",
                      "2 hours")

garbage_pail_kids = media.Movie("The Garbage Pail Kids",
                                "A boy makes some friends",
                                "PG",
                                "http://s3.amazonaws.com/mgm-assets/assets/Title/1264715234/730/PosterFull-GARBAGEP-poster-001.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=2CqoHch6QzQ",
                                "2 hours")

movies = [hobo_with_a_shotgun, the_room, american_hippy_in_israel,
          the_last_airbender, troll_2, garbage_pail_kids]

fresh_tomatoes.open_movies_page(movies)
