import PySimpleGUI as sg
from numpy import loadtxt
from os import system

sg.theme('TanBlue')

Levels = [
       'arena_01',
       'arena_02',
       'arena_04',
       'arena_05', 
       'arena_07', 
       'arena_08', 
       'arena_17',
       'forgottenislandoutro',
       'hub', 
       'hub_arena', 
       'hub_challenge', 
       'hub_worldtgs',
       'robarea1', 
       'robarea3', 
       'robarea5', 
       'robarea6', 
       'levelrob1',
       'testhats',
       'testlevel', 
       'testlevel2', 
       'testlevelblock', 
       'testlevelcinematics',
       'testlevelcinematics2', 
       'testlevelenemies', 
       'testlevelninja',
       'testlevelquest', 
       'testlevelrace', 
       'testlevelscroll',
       'testlevelwater'
       ]


layout = [  [sg.Text('PAK File:'), sg.FileBrowse(key="PAK")],
            [sg.Text('Level to Load'), sg.Combo(Levels, key="level")],
            [sg.Button('Patch')] ]

# Create the Window
window = sg.Window('tFPA Toolbox', layout, size=(300, 100))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    PAK = values["PAK"]
    level = values["level"]
    if event == 'Patch': # if user closes window or clicks cancel
        system("quickbms.exe -w -r -r" + "nyxquest.bms" + PAK + level)

    if sg.WIN_CLOSED == True:
        break
window.close()

