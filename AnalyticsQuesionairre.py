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
import numpy as np
from scipy import stats

#establsih wd
directory_path = '/Users/hillarywolff/documents/github/detroittigersanalytics'
os.chdir(directory_path)

current_directory = os.getcwd()
print(current_directory)

#import dataset

PATH = r'/Users/hillarywolff/documents/github/detroittigersanalytics/'
df = pd.read_csv(PATH+'AnalyticsQuestionnairePitchData.csv')

print(df.columns.tolist())

#1 histogram of pitch types

pitch_type_counts = df['PitchType'].value_counts()

plt.bar(pitch_type_counts.index, pitch_type_counts.values)
plt.xlabel('Pitch Type')
plt.ylabel('Frequency')
plt.title('Distribution of Pitch Types')
plt.xticks(rotation=45)
plt.show()


#2 barchart of pitch calls

pitch_call_counts = df['PitchCall'].value_counts()

plt.bar(pitch_call_counts.index, pitch_call_counts.values)
plt.xlabel('Pitch Call')
plt.ylabel('Frequency')
plt.title('Frequency of Pitch Calls')
plt.xticks(rotation=30)
plt.show()

#3 box plot of release speed


sns.boxplot(x='GamePk', y='ReleaseSpeed', data=df)
plt.xlabel('Game')
plt.ylabel('Release Speed')
plt.title('Release Speed Distribution in Two Games')
plt.show()

#4 scatter plot of release angle vs release spin rate

x = df['ReleaseAngle']
y = df['ReleaseSpinRate']

sns.regplot(x=x, y=y, line_kws={'color':'red'}, scatter_kws={"alpha":0.5})

plt.xlabel('Release Angle')
plt.ylabel('Release Spin Rate')
plt.title('Release Angle vs. Release Spin Rate with Trend Line')
plt.show()


#5 pitch type pie chart

pitch_type_counts = df['PitchType'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(pitch_type_counts, labels=pitch_type_counts.index, autopct='%1.1f%%', startangle=140)

plt.axis('equal')
plt.title('Pitch Type Distribution')
plt.show()

#7 strike zone heatmap

x = df['TrajectoryLocationX']
z = df['TrajectoryLocationZ']

plt.figure(figsize=(10, 8))
sns.kdeplot(x=x, y=z, bins=50, cmap='coolwarm', cbar=True)
plt.colorbar().set_label('Frequency')
plt.xlabel('Horizontal Location')
plt.ylabel('Vertical Location')
plt.title('Strike Zone Heatmap')
plt.gca().invert_yaxis()  
plt.show()

#8 pitch trajectory plot

#9 performance summary table

#10 game comparison table
















