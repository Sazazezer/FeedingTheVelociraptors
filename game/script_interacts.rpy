## Offices
label check_offices_1:
    if prog == 0:
        t "So, it’s decided. Paul has to die."
        $ location = 9
        jump forceroomrefresh
        a "This is horrible. I can’t believe it’s come down to this."
        $ prog = 1
        h "It is the only remaining response. The raptors have swarmed the compound. The lockdown system will only be active for a few more hours." 
        t "Communications are out. We have no defensive capabilities."
        a "Yeah but, what you’re suggesting is-"
        j "Oh, can it. It’s his fault we’re in this mess in the first place. Who tries to deliver data reports by disabling the security fields and wandering over to the boss."
        p phappy "Well no one now, considering how much blood isn’t in his body."
        j "If the raptors hadn’t eaten Todd, we might have been abe to get communications back online."
        p "And if Todd hadn’t been so delicious, then the Raptors probably wouldn’t have eaten him. Really, it’s his fault we’re in this mess."
        h "Anyway! The plan is clear. Once our route has been secured, Paul will be thrown out through the back entrance of the building and left to fend for themselves." 
        h "With the ensuring distraction, we will make our way to the helicopter in the parking lot."
        t "Heh, and you said me trying to validate my parking was ridiculous."
        h "People are still dead, Tony."
        t "Right... Sorry."
        h "Now, i’m sure there may be a desperate desire to be selfish and do what we can to ensure that we stay alive. At the very least, recognise that Tony must stay alive."
        h "He is the only one here that can pilot a helicopter. None of us live without him."
        p "Pretty sure i don’t get to live at all."
        h "Nonsense. If the four of us successfully escape and you remain uneaten and manage to find a way into a part of the building that cannot be accessed by velociraptors,"
        h " then you are free to stay alive until the cleanup crew arrives to take care of this mess."
        p "Oh, well that actually sounds pretty reasonabl-"
        h "in about six to eight weeks."
        p "Ah."
        h "Yeah, there’s going to be a lot of political stuff going on when we get back. Too many people have been stating that this place is a death trap waiting to happen."
        h "And well, you proved them right."
        h "I won’t lie. We will be listing you among the dead. If you make it, you can be a nice surprise for the clean crew to find."
        h "It is the least you deserve."
        p "Come on guys. There’s got to be a better plan than this."
        h "There is not. This has been discussed, and you had plenty of time to interject beforehand."
        p "I was in the bathroom."
        j "For three hours."
        p "I’ve seen you hog the cubicle, Jenny. Don’t act cocky on me now."
        h "None of this matters. We are talking to a dead person. Let us prepare."
        p "Wait, you can’t do this. At the very least give me some kind of chance."
        t "Donald didn’t get a chance."
        p "Donald was slower than me, and more susceptible to getting dirt thrown in his eyes. It was survival of the fittest out there."
        t "He was the only one of us armed and trained to fight those things and you shoved him into that tree first chance you got."
        p "Oh please. If he was really trained and not just lying on his CV, shouldn’t he have been able to take out three turkey dinosaurs before they overwhelmed him?"
        j "Not with the dirt in his eyes."
        a "Jenny. I really don’t think-"
        h "Oh. Fine. You have one hour. We need to prepare anyway."
        h "Don’t leave the building. Don’t turn lockdown off. If you come up with a better plan that lets all five of us survive, then we’ll hear it."
        t "You can’t be serious."
        h "He's no threat to us anyway, and we need the time. This is an administrative building. There’s nothing here of any use anyway. "
        h "And if they do find something, it’s not like i’m against them coming with us."
        p "You sure there’s no way for me to leave the building."
        h "Jesus, no. And don’t even try. The lockdown field is the only thing keeping us alive."
        j "Go. You have one hour."
        $ location = 9
        jump forceroomrefresh
    else:
        if have_ak47 and not ak47Scare:
            alt "Jam appears holding the gun." #!! test to see if this shows in game
            p "Hey everyone."
            j "Oh good lord."
            p "Just checking in. How's everyone doing?"
            j "Paul... where- where did you get that?"
            p "Oh this? I found it."
            j "And... what are you going to do with it?"
            p "Oh. i guess we'll all see."
            j "..."
            a "..."
            t "..."
            h "..."
            p "..."
            p "Well. Nothing much going on here. I'll catch you all later."
            p "Or not. Who knows."
            show mono empty
            j ". . . What the hell?"
            $ ak47Scare = True
            $ location = 3
            jump forceroomrefresh
        else:
            if evi_count > 1:
                p "Well. I think i’m good to go."
                p "The crowd has gathered. Is it time for me to present the evidence that i have so painstakingly uncovered?"
                jump accusation
            else:
                t "Oh. You're back."
                t "It's not been an hour yet. Or are you ready to begin."
                p "No no. Just having a bit of a wander."
                p "Still haven't had my lunch yet."
                p "Be back soon."
                t "..."
                $ location = 3
                jump forceroomrefresh

## Special Temp Corridor for initial scene
label temp_corridor:
    p "Well, this is a sticky little pickle i’ve gotten us into. How will i escape today?"
    #!!remvoe test skip
    $ location = 3
    play music "FTV-A.wav"
    $ prog = 2
    jump forceroomrefresh
    t "Oi."
    p "Ah, helicopter man. Excellent. I knew you’d come around."
    t "What?"
    p "Why, we are the only true smart ones here. Come, let us escape together."
    t "No. God no. What the hell is wrong with-"
    t "Look, i just came out here to say. To be clear with you."
    t "you’re going to be dead after this hour is up."
    t "I’ve seen people in their final moments before. Unexpected. Not wanting to be there. It’s rarely the clean and noble death people want."
    p "Sooo, you wanna swap?"
    t "..."
    t " What i’m trying to say is, don’t use this hour to figure out some non-existant escape. "
    t "Use it to find your peace. Most of the guys i used to work with would kill to know it’s their final hour on earth, rather than have it sneak up on them."
    t "You’ve got one last opportunity here. Use it wisely."
    p "... Understood. Got it."
    t "Good. See you about in about an hour."
    p "Oh you’ll see me, alright."
    t "What was that?"
    p "Nothing, commander. See you in an hour."
    p ". . ."
    p ". . ."
    p "Welp, let’s get out of here. No way i’m dying today."
    p "My horoscope mentioned nothing about it"
    p "So, i basically have two options."
    p "I need to either find an escape route for myself, or barring that, find a way to convince those wonderful people in there that i should go in the copter instead."
    p "Possibly in place of Adrian."
    p "Stupid receptionist. Expects me to laugh at his jokes every morning."
    p "So, let's find me some incriminating evidence to pass the role of bait onto someone else. Shouldn’t be too difficult."
    show mono empty
    ">>> Explore the Administration building to find \[EVIDENCE\] to switch with another passenger.\n>>> Gather \[STUFF\] to solve problems that you may encounter.{fast}"
    play music "FTV-A.wav"
    $ prog = 2
    $ location = 3
    jump forceroomrefresh
    jump investistart


label check_reception_1: #photo
    #!!checking three times is kind of meh, need to fix
    if desk_check == 0:
        p "Adrian’s desk is here. God he ticks me off."
        p "It’s not so much his stupid face as it is the eyes, nose, nose and ears that belong on it"
        p "His voice also gets to me."
        p "It’s kind of peppy. Full of the joy of every morning we have to go to work."
        p "Doesn’t he know that people are supposed to hate work."
        p "What sitcoms did he spend his life watching?"
        p "What else is on here?"
        $ desk_check = 1
        jump investistart
    if desk_check == 1:
        p "Maybe i can find some incriminating evidence."
        p "If i make the others hate adrian more than they hate me, they’ll be more willing to swap us around on the helicopter."
        p "I see no moral quanries with this plan. Onwards."
        $ desk_check = 2
        jump investistart
    if desk_check == 2:
        p "I see no papers containing a confession of any wrong doings on Adrian’s part."
        p "He must have them stored away in his secret evil vault or something."
        p "I probably won’t have time to locate that."
        p "But what’s this?"
        p "A photo of his wife and kids."
        p "A personal item? Just out of sight of anyone coming by, as if to hide his crimes against the company."
        p "I think i might have to take this."
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_photo = True
        $ evi_count += 1
        jump evi_tally

label check_reception_2: #filing cabinet
    if not filingCabinetOpen:
        p "Yup. that is one locked filing cabinet."
        p "Not getting in there anytime soon."
        p "Certain not with any tools."
        p "That i might happen to find."
        p "Certainly not a crowbar or anything."
        $ interacting_with = "check_reception_2"
        $ req = ["crowbar","grenade", "fuelcan"]
        jump stuff_prompt
        label .req1:  
            p "Huh, whaddya know."
            p "This locker was-"
            p "This locker-"
            p "Hold on."
            $ filingCabinetOpen = True
            p "This filing cabinet was open the entire time."
            p "And what's this?"
            p "Tickets?"
            p "For some kind of personal event."
            p "Oh, Adrian."
            p "You should not be using the company printer for this kind of thing."
            p "Methinks this could work against you in a court of your peers."
            show screen sc_evidence_pane
            $ ev_bo = True
            $ have_printout = True
            $ evi_count += 1
            jump evi_tally
        label .req2:
            jump play_with_grenade
        label .req3:
            p "This would definitely work on the filing canibet."
            p "Metal is known for being a flammable lubricant after all."
            p "It's practically famous for it."
            p "My concern would be for all the paper inside."
            p "If i used the fuelcan now..."
            p "There wouldn't be enough to use on any of the paper inside."
            p "Something else..."
            jump investistart
    else:
        p "The Cabinet has been searched and returned back to its original state."
        jump investistart

label check_reception_3:
    if receptionDoorsCheck == 0:
        p "A beautiful garden... erm... front entryway thing."
        p "You know, the things that they have in front of businessey buildings"
        p "With grass and seats and fountains."
        p "To make the corporate world seem more in tune with nature."
        p "They probably have a term. I should ask somebody."
        p "It feels like it’s one of those things that everyone sort of knows, but it escapes your mind when you’re trying to think of it."
        p "But yeah, basically one of those."
        $ lookOutsideReception = True
        p "Oh, and there are four velociraptors on the lawn parts."
        #!!Fix colouring issue
        $ lookOutsideReception = False
        $ receptionDoorsCheck = 1
        jump investistart

    if receptionDoorsCheck == 1:
        p "Well, they’ve stopped scratching at the force field now."
        p "They’ve probably realised that bone nails aren’t going to do a thing against magical electrical barriers."
        p "Though luckily for them they won’t have to worry about that for much longer."
        p "God they look stupid."
        p "We’ll have historically accurate dinosaurs. Our park will be ‘more correct’."
        p "Who wants feathers on a velociraptor?"
        p "Ruins the brutal mystique."
        p "I’m certain that’s what Todd was thinking as they were eating him."
        p "Cretasious corners."
        p "Yep, that’s the name of the park"
        p "I get the feeling Triassic Tark would have just been too obvious."
        p "Richard Hammand would have definitely come swooping down on his Pteradactyl if we had done that."
        p "This is just enough off the mark though."
        p "It uses trademark theft juuuuust right."
        $ receptionDoorsCheck = 2
        jump investistart

    #if westTowerQuest == 1:
        p "So, getting to the Tower and back will get Helen to swap me ou with Adrian."
        p "That’s definitely what i heard her say."
        p "But, not only are they’re Raptors and a five hundred meter heavy jog involved, but also that pesky force field."
        p "I won’t be able to get through that just as much as those raptors can’t get in."
        p "I’m going to need to find a way around it."
        $ westTowerQuest = 2
        jump investistart

    if receptionDoorsCheck == 2:
        p "What's that, boy?"
        r "..."
        p "You want me to try an item on you?"
        p "Well sure, why not?"
        $ interacting_with = "check_reception_3"
        $ req = ["ak47", "grenade", "hammer"]
        jump stuff_prompt
        label .req1:  
            p "Wait."
            p "Thinking about it..."
            p "Rationally and logically of course."
            p "RatioLogically, you could say."
            p "What if i were touse this gun"
            p "To make the bullets located in the clip of the gun"
            p "Travel really fast."
            p "Into the raptor."
            p "Why that’s just crazy enough to work."
            p "I mean, there’s more than one raptor, but if i start with this one."
            p "And work my way up."
            p "Or across i guess."
            p "Unless some are on a hill."
            p "Then the bullets could deal with the raptors for me."
            p "Yeah."
            p "YEAH!"
            p "Let’s do this."
            p "Now. I’ve never used a gun before."
            p "But i have played plenty of videogames."
            p "But i’m not stupid enough to think that gameplay transitions perfectly into reality."
            p "It will only mostly transition."
            p "So, there should be a safety on the gun."
            p "Make sure that’s turned off."
            p "Don’t wantthe raptors to be safe now. Do we?"
            p "Ha ha ha."
            p "Next. Make sure the clips in."
            p "Yep. That’s definitely a clip containing bullets."
            p "Then... i think i need to cock the gun."
            p "Movies do that all the time right?"
            p "But sometimes they don’t."
            p "Does a gun always need cocking."
            p "Well, i’ll guess i’ll just cock it anyway."
            p "Then it;ll be doubly loaded."
            p "Then next i guess i just point and shoot"
            n "BANGBANGBANGBANG"
            #!!(scene o raptor looking from outside the force field, completely unhardmed, from a position that makes it clearly Paul is on the floor. Dying.)"
            p "So... something went wrong."
            p "Painfully wrong in fact."
            p "Oh this hurts so much."
            p "Not sure what it cold have been."
            p "Unless bullets can’t travel thrugh the force field."
            p "Video games may have failed me this time."
            p "No. It got be video games fault i have a gun. That’s just passing the blame."
            p "Well, with nay luck someone wold have heard the gunshot and be coming to help me out."
            p "I’m sure tat’s a thing that’s about to happen."
            p "You just wait there, mister Raptor. You’ll get your commupance soon."
            $ route = _("2/16: My brain has bullets in it.")
            $ persistent.end_02 = True
            jump endcard
        label .req2:
            jump play_with_grenade
        label .req3:
            p "Ah ha."
            p "Now scientifically accurate raptor, the shoe is on the other foot."
            p "And the hammer is in my hands."
            p "This is the exact combination of events that lead to your demise."
            p "Take this!"
            n "THE HAMMER USELESSLY BOUNCES OFF THE FORCEFIELD."
            P "aH."
            P "rIGHT."
            P "lET'S TRY SOMETHING ELSE, sHALL WE?"
            jump investistart

## corridor ##
label check_corridor_1:
    if corridorCheck1 == 0:
        p "Nothing special here. Just the corridor to the upstairs."
        p "I mean, i still say it’s the perfect place for a little indoor baseball r bowling."
        p "But the othrs disagree."
        p "Something about projectiles in a small corridor and the frajility of the human skull."
        p "It’s not my fault they hire cleaning ladies."
        p "And of course the top of stairs is where you should place the pins. "
        p "The balls meant to roll down into the gutter after it’s done its job."
        p "This corridor’s kind of slopey anyway.. It’s like it was made for this."
        $ corridorCheck1 = 1
        jump investistart
    if corridorCheck1 == 1:
        p "Seriously. It's just a bunch of boring messages."
        p "Stuff like Jenny's woodworking club and keeping the corridor clean."
        p "A fire extinguisher safety notice and a reminder that we work on a site with living dinosaurs."
        p "None of it's exactly relevant."
        jump investistart

label check_corridor_2:
    p "Oh, what's this doing here?"
    p "Todd told me to take that to the oily rags room."
    p "I must have left it here randomly for no reason."
    p "Though i don't recall doing so."
    p "Or spreading half the contents of the can everywhere."
    p "How strange."
    p "..."
    p "Oh well, nothing to do but take this with me."
    p "I'm sure i'll get back to the oily rags room at some point."
    p "Just as soon as i figure out where that is."
    show screen sc_stuff_pane
    $ ev_bo = False
    $ have_fuelcan = True
    jump investistart

label check_corridor_3:
    p "A standard issue fire extinguisher."
    p "This one’s the electrical fire one."
    p "So it’s a cloud of crap rather than foam or water."
    p "No need to take this with me."
    p "Normally when i start fires other people sort it out for me."
    p "Plus it’s heavy."
    p "I should only get this if it’s absolutely necessary."
    jump investistart #fire extinguisher needed!!

## ceo ##

label check_ceo_1:
    if not globeSmashed:
        p "It's the Entire World."
        p "Or some kind of model of it anyway."
        p "Perfect for standing over and imagining yourself like a giant."
        p "Or proving that Uruguay doesn't really exist."
        p "... You know, the world always has been mean to me."
        p "What has it really given me."
        p "Clearly not much, if people are actively planning to feed me to dinosaurs."
        p "I think i'm owed some retribution."
        p "But what item to use..."
        $ interacting_with = "check_ceo_1"
        $ req = ["hammer","grenade", "wadofcash"]
        jump stuff_prompt
        label .req1:
            p "Well, i suppose the best way to solve the iceberg crisis is to smash up the icebergs so they can't threaten anyone."
            p "Maybe if i die, people will see what i've done here and be inspired."
            p "YAAAAAHHH. YAAAAAHHHHHHHH"
            p "SMaSHY SMAsHy!"
            $ globeSmashed = True
            p "Phew, that felt good."
            p "Oh hey, and there's something in here."
            p "A piece of paper."
            p "Looks like a job contract."
            p "Assassination contract..."
            p "This contract is a legal agreement, enforceable by Assassin law..."
            p "To pay Tony Floyover the sum of..."
            p "To Assassinate Todd Raptorman..."
            p "in the name of John Hammond..."
            p "...signed Tony Flyover."
            p "Oh..."
            p "Oh wow..."
            p "I guess this IS actual evidence."
            p "I better get this over to the group."
            p "Wait, i'll probably need proof he got paid or something as well."
            p "Some kind of crimson liquid currency or something."
            show screen sc_evidence_pane
            $ ev_bo = True
            $ have_contract = True
            $ evi_count += 1
            jump evi_tally
        label .req2:
            jump play_with_grenade
        label .req3:
            p "The entire world won't accept my bribe."
            p "I mean, that just makes sense."
            p "The world has, like, a hudnred people in it."
            p "That's less than a dollar each."
            p "Totally not worth it."
            p "Geez, stupid. Think about it for a change."
            jump investistart
    else:
        p "Yup."
        p "Definitely no Uruguay on here."
        p "That Gypsy was definitely wrong."
        jump investistart#globe

label check_ceo_2:
    if checkCEO2 == 0:
        p "This was the Boss’s office."
        p "It still is, technically."
        p "Were i to throw his body in here, he would technically be doing just as much work as he were when he was alive."
        p "I know i shouldn’t gripe. It was him who got me this job."
        p "Leaving me trapped here with a bunch of predators who are intent in seeing my flesh flayed from my bones."
        p "Not to mention the whole raptor problem."
        $ checkCEO2 = 1
        jump investistart #certificate rewrite!!
    if checkCEO2 == 1:
        p "Todd's diploma."
        p "His father owned the University, so he had to work twice as hard to get it."
        p "I'd hate to have to work under my dad."
        p "No doubt he would scrutinise and critcise every single action Todd took."
        p "Still, it paid off for him."
        p "Graduated first class honours and valedictorian."
        p "Sometimes you need to force your child to work hard."
        $ checkCEO2 = 2
        jump investistart
    if checkCEO2 == 2:
        p "I never got a diploma."
        p "And out of the two of us, i'm the one who remains uneaten."
        p "Suck on that, education system."
        jump investistart

label check_ceo_3: #CEO Desk
    p "Now this is a desk like what i want to have."
    p "It’s shiny, and it’s wood."
    p "... and it’s shiny."
    p "That proper kind of shine. Not the type that gets scratched off after a month of use."
    p "And there's a drawer."
    p "A sort of Dead Man's drawer."
    p "Let's see what's in here."
    $ showIDCard = True
    p "Huh. It's Todd's ID card."
    p "It looks kind of odd."
    p "Oh wait. It's just upside down."
    p "Yup. There's ol' Todd."
    p "Looking completely normaly and boring as ever."
    $ showIDCard = False
    p "Well i guess i should keep this."
    p "I'll probably need to hand it to his father at some point."
    show screen sc_stuff_pane
    $ ev_bo = False
    $ have_idcard = True
    jump investistart

label check_ceo_4:
    if not have_adrianID:
        p "It is a Cup Board."
        p "A long board of wood, specifcally designed to hold cups."
        p "An ingenious invention created in 2002 that prevent many spillages around the house."
        p "This is one of the newer fancier ones that also has storage underneath it."
        p "Let's have a look."
        p "Huh."
        $ showAdrianID = True
        p "It's Adrian's ID card."
        p "If i recall Todd took it off him as a prank."
        p "It was hilarious and fully deserved."
        $ showAdrianID = False
        p "Well, i'm sure i can used this for something."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_adrianID = True
        jump investistart
    else:
        p "The Cup Board contains no other items."
        p "If i come across some cups, i can equip them to the Cup Board."
        p "Here's hoping."
        jump investistart

label check_ceo_5: #raptor outside needs something!!
    p "Oh."
    p "Hello there."
    p "I'm just going to leave you alone."
    p "At least in the demo version of this game."
    jump investistart

label check_ceo_6:
    if not have_matchbox:
        p "A box of matches."
        p "Perfectly safe for me to have."
        p "I remember Todd himsefl saying:"
        p "Paul, i wish i could burn this place to the ground."
        p "And i fully plan to one day."
        p "Just as soon as the insurance is all sorted out."
        p "Don't tell anyone."
        p "Great guy. Shame about the raptor thing."
        p "Anyway, i'm sure he won't miss them."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_matchbox = True
        jump investistart
    else:
        p "I only really need one."
        p "I am, after all, an expert with matches."
        p "Having played with them for so long."
        jump investistart


## bunks ##

label check_bunks_1:
    if not have_wadofcash:
        p "This is Tony’s bunk box."
        p "We each have one, though they don’t really get used."
        p "It appears to have some kind of arcane spell placed upon it, preventing me access."
        p "If it were to cfind a counter spell, i could probably remove it"
        $ interacting_with = "check_bunks_1"
        $ req = ["crowbar","grenade", "wadofcash"]
        jump stuff_prompt
        label .req1: 
            $ tonyChestOpen  = True
            p "Using my honed magic skills, which i have always had, i cast crowbar on Tony’s bunk box, revealing the contents of his chest."
            p "But what do i find here?"
            #show bloody cash!!
            p "A wad of cash with bloodstains on it."
            p "..."
            p "That's certainly interesting."
            p "I wonder what this Blood covered money is all about."
            p "Probably something dastardly."
            p "I should keep it."
            p "You know... for Evidence."
            p "Evidence..."
            show screen sc_evidence_pane
            $ ev_bo = True
            $ have_wadofcash = True
            $ evi_count += 1
            jump evi_tally
        label .req2:
            jump play_with_grenade
        label .req3:
            p "Wait but..."
            p "This should be what i find in the bunk."
            p "How does that work..."
    else:
        p "There's some helicopter magazines in here as well."
        p "Helicopters aren't as cool as motorcycles."
        p "So i have no interest."
        jump investistart#tony's chest

label check_bunks_5:
    if fuelApplied and matchApplied:
        p "Huh, a dictaphone"
        p "i Believe this is what people used to record their thoughts before we invented mind reading technology and mp3."
        p "this probably contains a lot of Jenny's innermost thoughts."
        p "And therefore probably evidence of all her wrongdoings."
        p "No time to listen to it now though."
        p "I shall do so when and if i show it to everyone else."
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_dictaphone = True
        $ evi_count += 1
        jump evi_tally#jenny's chest
    if not fuelApplied:    
        p "This is Jenny’s bunk box."
        p "I don’t dare look."
        p "It’s not that i’m assuming the contents of her bunk box is the source of the smell she carries around with her at all times."
        p "I’m just saying i’m not willing enough to take that risk."
        p "Now, if i had a way to break open the box from a distance, with no risk to the inside contents, then i might be willing to take a gander inside."
    if fuelApplied:
        p "Well, that's the lock all lubed up."
        p "It needs something else though..."
    $ interacting_with = "check_bunks_5"
    $ req = ["fuelcan","grenade", "matchbox"]
    jump stuff_prompt
    label .req1: 
        if fuelApplied:
            p "Well, that didn't help loosen the lock."
            p "But maybe adding something more to this fuel will help."
            p "It needs a spark."
            p "A flash, a strike."
            p "An ignition..."
            p "It needs a match okay?"
            p "Just use the match."
            p "Geez."
            jump investistart
        if not fuelApplied:
            p "Maybe i can use the fuel in this can to lubricate the lock."
            p "Which will almost certainly help in prying it open."
            p "Yep. That is how locks works."
            p "I'll just- Whoops-"
            $ fuelApplied = True
            p "Well... more is less."
            p "As they say."
            jump investistart
    label .req2:
        jump play_with_grenade
    label .req3:
        if not fuelApplied:
            p "Ah yes."
            p "I could use the match to pick the lock."
            p "Yay. Oh..."
            p "But it's not lubricated enough to fit in."
            p "Not even worth trying."
            p "I need something to lubricate it."
            jump investistart
        if fuelApplied:
            p "Wait a second."
            p "Is this reasonable?"
            p "Well i probably won't find a lock pick around here."
            p "But i'm pretty sure i can lockpick using any straight object."
            p "It is at least worth a reasonable try."
            $ matchApplied = True
            p "..."
            p "Mmmm’yep"
            p "That sure was a lot fire for about a second."
            p "It kind of smells."
            p "..."
            p "I don’t think the source of the smell was in here."
            p "I mean, the fire would have burnt it out long ago if that was the case."
            p "..."
            p "Maybe Jenny herself is the source of the smell."
            p "What's in here?"
            jump investistart



label check_bunks_3:
    if not have_hammer:
        p "This is Todd's Teddy bear."
        p "His name is Nixon, and he is a friend to all."
        p "I have often requested that Todd allow me to sleep with Nixon some nights."
        p "But he said that some friendships are too deep to share with peons."
        p "It was weird that he referred to his bear as a peon."
        p "But i felt really close to him that night."
        p "So i didn't need the Teddy bear after all."
        p "Maybe next time, Nixon."
        p "Inside Nixon is a hammer."
        p "It is important you store that which is most important to you inside a bear named after the 37th President of the United States."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_hammer = True
        jump investistart
    elif matchApplied:
        p "Teddy Nixon will remain safe here."
        p "In this room once filled with fire."
        jump investistart
    else:
        p "Teddy Nixon will remain safe here."
        jump investistart#todd's teddy

label check_bunks_4:
    if checkBunks4 == 0:
        p "This is where we all sleep together as one big happy family."
        p "Well, i say that."
        p "The boss got me my own private room over in the west tower."
        p "It was nice of my dad to arrange that with him."
        p "Everyone gets a chest containing their stuff."
        p "My bunk is technically the one at the back."
        p "I come him occasionally for an afternoon nap."
        p "Though i took yesterday’s afternoon nap on Adrian’s bunk."
        p "It was hot so i was sweaty. Didn’t want to ruin my mattress."
        p "The day before that i slept on Todd’s bunk."
        p "I feel less guilty about that now, but only by comparison,"
        $ checkBunks4 = 1
        jump investistart
    if checkBunks4 == 1:
        p "Adrian has left his Bunk box open like a pitiful loser with no notion of mystery."
        p "In it is a towel, several pairs of socks, some stationary and a book of fraudulent tax claims he has made against the state."
        p "All useless to me."
        p "So useless they do not even get an art asset drawn for their close up."
        p "So it's just me talking again."
        jump investistart#adrian's chest

## toilet ##
label check_toilet_1:
    #mirror and sink i guess
    p "It’s my home away from home."
    p "Well, away from my desk anyway."
    p "Technically the whole building is my home."
    p "It’s the place where i spend a lot of my time basically."
    p "I can gather my thoughts. Take stock of things. Make revenge plans."
    p "Adrian will pay for his crimes."
    p "I can’t imagine i’ll find anything of use here."
    jump investistart

label check_toilet_2:
    #actual toilet
    p "Jenny has done unspeakable things here."
    p "But we are all aware of this transgression."
    p "So there’s nothing i could find here that could be used against her."
    p "Also, what would i be bringing from here to use against her."
    p "Maybe we could fling our poop at the raptors."
    p "Primates against large turkeys?"
    p "Yeah. That could work."
    p "I don’t need to go though."
    jump investistart

label check_toilet_3:
    # crowbar item pickup
    if not have_crowbar:
        p "Jammed behind the toilet pipe is a crowbar."
        p "There's also some note written in an arcane language."
        p "I can speak arcane language, but i'm not being paid to do that."
        p "It's very important i only do the job i am paid for."
        p "My father told me that on the day he left my mother."
        p "Anyway. I'll be taking this."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_crowbar = True
        jump investistart
    else:
        p "The pipe has started leaking for some reason."
        p "It is also not my job to notice this."
        jump investistart    
#need toilet itmes, puzzle

## staffroom ##
label check_staffroom_1:
    if not have_raptorclaw:
        p "This appears to be Helen's Containment box."
        p "For containing secreative things."
        p "Don't know what it's doing in the staff room like this."
        p "Almost like someone didn't plan their art assets properly and began to run out of time and so made something up."
        p "Irregardless! It must contain evidence of wrong doing by Helen."
        p "But i need some manner of getting into it."
        $ interacting_with = "check_staffroom_1"
        $ req = ["crowbar","idcard", "grenade"]
        jump stuff_prompt
        label .req1:
            p "Hhhmmm, a valiant effort."
            p "But there's nothing really to crow the bar into."
            p "There's this card scanner. I could probably get some torque on that."
            p "Torque is a funny word and i know exactly what it means."
            p "What was i doing again?"
            p "Whatever it is, it doesn't involve this crowbar."
            jump investistart
        label .req2:
            p "As CEO, Todd had access to everything."
            p "NOW HE HAS ACCESS ONLY TO DEATH."
            p "I'm sure he's doing fine in the underworld."
            p "Oh, it worked. The container opened."
            p "Strange, felt like there should be more destruction."
            p "Anyway, there's some raptor claw in here."
            p "Probably for an illegitimate science experiement from the mad scientist known only as Helen Smithson."
            p "I will take this for evidence."
            p "Like any good detective would."
            show screen sc_evidence_pane
            $ ev_bo = True
            $ have_raptorclaw = True
            $ evi_count += 1
            jump evi_tally
        label .req3:
            jump play_with_grenade
    jump investistart
    if have_raptorclaw:
        p "The Containment box now contains nothing."
        p "As it should be when the name of the game is to take anything that's not bolted down."
        jump investistart       

label check_staffroom_2:
    if not have_research:
        p "What's this on the floor?"
        #!!show journal in top right
        p "Oh, it appears to be a Research Journal from Helen, the scientist."
        p "With a qick cursory glance, i can see that it definitely contains evidence of Helen's wrong-doing."
        p "This is definitely a good start."
        p "Lucky i found it just lying on the floor like that."
        p "Yup. Some hard-boiled detective work was done here today."
        p "Yessir, not lazy at all."
        p "..."
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_research = True
        $ evi_count += 1
        jump evi_tally

label check_staffroom_3:
    if not have_blankPaper:
        p "Hey, some spare paper."
        p "This is always good for me to collect."
        p "For a vairety of reasons."
        p "For one, to add to the pile of paper that i've been collecting in my office."
        p "For two,"
        p "..."
        p "There's probably a reason i'm doing this."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_blankPaper = True
        jump investistart

## securityroom ##
label check_securityroom_1:
    if not monitorCheckStop:
        p "The Security Office."
        p "This is Jenny’s workplace, hence the smell."
        p "I’d rather spend as little time here as possible, but there might be something i can use here to get people to stop liking her."
        p "Hey, it’s the security monitor for the office area."
        p "Those four looks like ants from in here."
        p "Hey, i can listen into them if i press this."
        $ monitorCheck = True
        a "Oh god. We’re all going to die here, aren’t we? We’re all going to die here."
        j "Calm down, Adrian. We can do this."
        a "What? No we can’t. We’re just deluding ourselves."
        a "Getting to the helicopter? You realise if even one of those things opts not to chase Paul we’re done for."
        a "All it’ll needs is to get Tony once. Even if he survives he won’t be flying us out of here."
        t "Hey. I’m not going to let that happen."
        a "Is your skin made out of dinosaur-proof flesh, or are you just as edible as the rest of us."
        j "Calm it, boy. Where will panicking get you."
        a "Oh. Where’s does being stoic get me? Maimed. Devoured. It’ll be better for me to just jump off the balcony now."
        h "Knock yourself out."
        a "I... What?"
        h "Throw yourself off the balcony. It’ll distract the raptors for us. They’ll go round to feast on your body, and we can all get out."
        a "Well... i mean."
        h "Paul as well."
        a "Right. Okay. I’m sorry. I’m just terrified, and my wife has no idea and... I just needed to vent."
        h "I know."
        a "..."
        h "Success is never a guarantee in general. But failure is the default result of inaction."
        h "Do nothing, and you’ll just die, no matter how long it takes."
        a "Right. You’re right. I’ve just got to have hope."
        h "No. You’ve just got to run fast."
        $ monitorCheck = False
        $ monitorCheckStop = True
        p "..."
        p "Ha. Adrian is such a loser."
        jump investistart

    if monitorCheckStop:
        p "They're just milling around now."
        p "So unproductive."
        jump investistart

label check_securityroom_2:
    if securityCabinetClosed:
        p "Some kind of locked cabinet thingy."
        p "HHmmm no sign of a key."
        p "Or a keyhole."
        p "Or any kind of clear asset that will allow me to open it."
        p "Hhhhmmmmmmmmmmmm."
        $ interacting_with = "check_securityroom_2"
        $ req = ["crowbar", "grenade", "hammer"]
        jump stuff_prompt
        label .req1: 
            $ securityCabinetClosed = False
            p "Ah! There we go."
            p "It turns out the crowbar was the friends we made along the way."
            p "Or something like that."
            p "Now, let's have a look."
            jump investistart
        label .req2:
            jump play_with_grenade
        label .req3:
                p "If i had a hammer..."
                p "Oh wait, i do have a hammer."
                $ securityCabinetClosed = False
                p "Well, that solves all of my problems."
                p "Well, not all of them, but..."
                p "You know. This problem."
                p "The lockers container problem."
                p "Look. LEt's just look. Okay?"
                jump investistart
    if not securityCabinetClosed and not have_ak47:
        p "Oh!"
        p "Oh ho ho."
        p "Very nice."
        p "Very nice indeed."
        p "This is a perfect storage cloest."
        p "I could store all manner of things in here."
        p "It would be perfect for my collection of motorcycle magazines."
        p "I just need to get these other things out of here first."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_ak47 = True
        $ have_grenade = True
        $ evi_count += 1
        p "Thinking about it."
        p "Why would Jenny have a grenade."
        p "Oh, for nefarious purposes of course."
        p "No doubt that this was intended for nothing less than absolute villany."
        p "Oh i am onto you, Jenny."
        show screen sc_evidence_pane
        $ ev_bo = True
        jump evi_tally
    if not securityCabinetClosed and have_ak47:
        p "Excellent. All that remains is to collect my motorstyle magazines from the West Tower."
        p "..."
        p "I suppose that will have to wait."

label check_securityroom_3:
    if have_adrianID and have_blankPaper and have_idcard:
        p "Hey, thinking about it."
        p "Not that i have some paper and these ID cards."
        p "Maybe i could go beyond simply finding evidence."
        p "Maybe i could go into the business of making evidence."
        p "I've never much been involved in the law before."
        p "Well, save for all those chicken smuggling arrests that kept happening."
        p "But that's why Uncle Ernie got that job as a Judge."
        p "Let's see what i can do."
        $ securityPuzzleOpen = True
        jump investistart
    elif not viewSecurityPanel:
        p "Oh, i know this one."
        p "This is the ID log reports systems."
        p "It shows all ID usage within the park."
        p "Who opened what and what not."
        p "Me and Todd used to come in here to alter logs for a laugh."
        p "Make it look like employees weren't in their designated areas when they should have been."
        p "It was funny."
        p "Though thinking about it, i never did see any of those staff members again after Todd did that."
        p "Weird."
        p "Anyway, useless to me i suppose."
        p "Though with the right tools this could make some interesting things happen."
        $ viewSecurityPanel = True
        jump investistart
    else:
        p "Still useless to me."
        p "I'd probably need some ID cards to make something happen with it."

label check_securityroom_5:
    p "This is the log system."
    p "The mere presence of Todd's card is enough to put it into Edit mode."
    p "So i can apparently make changes."
    p "Let's see. To make changes, simply slide the dials, press the sliders..."
    p "honk the buttons and twiddle the switches in the order just stated."
    p "This will change the current log files to the nearest non-Todd ID."
    p "Once complete, flick the chicken to receive the printout."
    p "Seems easy enough."
    # need a way to escape the puzzle
    jump investistart

label check_securityroom_6:
    if currentPuzzleState == 1:
        p "Okay then..."
        $ currentPuzzleState = 2
        jump investistart
    else:
        p "I don't think that's right."
        $ currentPuzzleState = 0
        $ securityPuzzleOpen = True
        jump investistart

label check_securityroom_7:
    if currentPuzzleState == 0:
        p "Mmmm hmmm..."
        $ currentPuzzleState = 1
        jump investistart
    else:
        p "I don't think that's right."
        $ currentPuzzleState = 0
        $ securityPuzzleOpen = True
        jump investistart

label check_securityroom_8:
    if currentPuzzleState == 3:
        p "Right... Ok..."
        $ currentPuzzleState = 4
        jump investistart
    else:
        p "I don't think that's right."
        $ currentPuzzleState = 0
        $ securityPuzzleOpen = True
        jump investistart

label check_securityroom_9:
    if currentPuzzleState == 2:
        p "Yeah... i think that's it."
        $ currentPuzzleState = 3
        jump investistart
    else:
        p "I don't think that's right."
        $ currentPuzzleState = 0
        $ securityPuzzleOpen = True
        jump investistart

label check_securityroom_10:
    if currentPuzzleState == 4:
        p "So i should just need to push this..."
        $ currentPuzzleState = 5
        $ adrianAccused = True
        p "Oh, it worked."
        p "Excellent. I knew i'd get it right."
        p "Oh, and what's this?"
        p "A print out of the logs, showing that it was in fact Adrian that opened up the Raptor gates."
        p "All this time i thought it was Paul."
        p "Because i am Paul, and I opened the gates."
        p "But this shows that i am wrong and i am Paul and not Adrian."
        p "And Adrian was the one who opened the gates."
        p "I am willing to admit my mistakes."
        p "Let's go see if Adrian would as well."
        $ securityPuzzleOpen = False
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_fakePaper1 = True
        $ have_fakePaper2 = True
        $ evi_count += 1
        $ evi_count += 1
        jump evi_tally
    else:
        p "I don't think that's right."
        $ currentPuzzleState = 0
        jump investistart


label play_with_grenade:
    if playWithGrenade == 0:
        p "This is a grenade i found in Jenny’s Security Room"
        p "I do not know why she has a grenade."
        p "I only know that her having a grenade will be used in exchange for me having a seat on the helicopter."
        p "As such, it is vital that i ensure this grenade is kept in one piece and not be used for anything."
        $ playWithGrenade = 1
        jump investistart
    if playWithGrenade == 1:
        p "I know itis tempting."
        p "To have a grenade is to want to use a grenade."
        p "Grenades have long been the chocolate bar of the armed forces."
        p "To have a grenade is to want to use the grenades."
        p "Vide games have taught me well for this."
        p "But i must hold back."
        $ playWithGrenade = 2
        jump investistart
    if playWithGrenade == 2:
        p "I must be rational about this."
        p "Ther are uses for this grenade. IT could even save the day."
        p "To use grenade on raptor could result in the deaths of many raptors"
        p "But it is unlikely that a single grenade could receive the result i am looking for."
        p "No. It is better to use the grenade as evidence"
        p "To ensure that another takes my place"
        p "On the Raptor killing grounds."
        $ playWithGrenade = 3
        jump investistart
    if playWithGrenade == 3:
        p "Though saying all that..."
        p "It is entirely possible that this grenade simply does not work."
        p "It is not out of the question that Jenny would have a dud grenade."
        p "She is know for her crazy irrational ways."
        p "And as an uncrazy unirrational person,"
        p "It is clear to me that relying on Jenny to have a working grenade is not something i can rely on."
        p "Perhaps testing is in order."
        $ playWithGrenade = 4
        jump investistart
    if playWithGrenade == 4:
        p "But a test alone wuld be difficult to do."
        p "For one, there is only one grenade."
        p "I would need some kind of second control grenade in order to compare it to."
        p "Also, to achieve statistical reigour, i would need about another thirty seven grenades."
        p "Also, i would probably still need this grenade afterwards."
        p "Which would be difficult if it is in pieces."
        $ playWithGrenade = 5
        jump investistart
    if playWithGrenade == 5:
        p "Perhaps the key here would be to stick to the hypothesis, rather than wade into the complexities of the practical."
        p "Being a man of science, which i now am, for i am doing experiments, i am smart enough to know that i can only test the grenade once. "
        p "And to attempt to test the grenade a second time would be impractical."
        p "And so, i should not do it."
        p "But whatis science, is not a traversal from the realm of the hypothetical, to a realm of practical."
        p "Would Louis Pastuer have not created pasta in his kitchen sink, if he spent so long worrying about the theoretical possibilities of bacteria?"
        p "Wold von Nueman have ever created the computer, if he had not stopped dating Turing first?"
        p "Clearly there is a time for action."
        p "But is that time now?"
        #" (picture of Paul holding grenade pin!!)"
        $ playWithGrenade = 6
        jump investistart
    if playWithGrenade == 6:
        p "Ulp. Never mind. The pin just fell out."
        p "Barely touched it and it slipped right through its..."
        p "its..."
        p "Ah, what’s the latch thing called. The thing that just popped off."
        p "I know it’s got a name."
        p "Is it just latch?"
        p "People probably do just call it a latch."
        p "Perhaps i should go ask someone."
        $ route = _("1/16: Boom boom boom boom")
        $ persistent.end_01 = True
        jump grenadeend