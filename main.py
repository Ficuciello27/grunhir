def grunhir():
    basic.pause(500)
    for abrir_boca in range(5):
        pass
def rugir():
    pass
robotbit.servo(robotbit.Servos.S8, 20)
robotbit.servo(robotbit.Servos.S7, 90)
robotbit.servo(robotbit.Servos.S6, 90)

def on_forever():
    rugir()
basic.forever(on_forever)
