# CocktailBuilder
A fun little textgenrnn-based neural network I built to generate novel cocktail recipes. NOTE: As of 2021 textgenrnn won't work well without some finagling due to a Keras update. If you want to reproduce this, I recommend downloading the Colab notebook linked on the textgenrnn Github. 

In December 2020, I had my first Aviation cocktail, and fell in love. So I bought a bottle of Creme de Violette to make my own pretty purple cocktails at home. I'm no mixologist, so I decided to build a text generator to concoct recipes for me. 

I used the very novice-friendly textgenrnn (https://github.com/minimaxir/textgenrnn), which is itself based on Andrej Karpathy's char-rnn (http://karpathy.github.io/2015/05/21/rnn-effectiveness/). This module lets you train at the word level as well as character level; it also allows you to train bidirectionally (going both directions through the text).

I trained my generator on a custom database with over 200 Creme de Violette cocktail recipes from across the web. The database was standardized, as I wanted to play with ingredient combinations and their proportions. Database format: <i>Name - muddle - hard liquor - liqueur - acid - syrup - garnish or topper</i>. This is considered a tiny training set, FYI. But it worked for me. 

I tested my results by drinking them. My favorite was a tie between the Violet Crome and the Silver Win Moon.

<img src="https://github.com/meg256/CocktailBuilder/violet_crome.jpg" width="100">

Best results were generated using 30 epochs and temperature between 1.0-1.2. A selection of results:

<i>

Bearney Prigar - 1.5 oz gin - 0.5 oz green chartreuse - 0.5 oz creme de violette - 0.5 oz lemon juice - garnish with curacao - garnish with orange zest wedge

Dolin Manten - 2 oz gin - 0.75 oz ginger liqueur - 0.33 oz creme de violette - 0.25 oz lime juice - 0.25 oz lemon juice

Royal Drefel - 0.75 oz gin - 0.75 oz dry vermouth - 0.25 oz creme de violette - 0.25 oz lime juice - 1 egg white - top with mint

Violet Crome - muddled mint - 2 oz light rum - 0.5 oz creme de violette - 0.5 oz lemon juice - 0.5 oz honey syrup - garnish with rosemary

Sodo Violets - 2 oz scotch - 0.75 oz gin - 0.25 oz maraschino liqueur - 0.5 oz lemon juice - 0.25 oz creme de violette - garnish with lemon twist

Silver Win Moon - 1.5 oz gin - 0.25 oz creme de violette - 1 oz lemon juice - 0.5 oz honey syrup - 1 egg white

No Man-Landed Trail - 1.5 oz gin - 0.5 oz maraschino liqueur - 0.75 oz elderflower liqueur - 0.5 oz creme de violette - top with tonic - garnish with blackberries

Purple Steady - 2 oz sloe gin - 0.05 oz creme de violette - 0.75 oz lemon juice - 0.66 egg white - 0.5 oz orange juice - 0.75 oz simple syrup - 0.15 oz creme de violette

Sloe and Stardust - 2 oz gin - 0.5 oz orgeat - 0.25 oz creme de violette - 0.75 oz lemon juice - 1 dash bitters

Myrrah's Ghost - 2 oz gin - 0.33 oz light rum - 0.25 oz creme de violette - 0.75 oz lemon juice - 0.25 oz simple syrup - 0.12 oz lime juice

Nim rose and Violets - 2 oz scotch - 0.33 oz creme de violette - 1 oz lemon juice - 0.75 oz simple syrup - garnish with mint

Blueberry whiskey cocktail - muddled blueberries - 2 oz scotch - 0.5 oz orgeat - 0.1 oz creme de violette - 0.25 oz maraschino liqueur - 2 dash orange bitters

Rainy Night - muddled basil - muddled mint - muddled orange wedge - 2 oz gin - 0.75 oz campari - 0.25 oz creme de violette

</i>
