#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:58:22 2023

@author: hillarywolff
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#establsih wd
directory_path = '/Users/hillarywolff/documents/github/detroittigersanalytics'
os.chdir(directory_path)

current_directory = os.getcwd()
print(current_directory)

#import dataset

PATH = r'/Users/hillarywolff/documents/github/detroittigersanalytics/'
df = pd.read_csv(PATH+'AnalyticsQuestionnairePitchData.csv')



#_____________________________________________________________________________


# histogram of pitch types
plt.figure(figsize=(16, 8))  
plt.subplots_adjust(right=0.7)
pitch_counts_by_pitcher = df.groupby(['PitcherId', 'PitchType']).size().reset_index(name = 'PitchCount')
for pitcher_id in pitch_counts_by_pitcher['PitcherId'].unique():
    pitcher_data = pitch_counts_by_pitcher[pitch_counts_by_pitcher['PitcherId'] == pitcher_id]
    plt.bar(pitcher_data['PitchType'], pitcher_data['PitchCount'], label=f'Pitcher {pitcher_id}')

plt.xlabel('Pitch Type')
plt.ylabel('Pitch Count')
plt.title('Pitch Type Histogram for All Pitchers')
plt.xticks(rotation=45)
plt.legend(fontsize='small', bbox_to_anchor = (1.05, 1), loc='upper right')
plt.tight_layout()
plt.show()


# barchart of pitch calls
plt.figure(figsize=(16, 8))  
plt.subplots_adjust(right=0.7)
pitch_counts_by_pitcher = df.groupby(['PitcherId', 'PitchCall']).size().reset_index(name = 'PitchCallCount')
for pitcher_id in pitch_counts_by_pitcher['PitcherId'].unique():
    pitcher_data = pitch_counts_by_pitcher[pitch_counts_by_pitcher['PitcherId'] == pitcher_id]
    plt.bar(pitcher_data['PitchCall'], pitcher_data['PitchCallCount'], label=f'Pitcher {pitcher_id}')

plt.xlabel('Pitch Call')
plt.ylabel('Frequency')
plt.title('Frequency of Pitch Calls')
plt.xticks(rotation=90)
plt.legend(fontsize='small', bbox_to_anchor = (1.05, 1), loc='upper right')
plt.show()

#box plot of release speed between pitchers
sns.boxplot(x='PitcherId', y='ReleaseSpeed', data=df)
plt.xlabel('PitcherId')
plt.ylabel('Release Speed')
plt.title('Release Speed Distribution Between Pitchers')
plt.show()


# box plot of release speed between games
sns.boxplot(x='GamePk', y='ReleaseSpeed', data=df)
plt.xlabel('Game')
plt.ylabel('Release Speed')
plt.title('Release Speed Distribution Between Games')
plt.show()


# scatter plot of release angle vs release spin rate
x = df['ReleaseAngle']
y = df['ReleaseSpinRate']

sns.regplot(x=x, y=y, line_kws={'color':'red'}, scatter_kws={"alpha":0.5})

plt.xlabel('Release Angle')
plt.ylabel('Release Spin Rate')
plt.title('Release Angle vs. Release Spin Rate')
plt.show()


# pitch type pie chart
pitch_type_counts = df['PitchType'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(pitch_type_counts, labels=pitch_type_counts.index, autopct='%1.1f%%', 
        startangle=140)

plt.axis('equal')
plt.title('Pitch Type Distribution')
plt.show()

# strike zone heatmap
x = df['TrajectoryLocationX']
z = df['TrajectoryLocationZ']
strike_zone_top = df['StrikeZoneTop']
strike_zone_bottom = df['StrikeZoneBottom']

plt.figure(figsize=(10, 8))
sns.kdeplot(x=x, y=z, cmap='coolwarm', shade=True)


strike_zone_left = -0.708  
strike_zone_right = 0.708  
plt.gca().add_patch(plt.Rectangle((strike_zone_left, strike_zone_bottom.min()), 
                                  strike_zone_right - strike_zone_left, 
                                  strike_zone_top.max() - strike_zone_bottom.min(), 
                                  fill=False, edgecolor='white', linewidth=2))

plt.xlabel('Horizontal Location')
plt.ylabel('Vertical Location')
plt.title('Strike Zone Heatmap')

sm = plt.cm.ScalarMappable(cmap='coolwarm')
sm.set_array([])
plt.colorbar(sm, label='Probability')

plt.show()

# game comparison tables

#balls and strikes by pitcher by game
summary_table = df.groupby(['GamePk', 'PitcherId']).agg({
    'Balls': 'sum',
    'Strikes': 'sum'
}).reset_index()
print(summary_table)


# count of pitch type and call combinations by pitcher by game
pitch_stats_counts = df[['GamePk', 'PitcherId', 'PitchType', 
                         'PitchCall']].value_counts().reset_index()
print(pitch_stats_counts)


# count of pitch type, pitch calls by batter side by inning by pitcher by game
bat_stats_counts = df[['GamePk', 'PitcherId', 'PitchType', 
                         'PitchCall', 'BatterSide', 
                         'Inning']].value_counts().reset_index().sort_values(['GamePk', 'PitcherId'])
bat_stats_counts.columns = ['GamePk', 'PitcherId', 'PitchType', 'PitchCall', 
                            'BatterSide', 'Inning', 'Count']
print(bat_stats_counts)



