# Blackjack-python-JS



Game responsibilities
Flask
-user management


State logic

[Starting game]
A) MongoDB returns: gameInfo, playerDoc
B) build array of player objects, request game Info fields
C) Function: startHand(players Array,data, casino, deckCount)
+updates
+++gameInfo.deck
+++players.player.hand
