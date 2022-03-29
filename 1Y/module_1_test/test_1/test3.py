import pandas as pd
from IPython.display import display

football = pd.read_csv('data_sf.csv')

# display(football[football.Age > 20])
# display(football[football.Age > football.Age.mean()])
# display(football[(football.Age < football.Age.mean())|
#         (football.Club == 'FC Barcelona')])
# display(football[(football.Age < football.Age.mean())&
#         (football.Club == 'FC Barcelona')].Wage.mean())
# display(round(football[(football.Wage > football.Wage.mean())].SprintSpeed.mean(), 2))
# display(round(football[(football.Wage < football.Wage.mean())].SprintSpeed.mean(), 2))
# display(football[(football.Wage == football.Wage.max())].Position)
# display(football[(football.Nationality == 'Brazil')].Penalties.sum())
# display(round(football[(football.HeadingAccuracy > 50)].Age.mean(), 2))
# display(football[(football.Composure > football.Composure.max() * 0.9) 
#     & (football.Reactions > football.Reactions.max() * 0.9)].Age.min())
# display(round(football[football.Age == football.Age.max()].Reactions.mean()
#     - football[football.Age == football.Age.min()].Reactions.mean(), 2))    

# display(football[football.Value > football.Value.mean()].Nationality.describe())
# gk1 = football[football[football.Position == 'GK'].GKReflexes == football[football.Position == 'GK'].GKReflexes.max()]
gks = football[football.Position == 'GK']
display( gks )    
gk1 = gks[gks.GKReflexes == gks.GKReflexes.max()]
display( gk1 )    
gk2 = gks[gks.GKHandling == gks.GKHandling.max()]
display( gk2 )    
display(round(gk1.Wage.mean() / gk2.Wage.mean(), 2))
ags_max = football[football.Aggression == football.Aggression.max()]
ags_min = football[football.Aggression == football.Aggression.min()]
display(round(ags_max.ShotPower.mean() /  ags_min.ShotPower.mean(), 2))
