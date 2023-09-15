from django import forms


class GameForm(forms.Form):
    GAME_CHOICES = [
        ('HeadsOrTails', 'Heads or Tails'),
        ('Dice', 'Dice'),
        ('RandomNumbers', 'Random Numbers')
    ]
    game = forms.ChoiceField(choices=GAME_CHOICES)
    attempt = forms.IntegerField(min_value=1, max_value=64)