from pop import Camera

from pop.Pilot import Object_Follow

from pop.Pilot import SerBot

from time import sleep

bot = None

of = None



def setup():

    global bot, of

    cam = Camera() # 21fps

    of = Object_Follow(cam)

    bot = SerBot()

    of.load_model()

    print("="*50)

    print("Model load ok!")

    print("It starts in about 10 seconds.")



def loop():

    is_person = False

    person = of.detect(index='person')

    # person 을 못찾으면 -> 무조건 서는게 아니고 오른쪽으로 회전 하는데 얼마나 돌게 할 것인가 ?? 이게 중요함



    # TODO 앞에 사람이 있을 때

    if person or is_person:

        x = round(person['x'] * 4, 1) # 여기서 4도 변경가능

        rate = round(person['size_rate'], 5)



        # rate가 0.25보다 클 때

        if rate > 0.25:

            bot.stop()

        

        # rate가 0.25보다 작고 ~ 보다 클 때

        elif 0.25 <= rate and 0.10:

            bot.forward(20)

            bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

        

        elif 0.09 <= rate and rate >= 0.04:

            bot.forward(50)

            bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

        

        else:

            bot.forward(70)

            bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x



        # debuging

        print(f"{rate}, {bot.steering}") # f string 

        sleep(1)

    

    # TODO 못 찾게 되었을 때

    else:

        # TODO 오른쪽으로 일정 각도 만큼 돌고 사람이 있는지 체크

        while (1) :

            bot.turnRight()

            sleep(0.2)

            bot.stop()

            

            person = of.detect(index='person')

            if person:

                x = round(person['x'] * 4, 1) # 여기서 4도 변경가능

                rate = round(person['size_rate'], 5)



                # rate가 0.25보다 클 때

                if rate > 0.25:

                    bot.stop()

                

                # rate가 0.25보다 작고 ~ 보다 클 때

                elif 0.25 <= rate and 0.10:

                    bot.forward(20)

                    bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

                

                elif 0.09 <= rate and rate >= 0.04:

                    bot.forward(50)

                    bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

                

                else:

                    bot.forward(70)

                    bot.steering =  1.0 if x > 1.0 else -1.0 if x < -1.0 else x

                break

            else:

                print("person not dectected...")  

 

def main():

    setup()

    while True:

        try:

            loop()

        except KeyboardInterrupt:

            break

    bot.stop()



if __name__ == '__main__':

    main()
