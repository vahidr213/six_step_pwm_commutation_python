# pwm for 6 step firing with 100 Hz  frequency and changing duty cycle from 0 - 100%
import RPi.GPIO as IO         #calling header file which help us use GPIO'S of PI
import time   #calling time to provide delays in program
IO.setwarnings(False)       #don't show any warnings

#setting 6 GPIO pins as output for 6 step commutation
IO.setmode(IO.BCM)      #WE ARE PROGRAMMING THE gpio BY BCN PIN NUMBERS. (PIN35 AS 'GPIO19')
IO.setup(2,IO.OUT)      #initialize GPIO2 as an output
IO.setup(3,IO.OUT)      #initialize GPIO3 as an output
IO.setup(4,IO.OUT)      #initialize GPIO4 as an output
IO.setup(17,IO.OUT)      #initialize GPIO17 as an output
IO.setup(27,IO.OUT)      #initialize GPIO27 as an output
IO.setup(22,IO.OUT)      #initialize GPIO22 as an output

fr4pwm = 100
p1 = IO.PWM(2,fr4pwm)   #GPIO2 as PWM output with 100 HZ frequency
p2 = IO.PWM(3,fr4pwm)   #GPIO3 as PWM output with 100 HZ frequency
p3 = IO.PWM(4,fr4pwm)   #GPIO4 as PWM output with 100 HZ frequency
p4 = IO.PWM(17,fr4pwm)   #GPIO17 as PWM output with 100 HZ frequency
p5 = IO.PWM(27,fr4pwm)   #GPIO27 as PWM output with 100 HZ frequency
p6 = IO.PWM(22,fr4pwm)   #GPIO22 as PWM output with 100 HZ frequency


fireinterval = 1/(6*fr4pwm)
print(fireinterval)

p1.start(0)  #generate PWM signal with 0% duty cycle on GPIO2
time.sleep(fireinterval);   # interval bw firing pulses
p2.start(0)  #generate PWM signal with 0% duty cycle on GPIO3
time.sleep(fireinterval);   # interval bw firing pulses
p3.start(0)  #generate PWM signal with 0% duty cycle on GPIO4
time.sleep(fireinterval);   # interval bw firing pulses
p4.start(0)  #generate PWM signal with 0% duty cycle on GPIO17
time.sleep(fireinterval);   # interval bw firing pulses
p5.start(0)  #generate PWM signal with 0% duty cycle on GPIO27
time.sleep(fireinterval);   # interval bw firing pulses
p6.start(0)  #generate PWM signal with 0% duty cycle on GPIO22


try:
    while 1:    #execute loop forever
        for x in range(50): #execute loop for 50 times, x being incremented from 0 to 49.
            p1.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            p2.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            p3.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            p4.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            p5.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            p6.ChangeDutyCycle(x)    # change duty cycle for varying the speed of ac motor.
            
            time.sleep(0.1) #sleep for 100 milli seconds

        for x in range(50): #EXECUTE LOOP FOR  50 TIMES X BEING INCREMENTED FROM 0 TO 49
            p1.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            p2.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            p3.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            p4.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            p5.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            p6.ChangeDutyCycle(100-x)        #change duty cycle for changing the speed of ac motor.
            
            time.sleep(0.1) #sleep for 100 milli seconds
except KeyboardInterrupt:    # KeyboardInterrupt : user signal executed by user; by pressing Ctrl+C the following lines are executed
    p1.stop()  # stop pwm 1
    p2.stop()  # stop pwm 2
    p3.stop()  # stop pwm 3
    p4.stop()  # stop pwm 4
    p5.stop()  # stop pwm 5
    p6.stop()  # stop pwm 6
    IO.cleanup()  # sets the GPIO's to inital states (some High some Low)
        
        