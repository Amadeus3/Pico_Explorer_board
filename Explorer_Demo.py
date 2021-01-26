import time, random
import picoexplorer as explorer

width = explorer.get_width()
height = explorer.get_height()

display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
explorer.init(display_buffer)

explorer.set_backlight(1.0)
explorer.set_audio_pin(0)

A_Pressed = False
B_Pressed = False
X_Pressed = False
Y_Pressed = False

i = 1

while True:
    explorer.set_pen(120, 40, 60)    
    explorer.clear()
    
    adc0 = int(explorer.get_adc(0) * 120)
    adc1 = int(explorer.get_adc(1) * 120)
    adc2 = int(explorer.get_adc(2) * 120)
    
    explorer.set_pen(255, 255, 255)

    explorer.text("ADC0:", 20, 20, 100)    
    explorer.text("ADC1:", 20, 40, 100)    
    explorer.text("ADC2:", 20, 60, 100)    
    explorer.text("Button:", 20, 80, 100)    
    
    if explorer.is_pressed(explorer.BUTTON_A):
        if A_Pressed == True:
            A_Pressed = False
        else:
            A_Pressed = True
          
    if explorer.is_pressed(explorer.BUTTON_B):
        if B_Pressed == True:
            B_Pressed = False
        else:
            B_Pressed = True

    if explorer.is_pressed(explorer.BUTTON_X):
        if X_Pressed == True:
            X_Pressed = False
        else:
            X_Pressed = True

    if explorer.is_pressed(explorer.BUTTON_Y):
        if Y_Pressed == True:
            Y_Pressed = False
        else:
            Y_Pressed = True
        
    if A_Pressed == True:
        explorer.text("A", 110, 80, 100)
    if B_Pressed == True:
        explorer.text("B", 130, 80, 100)
    if X_Pressed == True:
        explorer.text("X", 150, 80, 100)
    if Y_Pressed == True:
        explorer.text("Y", 170, 80, 100)
       
    explorer.set_pen(adc0 * 2, 0, 0) 
    explorer.circle(90 + adc0, 26, 10)
    
    explorer.set_pen(0, adc1 * 2, 0) 
    explorer.circle(90 + adc1, 46, 10)

    explorer.set_pen(0, 0, adc2 * 2) 
    explorer.circle(90 + adc2, 66, 10)

    explorer.set_pen(255, 255, 255)
    explorer.text("Plug a jumper wire from GP0 to AUDIO to hear noise!", 20, 110, 200)    

    explorer.set_tone(i)

    if i > 600:        
        explorer.text("Motor 1: Forwards", 20, 180, 200)    
        explorer.set_motor(0, 0, 1)
    else:
        explorer.text("Motor 1: Backwards", 20, 180, 200)    
        explorer.set_motor(0, 1, 1)
    
    if i > 600:
        explorer.text("Motor 2: Forwards", 20, 200, 200)    
        explorer.set_motor(1, 0, 1)
    else:
        explorer.text("Motor 2: Backwards", 20, 200, 200)    
        explorer.set_motor(1, 1, 1)

    i = i + 20
    if i > 1000:
        i = 1
        
    explorer.update()
    time.sleep(0.1)