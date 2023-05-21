import PySimpleGUI as sg
import subprocess

# Do this to not get error for no reason
PAK = ''
level = ''

sg.theme('TanBlue')

Levels = [
       'arena01',
       'arena02',
       'arena04',
       'arena05', 
       'arena07', 
       'arena08', 
       'arena17',
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
window = sg.Window('tFPA Unused Level Tool', layout, size=(300, 100), icon="tFPA.ico")
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    PAK = values["PAK"]
    level = values["level"]
    if event == 'Patch': # if user closes window or clicks cancel
        subprocess.run(args=["quickbms.exe", "-w", "-r", "-r", "nyxquest.bms", PAK, "Levels/" + level], shell=True)
    if sg.WIN_CLOSED == True:
        break
window.close()

