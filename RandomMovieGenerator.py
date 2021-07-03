import random
import sys

movies = {
        'Waynes World': 1,
         'Freaky Friday': 2,
         'Heavy Weights': 3,
         'A Walk to Remember': 4,
         'Confessions of a Teenage Drama Queen': 5,
         'Fight Club': 6,
         'The Princess Diary': 7,
         'Billy Madison': 8,
         'Dumb and Dumber': 9,
         'Jurassic Park': 10,
         'Clueless': 11,
         'White Chicks': 12,
         'Rat Race': 13,
         'Wedding Singer': 14,
         'Mean Girls': 15,
         'How to deal': 16,
         'Riding in Cars with Boys': 17,
         'Dodgeball': 18,
         'Big Fat Liar': 19,
         'Godzilla': 20,
         'Pitch Perfect': 21,
         'Pitch Perfect 2': 22,
         'Pitch Perfect 3': 23,
         'Jaws': 24,
         'American Pie': 25,
         '10 Things I Hate About You': 26,
         'What A Girl Wants': 27,
         'E.T.': 28,
         'Pulp Fiction': 29,
         'Mighty Joe Young': 30,
         'V for Vandetta': 31,
         'Happy Gilmore': 32,
         'Goonies': 33,
         'Sister Act': 34
}


while True:
    print('Welcome to Random Movie Generator')
    print('Output a random movie (1)')
    print('See all the movies available (2)')
    print('Quit (3)')
    command = input('Please enter a command!')
    if command == '1':
        random_movie = random.choice(list(movies))
        print('')
        print(random_movie, '\n')

    elif command == '2':
        for key in movies:
            print(key)

    elif command == '3':
        print('Bye bye!')
        sys.exit()
    else:
        if command not in ('1', '2', '3'):
            print('Please enter an input I understand!')
