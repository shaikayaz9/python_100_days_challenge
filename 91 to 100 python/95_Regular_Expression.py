# regular Expression

import re
pattern = "Bangladesh"
text = '''
NZ fast bowler O'Rourke rocks SL with two early wickets in 1st Test
New Zealand fast bowler William O'Rourke rocked Sri Lanka with two early wickets as the hosts took lunch at 88 for two on the opening day of the first Test at 
Galle on Wednesday.
A tall right-arm quick, O'Rourke was on the money and troubling the Sri Lankan b…
Best style is the style that wins: Gautam Gambhir
Gautam Gambhir, as the new head coach of the Indian cricket team, focuses on adaptability and quick learning instead of a single approach. He seeks to build strong relationships with senior players while advancing Indian cricket. Despite mixed results in his …
India vs Bangladesh: Gambhir backs Indian batters to take on any spin unit
India head coach Gautam Gambhir on Wednesday expressed confidence in his batting unit's capability to negate quality spin bowling, a challenge they are expected to face in the Test series against Bangladesh.
India batters, including star batter Virat Kohli, s…
India vs Bangladesh: Important to build relationship with seniors - Gambhir
Head coach Gautam Gambhir on Wednesday underlined the significance for him to build on the existing cordial relationship with the senior players like skipper Rohit Sharma and batting talisman Virat Kohli to take Indian cricket forward.
'''

a = re.search(pattern, text)
print(a)