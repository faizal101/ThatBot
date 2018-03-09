from random import choice

eightBallStrings = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
                    'As I see it, yes', 'Most likely', 'Outlook good', 'Yep', 'Signs point to yes',
                    'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                    'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no',
                    'Outlook not so good', 'Very doubtful']


fightStrings = [', but instead slipped on some jam and fell right into a conveniently placed hole.',
                ' with a transformer.', ', but creates a black hole and gets sucked in.',
                ' with poutine.', ', but they slipped on a banana peel.',
                ' and in the end, the only victor was the coffin maker.',
                ', and what a fight it is! Whoa mama!', ', with two thousand blades!',
                ', but he fell into a conveniently placed manhole!',
                ', but they tripped over a rock and fell in the ocean.',
                ', but they hurt themselves in confusion.', '. HADOUKEN!', ' with a pillow.',
                ' with a large fish.', ', but they stumbled over their shoelaces.', ', but they missed.',
                ' with a burnt piece of toast.', ', but it wasn\'t every effective.',
                'and it was super effective!', ', but nothing happened.',
                ', while shouting out a move as if they\'re a main character from an anime.', ', but gave up halfway.']


def ball():
    outcome = choice(eightBallStrings)
    return outcome


def fight():
    outcome = choice(fightStrings)
    return outcome
