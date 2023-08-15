print ("Hello adventurer! Welcome to Choose Your Journey!\n")

user = input("Please, tell me your name:\n>")
print("\nIndeed a curious name.\nVery well " + str(user) + ", the future of this journey is now in your hands.\nChoose wisely and, for your first, and last, unchangeable event:\nWake up.")
while True:
    print("\nYou wake up suddenlly, what a strange dream that was.")
    print("\nLooking around you realise to be in a tent, you were hunting something weren't you? A beast?")
    choice = input("1. An owl bear\n2. A manticore\n>")
    if int(choice) == 1:
        print("Yes, an owl bear, a big predator with the body of a bear and head and talons like an owl that's why you're in the wild, searching for it in the dark forest close to Hyeran.\nPeople from the village claim to have seen it killing a man in open sight.")
        print("You look around and ready your equipment for continue the hunt, where will you search for the beast?")
        choice = input("1. Along the river\n2. The forbidden woods\n>")
        if int(choice) == 1:
            print("All beasts need water, smart thinking.")
            print("You pick up your gear and go searching, soon you arrive at the river and start walking along it.\nYou see some markings crossing the water to the other side, but there's also a path open in the woods.\nWhere will you go?")
            choice = input("1. Cross the river\n2. Enter the forest\n>")
            if int(choice) == 1:
                print("You cross the river as if the track is enough to be seen it might be fresh.\nYou follow the markings and see an open area inside the forest, sure enough, the creature is laying there facing the opposite direction from where you are, and seems to be guarding something.\nShould you use this opportunitty or wait to see what the animal guards?")
                choice = input("1. Attack, now\n2. Wait and discover what it's hiding\n>")
                if int(choice) == 1:
                    print("You ready your bow as you don't think any chances of killing it would be better than now and shoot an arrow with paralysis poison at the beast.\n It stands in pain and search angrilly for the offender but soon gets confused and falls asleep as the poison is quite strong.\nAs soon as it hits the ground you hear a cry from beside it, a little cub jumps around the, you guess, mother, crying in fear")
                    print("Your heart sink, you were about to kill a mother taking care of its cub, will you carry on with the plan? Will you spare it?")
                    choice = input("1. End the beast\n2. Let it be\n>")
                    if int(choice) == 1:
                        print("You've travelled too far for just turning around now, a man died, got a taste for humans, leave it and more people might die.")
                        print("You step closer to it, the cub realising your presence and instantly getting quiet, it looks at you attentivelly without moving, as if frozen, and then:")
                        print("You see it, their eyes, they're human eyes.\n_Please, don't hurt me - says the little beast with a heavy, hoarse voice, the words enough to stun you in place, What is happening?")
                        choice = input("1. Get closer\n2. Stay put\n>")
                        if int(choice) == 1:
                            print("You step closer to the cub, who's shaking in fear by that point but still not moving a muscle to run.\n_It's okay, I won't hurt you - you say, the thoughts of harm vanishing from your mind.")
                            print("_You hurt Nando - the little one answers and you stop in your tracks, is Nando the beast? Wait, the missing man's name... - He didn't do anything I swear, we're were leaving, didn't hurt anyone, please don't cage us, don't harm us - it keeps begging, the voice shaking and you can see tears in it's big wide eyes.\nSuddenly you hear a groan coming from the paralised creature.")
                            choice = input("1. Run\n2. Stay\n>")
                            if int(choice) == 1:
                                print("The sound startles you enough that you run away, leaving the misterious animals behind.")
                                print("End of journey - Sleeping Beast\nIf you wish to play again type R, if you wish to quit type Q")
                                replay = input(">")
                                if replay.lower() == "r":
                                    continue
                                if replay.lower() == "q":
                                    quit()
                                else:
                                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                    replay = input(">")
                                    if replay.lower() == "r":
                                        continue
                                    if replay.lower() == "q":
                                        quit()
                            if int(choice) == 2:
                                print("The fear makes it impossible to run and you watch the enormous beast getting up, still weak from the poison but slowly reagaining it's strength, it looks at you and at the cub who runs close to it.\n_Nando! - it yells happilly - The human said won't hurt us! I told you they weren't all bad!")
                                print("_Hyera stop, they're a hunter, stay behind me - growls the owlbear, it looks at you and at your bow still in your hand.")
                                choice = input("1. Put the bow down\n2. Ready the bow in a defensive stance\n>")
                                if int(choice) == 1:
                                    print("You realise the threat and puts the bow down slowly and raising your hands.\n_I won't hurt you, I was asked by vilagers to find the owlbear who killed, well, Nando - you say sincerely, the beast emmits somewhat of a laughter, but not a good one, a sad, hopeless laugh.")
                                    print("_They sent you to kill Nando, that's what they did - says the beast sadly - They didn't listen, no one did. Devil's magic they said, a curse that killed the man for the rise of a beast.")
                                    print("You're paralised with the story, No one said anything about this to you, they asked for your aid to hunt a monster knowing it was no just a man, but an innocent?\n_So you're a...?\n_I'm a druid, used to be a healer, but after the empire priests arrived I'm no more than a monster and my gods no more than demons - he says looking down adn then at the little cub still hidden behind him - I'm just thankful I found Hyera before they did, she was called by this land's magic, druid often are guided to their teachers by the forest, couldn't imagine what they would've done to her.")
                                    print("_Please, don't tell anyone where we went, we just want to live and be who we are - asks the owl bear now morphing into a human form, he's tall, slim and dark skinned, with long braided black hair and deep green eyes, his human voice is low and calming but worried.")
                                    choice = input("1. Agree\n2. Disagree\n>")
                                    if int(choice) == 1:
                                        print("_Of course, you deserve freedom - you answer and he nods sighing in relief, you then get you abandonned bow from the ground seeing he tensing again - You said priests yeah?\n_Please don't, when you murder an assassin the number of murderers doesn't decrease.\n_When you kill monsters you don't worry about how many of them will die, but about how many innocents will live. Farewell druid, till someday cub.")
                                        print("End of journey - The Great Hunt\nIf you wish to play again type R, if you wish to quit type Q")
                                        replay = input(">")
                                        if replay.lower() == "r":
                                            continue
                                        if replay.lower() == "q":
                                            quit()
                                        else:
                                            print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                            replay = input(">")
                                            if replay.lower() == "r":
                                                continue
                                            if replay.lower() == "q":
                                                quit()
                                    if int(choice) == 2:
                                        print("_Why do you have to leave? That village is your home, you shouldn't have to go somewhere else.\n_Child, I don't have the energy neither the will to fight for territory, home is where wish to die at not where you were born - says the old druid turning back into an owlbear - It was good to meet you hunter, I wish others had the respect and empathy you have.")
                                        print("End of journey - Finding Home\nIf you wish to play again type R, if you wish to quit type Q")
                                        replay = input(">")
                                        if replay.lower() == "r":
                                            continue
                                        if replay.lower() == "q":
                                            quit()
                                        else:
                                            print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                            replay = input(">")
                                            if replay.lower() == "r":
                                                continue
                                            if replay.lower() == "q":
                                                quit()
                                    else:
                                        print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                        replay = input(">")
                                        if replay.lower() == "r":
                                            continue
                                        if replay.lower() == "q":
                                            quit()
                                if int(choice) == 2:
                                    print("You ready your bow, the owl bear growls at you, it's a lost battle and you know it, but the adrenaline makes you stiff, waiting for the attack looking into deep green eyes. It charges and before you could shoot the beak is in your neck and the claws give you one last hug.")
                                    print("End of journey - Lost Defense\nIf you wish to play again type R, if you wish to quit type Q")
                                    replay = input(">")
                                    if replay.lower() == "r":
                                        continue
                                    if replay.lower() == "q":
                                        quit()
                                    else:
                                        print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                        replay = input(">")
                                        if replay.lower() == "r":
                                            continue
                                        if replay.lower() == "q":
                                            quit()
                                else:
                                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                    replay = input(">")
                                    if replay.lower() == "r":
                                        continue
                                    if replay.lower() == "q":
                                        quit()
                            else:
                                print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                replay = input(">")
                                if replay.lower() == "r":
                                    continue
                                if replay.lower() == "q":
                                    quit()
                        if int(choice) == 2:
                            print("You stand your ground, afraid to disturb the talking cub, your mind races thinking of what to do in such a weird situation, seeing your hesitation the cub charges onto you, making you fall and hit you head on a rock, losing conscience.")
                            print("End of journey - Lazy End\nIf you wish to play again type R, if you wish to quit type Q")
                            replay = input(">")
                            if replay.lower() == "r":
                                continue
                            if replay.lower() == "q":
                                quit()
                            else:
                                print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                                replay = input(">")
                                if replay.lower() == "r":
                                    continue
                                if replay.lower() == "q":
                                    quit()
                        else:
                            print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                            replay = input(">")
                            if replay.lower() == "r":
                                continue
                            if replay.lower() == "q":
                                quit()
                    if int(choice) == 2:
                        print("You regret shooting the arrow, no cub should be orphaned like this, you leave the sight ready to tell the villagers to leave the beast be, as you didn't find it and the tracks were old and leaving the surroundings")
                        print("End of journey - Mercy\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                                quit()
                    else:
                        print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
                if int(choice) == 2:
                    print("You wait to see what it has with it, if it's a living person the arrow might encourage an attack, soon you see a little cub behind the animal, jumping up and down.\n_But Nando! I don't know how to do this!")
                    print("You almost gasp in surprise, the cub just talked? And Nando? That's the dead man's name!")
                    choice = input("1. Leave\n2. Keep watching\n>")
                    if int(choice) == 1:
                        print("Calm down Hyera, meditating is hard when you start it, but you'll soon understand why it's so necessary - says the owlbear, the voice is animalistic but calm, like a teacher talking to a student, suddenly it starts sniffing the air and looks to you where you're hidden.")
                        choice = input("1. Run\n2. Freeze\n>")
                        if int(choice) == 1:
                            print("You're scared to the bones by it, so you run as fast as you can, hoping to not be chased by the weird talking beasts")
                            print("End of journey - Listen and Run\nIf you wish to play again type R, if you wish to quit type Q")
                            replay = input(">")
                            if replay.lower() == "r":
                                continue
                            if replay.lower() == "q":
                                quit()
                        if int(choice) == 2:
                            print("You freeze behind the bushes, barely breathing and hoping for the creature not to notice you, it stands and look at you for a moment longer, then luckilly turns away looking at the cub.\n_I think we better get moving again Hyera, We're still quite close to the village - and just like this both of them go away and you're still frozen until you can't hear the steps anymore.")
                            print("End of journey - Stay Invisible\nIf you wish to play again type R, if you wish to quit type Q")
                            replay = input(">")
                            if replay.lower() == "r":
                                continue
                            if replay.lower() == "q":
                                quit()
                else:
                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
            if int(choice) == 2:
                print("The path in the forest might be the best guess as there would be no reason for the owlbear to leave it's territory and an opening in the woods leads to think it passes constantly through it.")
                print("You follow the gap in the dark forest, walking for hours until you see something in the distance, but, as you get closer quietly you realise it isn't the owlbear you're searching for, but an unicorn peacefully eating grass, it's coat is white with dark brown markings and the horn glows with a magical aura")
                choice = input("1. Leave it be and return to camp\n2. Get closer\n>")
                if int(choice) == 1:
                    print("You decide to leave the beautiful sight as it wasn't your goal to hunt a peaceful creature and decides to tell the villagers that the owlbear crossed the river and surely won't disturb them anymore")
                    print("End of journey - Wrong Turn\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
                if int(choice) == 2:
                    print("You decide to get closer to the animal, maybe cut some of it's mane as proof that you've seen it as you never met anyone who claimed to see one with any proof, but when you're almost touching it the thought to be peaceful creature turns to you with red violent eyes and you soon understands why you never met someone who could prove to have seen it")
                    print("End of journey - Lure\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
            else:
                print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                replay = input(">")
                if replay.lower() == "r":
                    continue
                if replay.lower() == "q":
                    quit()
        if int(choice) == 2:
            print("The forest is good for making dens, where the beast would always be close to, good thinking.")
            print("You enter the dark woods, silently and carefully searching for hints when you find some tracks. Following them you find a split, some tracks go to the right while the others go to the left, which way you choose?")
            choice = input("1. Right\n2. Left\n>")
            if int(choice) == 1:
                print("You choose the right side and start following the tracks, unfortunately after some time it starts to rain, making it impossible to keep searching as the tracks disappear.")
                print("End of journey - Rain of Misfortune\nIf you wish to play again type R, if you wish to quit type Q")
                replay = input(">")
                if replay.lower() == "r":
                    continue
                if replay.lower() == "q":
                     quit()
            if int(choice) == 2:
                print("You decide to go left and the tracks soon lead to a dark cave covered by dense forest covering, in this part of the woods not even birds make any sound and the absolute silence sends a shiver down your spine. Entering it might be dangerous, but waiting outside might leave you here for several hours.")
                choice = input("1. Enter\n2. Wait\n>")
                if int(choice) == 1:
                    print("You risk entering the cave as you don't want to wait till night when the forest will become even more dangerous than just a single beast. Entering the darkness you can now hear some faint snorelike sounds, following them carefully you come up to the manticore laying in deep slumber, it has hundreds of battle marks along it's body, the humanlike face has a single scar going from eyebrow to chin and the partially open mouth show razor like teeth.")
                    print("You must now prepare to shoot the paralysis poison arrow while having some cover as the creature is capable of shooting venomous dards from its tail, so you hide behind a rock e ready you bow when you hear a strong thunder coming from outside the cave, making the animal jump from it's sleep.\nParalised to avoid being seen you watch as the manticore looks around with wide fearful eyes as another thunder roars through the cave, making it shiver and curl up tight, how weird to see such a fantastic beast to cower like this.")
                    print("Then it starts singing:\nAmazing grace, how sweet the sound\nThat saved a wrech like me\nI once was lost, but now am found\nWas blind, but now I see")
                    print("You recognize the lullaby your mother used to sing to you when you were a child, now it's the perfect moment to strike but your heart empathizes with the creature.")
                    choice = input("1. Strike\n2. Keep listening\n>")
                    if int(choice) == 1:
                        print("You came too far to hesitate now, with the rain you might not even find the owlbear so it's better to hunt this manticore than nothing, you aim and shoot, hiding right after. The animal growls in pain but as the poison runs through the blood it falls paralysed, giving you the chance to end the job.")
                        print("End of journey - A Coward's Hunt\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
                    if int(choice) == 2:
                        print("The nostalgia from the song is enough to make you hesitate and keep listening, the creature's voice slowly calms with the lullaby and, as the summer rain soon fades away, turns to soft snores once again. With the deep empathy developed for the creature you decide to spare it and leave the cave as it wasn't even you goal to find it in the first place.")
                        print("End of journey - Song Spare\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
        else:
            print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
            replay = input(">")
            if replay.lower() == "r":
                continue
            if replay.lower() == "q":
                quit()
    if int(choice) == 2:
        print("Yes, a manticore of course, a beast with the body of a lion, head of a man and scorpion tail, capable of shooting dangerous poison darts.\nSo you preapare your equipment and plan on where to search for it:")
        choice = input("1. Along the river\n2. The forbidden woods\n>")
        if int(choice) == 1:
            print("All beasts need water, smart thinking.")
            print("You pick up your gear and go searching, soon you arrive at the river and start walking along it.\nYou see some markings crossing the water to the other side, but there's also a path open in the woods.\nWhere will you go?")
            choice = input("1. Cross the river\n2. Enter the forest\n>")
            if int(choice) == 1:
                print("You cross the river as if the track is enough to be seen it might be fresh.\nYou follow the markings and see an open area inside the forest, sure enough, a creature is laying there facing the opposite direction from where you are, but it doesn't look like a manticore, instead it looks like somekind of bear and seems to be guarding something.\nShould you use this opportunitty of hunt or leave as this isn't what you were searching for?")
                choice = input("1. Attack, now\n2. Wait and discover what it's hiding\n>")
                if int(choice) == 1:
                    print("You ready your bow, as you don't think there's time left in today to go back hunting the manticore, and shoot an arrow with paralysis poison at the beast.\n It stands in pain and search angrilly for the offender but soon gets confused and falls asleep as the poison is quite strong.\nAs soon as it hits the ground you hear a cry from beside it, a little cub jumps around the, you guess, mother, crying in fear.\nTurns out it was an owlbear with it's cub")
                    print("As it wasn't the creature you wished to hunt and carrying it's child you decide to just leave, there is no pride in orphaning a cub")
                    print("End of journey - Mother's Mercy\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
                if int(choice) == 2:
                    print("You wait and see a little cub jumping around the bigger one, seeing it makes you hesitate and decide to leave the creatures as it wasn't your goal to orphan a cub.")
                    print("End of Journey - Family Sight\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
                else:
                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
            if int(choice) == 2:
                print("The path in the forest might be the best guess as there would be no reason for the manticore to leave it's territory and an opening in the woods leads to think it passes constantly through it.")
                print("You follow the gap in the dark forest, walking for hours until you see something in the distance, but, as you get closer quietly you realise it isn't the owlbear you're searching for, but an unicorn peacefully eating grass, it's coat is white with dark brown markings and the horn glows with a magical aura")
                choice = input("1. Leave it be and return to camp\n2. Get closer\n>")
                if int(choice) == 1:
                    print("You decide to leave the beautiful sight as it wasn't your goal to hunt a peaceful creature and decides to tell the villagers that the owlbear crossed the river and surely won't disturb them anymore")
                    print("End of journey - Wrong Turn\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
                if int(choice) == 2:
                    print("You decide to get closer to the animal, maybe cut some of it's mane as proof that you've seen it as you never met anyone who claimed to see one with any proof, but when you're almost touching it the thought to be peaceful creature turns to you with red violent eyes and you soon understands why you never met someone who could prove to have seen it")
                    print("End of journey - Lure\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()  
                else:
                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
            else:
                print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                replay = input(">")
                if replay.lower() == "r":
                    continue
                if replay.lower() == "q":
                    quit()
        if int(choice) == 2:
            print("The forest is good for making dens, where the beast would always be close to, good thinking.")
            print("You enter the dark woods, silently and carefully searching for hints when you find some tracks. Following them you find a split, some tracks go to the right while the others go to the left, which way you choose?")
            choice = input("1. Right\n2. Left\n>")
            if int(choice) == 1:
                print("You choose the right side and start following the tracks, unfortunately after some time it starts to rain, making it impossible to keep searching as the tracks disappear.")
                print("End of journey - Rain of Misfortune\nIf you wish to play again type R, if you wish to quit type Q")
                replay = input(">")
                if replay.lower() == "r":
                    continue
                if replay.lower() == "q":
                    quit()
            if int(choice) == 2:
                print("You decide to go left and the tracks soon lead to a dark cave covered by dense forest covering, in this part of the woods not even birds make any sound and the absolute silence sends a shiver down your spine. Entering it might be dangerous, but waiting outside might leave you here for several hours.")
                choice = input("1. Enter\n2. Wait\n>")
                if int(choice) == 1:
                    print("You risk entering the cave as you don't want to wait till night when the forest will become even more dangerous than just a single beast. Entering the darkness you can now hear some faint snorelike sounds, following them carefully you come up to the manticore laying in deep slumber, it has hundreds of battle marks along it's body, the humanlike face has a single scar going from eyebrow to chin and the partially open mouth show razor like teeth.")
                    print("You must now prepare to shoot the paralysis poison arrow while having some cover as the creature is capable of shooting venomous dards from its tail, so you hide behind a rock e ready you bow when you hear a strong thunder coming from outside the cave, making the animal jump from it's sleep.\nParalised to avoid being seen you watch as the manticore looks around with wide fearful eyes as another thunder roars through the cave, making it shiver and curl up tight, how weird to see such a fantastic beast to cower like this.")
                    print("Then it starts singing:\nAmazing grace, how sweet the sound\nThat saved a wrech like me\nI once was lost, but now am found\nWas blind, but now I see")
                    print("You recognize the lullaby your mother used to sing to you when you were a child, now it's the perfect moment to strike but your heart empathizes with the creature.")
                    choice = input("1. Strike\n2. Keep listening\n>")
                    if int(choice) == 1:
                        print("You came too far to hesitate now, you aim and shoot, hiding right after. The animal growls in pain but as the poison runs through the blood it falls paralysed, giving you the chance to end the job.")
                        print("End of journey - A Coward's Hunt\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
                    if int(choice) == 2:
                        print("The nostalgia from the song is enough to make you hesitate and keep listening, the creature's voice slowly calms with the lullaby and, as the summer rain soon fades away, turns to soft snores once again. With the deep empathy developed for the creature you decide to spare it and leave the cave.")
                        print("End of journey - Song Spare\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
                    else:
                        print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                        replay = input(">")
                        if replay.lower() == "r":
                            continue
                        if replay.lower() == "q":
                            quit()
                if int(choice) == 2:
                    print("You decide on waiting as a cave with a monster who can shoot venomous darts is not the ideal scenario, while waiting it starts to rain and you're forced to go back to camp.")
                    print("End of journey - Rain of Misfortune\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
                else:
                    print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                    replay = input(">")
                    if replay.lower() == "r":
                        continue
                    if replay.lower() == "q":
                        quit()
            else:
                print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
                replay = input(">")
                if replay.lower() == "r":
                    continue
                if replay.lower() == "q":
                    quit()
        else:
            print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
            replay = input(">")
            if replay.lower() == "r":
                continue
            if replay.lower() == "q":
                quit()
    else:
        print("You die.\nEnd of Journey - I Can't Type\nIf you wish to play again type R, if you wish to quit type Q")
        replay = input(">")
        if replay.lower() == "r":
            continue
        if replay.lower() == "q":
            quit()
        
                            