#Enter Python code here and hit the Run button.
# step bet winnings calculator

# user input # of players, $bet, eligible players, $pot
# program prints winnings

players = int(input("How many players are left? "))
pot = int(input("How much is in the pot? "))

total_players = pot/40
print("pot / $40")
print("= total players: ", total_players)

drop_outs = total_players - players
print("total players - palyers")
print("= drop outs: ", drop_outs)

gross_winnings = (drop_outs * 40)
print("drops outs × $40")
print("= gross winnings: $", gross_winnings)

fees = gross_winnings * 0.15
print("15% of gross winnings")
print("= fees: $", fees)

winnings = gross_winnings - fees
print("gross winnings - fees / players")
print("= winnings: $", winnings)

my_winnings = winnings / players
print("winnings / players")
print("= my winnings: $", my_winnings)


my_payout = my_winnings + 40
print("my winnings + $40")
print("= my payout: $", my_payout)

#total_players = 331
#eligable_players = 331
#drop_outs = 0
#bet = 40
#while #total_players > 0:
# lost_bets = total_players - eligable_players
# winnings = lost_bets * bet
# winnings_per_player = winnings / eligable_players
# my_winnings = winnings_per_player + bet
 # print("# of players", eligable_players)
 # print("winnings: $", my_winnings)
# print("drop outs:", drop_outs)
# eligable_players -= 1
# drop_outs += 1
print()
