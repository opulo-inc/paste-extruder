from leash import Lumen

lumen = Lumen()

lumen.connect()
lumen.home()

boardHeight = 9.6

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

lumen.safeZ()

lumen.goto(x=20, y=20)

lumen.sm.send("G92 A0")
lumen.setSpeed(f=2000)
lumen.sm.send("M906 A400")
lumen.goto(a = lumen.position["a"] + 100 )

lumen.sleep(2)

lumen.setSpeed(f=50000)

lumen.safeZ()

for pos in resistorPads:
    # move above position
    lumen.goto(x = pos[0], y = pos[1], z = lumen.parkZ)
    # plunge to position
    lumen.goto(z = boardHeight)

    # extrude
    lumen.setSpeed(f=2000)
    lumen.goto(a = lumen.position["a"] + 5 ) 

    lumen.sleep(0.1)  

    # z back to safe z
    lumen.setSpeed(f=50000)
    lumen.goto(z = lumen.parkZ)

for pos in ledPads:
    # move above position
    lumen.goto(x = pos[0], y = pos[1], z = lumen.parkZ)
    # plunge to position
    lumen.goto(z = boardHeight)

    # extrude
    lumen.setSpeed(f=2000)
    lumen.goto(a = lumen.position["a"] + 5 )

    lumen.sleep(0.1)

    # z back to safe z
    lumen.setSpeed(f=50000)
    lumen.goto(z = lumen.parkZ)
    
lumen.sm.send("M906 A100")
lumen.idle()

