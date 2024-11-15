from leash import Lumen
import sys

# This script is an example of how one might use the LumenPnP paste extruder to deposit material.
# It heavily depends on leash as the interface with the machine. For more information on how leash works,
# check out its source here: https://github.com/opulo-inc/leash

# ----------------------------
# Defining Positions
# ----------------------------

boardHeight = 11.5

boardOffset = [17.75, 2.25]

# For this demo, pad locations are manually inputted. Ideally a utility generates these positions based on source.
resistorPads = [
    [361.6, 216.2],
    [361.6, 214.4],
    [365.8, 214.4],
    [364.6, 213.2],
    [367.4, 210.2],
    [365.8, 210.2],
    [365.6, 206.2],
    [364.4, 207.4],
    [361.6, 204.4],
    [361.6, 206.0],
    [357.4, 206.2],
    [358.6, 207.4],
    [355.8, 210.2],
    [357.4, 210.2],
    [357.4, 214.4],
    [358.6, 213.2]
]

ledPads = [
    [360.2, 219.8],
    [362.0, 219.8],
    [367.6, 217.4],
    [368.8, 216.2],
    [371.2, 210.6],
    [371.2, 209.0],
    [368.8, 203.6],
    [367.4, 202.2],
    [362.0, 199.8],
    [360.2, 199.8],
    [354.6, 202.2],
    [353.2, 203.6],
    [351.0, 209.0],
    [351.0, 210.8],
    [353.6, 216.2],
    [354.8, 217.4]

]

# ----------------------------
# Creating lumen instance, connecting, homing
# ----------------------------

lumen = Lumen()

if not lumen.connect():
    lumen.log.error("Couldn't connect, exiting.")
    sys.exit()

lumen.home()
lumen.lightOn("TOP")

# ----------------------------
# Priming the extruder
# ----------------------------

lumen.goto(x=20, y=20)
# bumping the current to 400ma
lumen.sm.send("M906 B400")

lumen.sm.send("G92 B0")
lumen.setSpeed(f=2000)

# extrude 300 beyond current position
lumen.goto(b = lumen.position["b"] - 300 )

# allowing some ooze
lumen.sleep(12)

# ----------------------------
# Depositing paste
# ----------------------------

lumen.setSpeed(f=50000)
lumen.safeZ()

for pos in resistorPads:
    # move above position
    lumen.goto(x = pos[0] + boardOffset[0], y = pos[1] + boardOffset[1], z = lumen.parkZ)
    # plunge to position
    lumen.goto(z = boardHeight)

    # extrude
    lumen.setSpeed(f=2000)
    lumen.goto(b = lumen.position["b"] - 6 ) 

    lumen.sleep(0.6)  

    # z back to safe z
    lumen.setSpeed(f=50000)
    lumen.goto(z = lumen.parkZ)

for pos in ledPads:
    # move above position
    lumen.goto(x = pos[0] + boardOffset[0] + 0.5, y = pos[1] + boardOffset[1] + 0.5, z = lumen.parkZ)
    # plunge to position
    lumen.goto(z = boardHeight)

    # extrude
    lumen.setSpeed(f=2000)
    lumen.goto(b = lumen.position["b"] - 6 )

    lumen.sleep(0.6)

    # z back to safe z
    lumen.setSpeed(f=50000)
    lumen.goto(z = lumen.parkZ)

lumen.idle()
