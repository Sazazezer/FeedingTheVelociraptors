## Alexandre
label check_offices_1:
    if prog == 0:
        t "So, it’s decided. Paul has to die."
        $ have_ak47 = True
        $ have_grenade = True
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
        t "Right… Sorry."
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
        if evi_count > 1:
            if fire_count == 4:
                a afear "Kid, do you, uh, smell something burning?"
                j jalarm "No idea what you're talking about!"
                j janger "Anyway, let's wrap this up."
                j jsmug "I know what you did, and I've got the evidence to prove it!"
            else:
                p "Well. I think i’m good to go."
                p "The crowd has gathered. Is it time for me to present the evidence that i have so painstakingly uncovered?"

            jump accusation
        else:
            if fire_count == 4:
                a afear "Uh, do you smell something burning?"
                j jalarm "Everything's fine! Everything's totally cool!"
                j "I just left my cake in the oven too long!"
                a adoubt "Wait, you're baking a cake? Like, right now? In this house of horrors?"
                j jalarm "It's for, uh, your birthday! We're having a surprise party!"
                j jneutral "Now if you'll excuse me, I've to go wrap the cake. I mean frost your presents."
            elif have_mask:
                alt "Jam appears wearing the horse mask."
                j jmask "NEIGH"
                a aalarm "OH GOD IT'S BACK TO oh wait it's just you again."
                a agrin "So, uh, you ready to untie me yet?"
                j jmask ". . ."
                j "neigh"
            elif have_gun:
                alt "Jam appears holding the gun."
                j jgun ". . . . . ."
                a afear ". . . Jam?"
                a "What exactly are you gonna do with that?"
                j jgun "Oh, nothing much."
                a afear "That thing's not loaded, right?"
                a "Right, Jam?"
                show mono empty
                a ". . . Jam?"
            else:
                a agrin "So, uh, you ready to untie me yet?"
                j janger ". . . . . . . . ."
                j jneutral "Nope."
    jump investistart

label temp_corridor:
    p "Well, this is a sticky little pickle i’ve gotten us into. How will i escape today?"
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
    p "… Understood. Got it."
    t "Good. See you about in about an hour."
    p "Oh you’ll see me, alright."
    t "What was that?"
    p "Nothing, commander. See you in an hour."
    $ tonyincorridor = False
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
    jump investistart

label check_reception_1: #desk
    #!!checking three times is kind of meh, need to fix
    if desk_check == 0:
        p "Adrian’s desk is here. God he ticks me off."
        p "It’s not so much his stupid face as it is the eyes, nose, nose and ears that belong on it"
        p "His voice also gets to me."
        p "It’s kind of peppy. Full of the joy of every morning we have to go to work."
        p "Doesn’t he know that people are supposed to hate work."
        p "What sitcoms did he spend his life watching?"
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
        $ req = ["crowbar,grenade"]
        jump stuff_prompt
        label .req1:  
            p "Huh, whaddya know."
            p "This locker was-"
            p "This locker-"
            p "Hold on."
            $ filingCabinetOpen = true
            #!!Add broken loker as 2b
            p "This filing cabinet was open the entire time."
            p "And what's this?"
            p "Tickets?"
            P "For some kind of personal event."
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
    else:
        p "The Cabinet has been searched and returned back to its original state."
        jump investistart
        #!!need broken cabinet image

label check_reception_3:
    if receptionDoorsCheck == 0:
        p "A beautiful garden… erm… front entryway thing."
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
        jump investistart

    if westTowerQuest == 1:
        p "So, getting to the Tower and back will get Helen to swap me ou with Adrian."
        p "That’s definitely what i heard her say."
        p "But, not only are they’re Raptors and a five hundred meter heavy jog involved, but also that pesky force field."
        p "I won’t be able to get through that just as much as those raptors can’t get in."
        p "I’m going to need to find a way around it."
        $ westTowerQuest = 2
        jump investistart

        $ interacting_with = "check_reception_2"
        $ req = ["ak47, grenade"]
        jump stuff_prompt
        label .req1:  
            p "Wait."
            p "Thinking about it…"
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
            p "Then… i think i need to cock the gun."
            p "Movies do that all the time right?"
            p "But sometimes they don’t."
            p "Does a gun always need cocking."
            p "Well, i’ll guess i’ll just cock it anyway."
            p "Then it;ll be doubly loaded."
            p "Then next i guess i just point and shoot"
            #!!BANGBANGBANGBANG"
            #!!(scene o raptor looking from outside the force field, completely unhardmed, from a position that makes it clearly Paul is on the floor. Dying.)"
            p "So… something went wrong."
            p "Painfully wrong in fact."
            p "Oh this hurts so much."
            p "Not sure what it cold have been."
            p "Unless bullets can’t travel thrugh the force field."
            p "Video games may have failed me this time."
            p "No. It got be video games fault i have a gun. That’s just passing the blame."
            p "Well, with nay luck someone wold have heard the gunshot and be coming to help me out."
            p "I’m sure tat’s a thing that’s about to happen."
            p "You just waitthere, mister Raptor. You’ll get your commupance soon."
        label .req2:
            jump play_with_grenade

## corridor ##
label check_corridor_1:
    p "Nothing special here. Just the corridor to the upstairs."
    p "I mean, i still say it’s the perfect place for a little indoor baseball r bowling."
    p "But the othrs disagree."
    p "Something about projectiles in a small corridor and the frajility of the human skull."
    p "It’s not my fault they hire cleaning ladies."
    p "And of course the top of stairs is where you should place the pins. "
    p "The balls meant to roll down into the gutter after it’s done its job."
    p "This corridor’s kind of slopey anyway.. It’s like it was made for this."
    jump investistart

label check_corridor_2:
    p "A standard issue fire extinguisher."
    p "This one’s the electrical fire one."
    p "So it’s a cloud of crap rather than foam or water."
    p "No need to take this with me."
    p "Normally when i start fires other people sort it out for me."
    p "Plus it’s heavy."
    p "I should only get this if it’s absolutely necessary."
    jump investistart


## ceo ##
label check_ceo_1:
    p "This was the Boss’s office."
    p "It still is, technically."
    p "Were i to throw his body in here, he would technically be doing just as much work as he were when he was alive."
    p "I know i shouldn’t gripe. It was him who got me this job."
    p "Leaving me trapped here with a bunch of predators who are intent in seeing my flesh flayed from my bones."
    p "Not to mention the whole raptor problem."
    jump investistart

label check_ceo_1: #CEO Desk
    p "Now this is a desk like what i want to have."
    p "It’s shiny, and it’s wood."
    p "… and it’s shiny."
    p "That proper kind of shine. Not the type that gets scratched off after a month of use."
    jump investistart

label check_ceo_2: #finding grenade
    jump investistart


## bunks ##
label check_bunks_1:
    p "This is where we all sleep together as one big happy family."
    p "Well, i say that."
    p "The boss got me my own private room over in the west tower."
    p "It was nice of my dad to arrange that with him."
    p "My bunk is technically the one at the back."
    p "I come him occasionally for an afternoon nap."
    p "Though i took yesterday’s afternoon nap on Adrian’s bunk."
    p "It was hot so i was sweaty. Didn’t want to ruin my mattress."
    p "The day before that i slept on Todd’s bunk."
    p "I feel less guilty about that now, but only by comparison,"
    jump investistart

label check_bunks_2:
    p "This is tony’s bunk box."
    p "We each have one, though they don’t really get used."
    p "It appears to have some kind of arcane spell placed upon it, preventing me access."
    p "If it were to cfind a counter spell, i could probably remove it"
    $ interacting_with = "check_reception_2"
    $ req = ["crowbar"]
    jump stuff_prompt
    label .req1:  
        p "Using my honed magic skills, which i have always had, i cast crowbar on Tony’s bunk box, revealing the contents of his chest."
        p "But what do i find here?!!"
        jump investistart

label check_bunks_3:
    p "Adrian has left his Bunk box open like a pitiful loser with no notion of mystery."
    p "In it is a towel, several pairs of socks, some stationary and a book of fraudulent tax claims he has made against the state."
    p "All useless to me."
    p "So useless they do not even get an art asset drawn for their close up."
    p "So it's just me talking again."
    jump investistart

label check_bunks_4:
    p "This is Jenny’s bunk box."
    p "I don’t dare look."
    p "It’s not that i’m assuming the contents of her bunk box is the source of the smell she carries around with her at all times."
    p "I’m just saying i’m not willing enough to take that risk."
    p "Now, if i had a way to break open the box from a distance, with no risk to the inside contents, then i might be willing to take a gander inside."
    $ interacting_with = "check_reception_2"
    $ req = ["crowbar"]
    jump stuff_prompt
    label .req1: 
        p "…"
        p "Mmmm’yep"
        p "That sure is fire."
        p "It kind of smells."
        p "…"
        p "I don’t think the source of the smell was in here."
        p "I mean, the fire would have burnt it out long ago if that was the case."
        p "…"
        p "Maybe Jenny herself is the source of the smell."
        jump investistart

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
#need toilet itmes, puzzle

## staffroom ##
label check_staffroom_1:
    if not used_mask:
        alt "The horrifying thing glowers down at Jam."
        j jterror "oh god what is that thing"
        j "why does it have so many eyes"
        j "oh god oh man oh god"

        $ interacting_with = "check_staffroom_1"
        $ req = ["mask","gun","book"]
        jump stuff_prompt

        label .req1:
            j jterror "Ri—right! Maybe I could use the mask!"
            j "If I just put it on . . ."
            j jmask ". . ."
            j "This isn't helping!"
            j jterror "Okay, maybe if I put the mask on it instead . . ."
            $ used_mask = True
            $ have_mask = False
            alt "Jam sticks the mask over the demon's head."
            j ". . ."
            j jdoubt ". . ."
            j janger ". . ."
            j "Wow, that's somehow exactly as terrible as it was before."
            j jneutral "Still, at least it's not any worse?"
            jump investistart
        label .req2:
            j jgun "Keep it together, Jam!"
            j "It's just a taxidermied model. All I need to do is take the gun, look that thing in the eyes, and—"
            j jterror "oh my god i'm gonna die"
            jump stuff_prompt
        label .req3:
            j jterror "If it's a demon, it probably got here by magic, so magic can send it back, right?"
            j jdoubt "Just got to find the right spell in this book . . ."
            j jalarm "Uh . . . centi, milli, micro, nano?"
            j jterror "oh god it's not working"
            jump stuff_prompt
    else:
        j jneutral ".{w} .{w} ."
        j "nope"
        jump investistart
label check_staffroom_2:
    if not used_mask:
        j jneutral "Oh, cool, a yardstick!"
        j "All I need to do is walk past that—"
        j jterror "—that demonic monstrosity holy crap it's going to eat me alive"
        jump investistart
    else:
        j jneutral "I sure am glad that I can walk past this absolute nightmare without any issues at all, ha ha."
        j "Yep, just gonna walk on over to pick up this yardstick while avoiding looking to my left at all costs. Totally cool!"
        j jdoubt "Wait a second . . ."
        j janger "This isn't a yard stick! It's all in centimeters and stuff!"
        j "What a waste of wood. Honestly, how are you even supposed to use that?"

        $ interacting_with = "check_staffroom_2"
        $ req = ["book","candle","gun"]
        jump stuff_prompt

        label .req1:
            j jgrim "Ugh. I suppose I did pick up that book on metric back in the securityroom."
            j janger "I g u e s s I could try and figure it out."
            j jthink "Hmmm . . ."
            j ". . . units of measurement . . . international standard . . ."
            j ". . . divisible by ten . . . something French or whatever . . ."
            j ". . . one kilometer is equal to 0.62 miles . . ."
            j jsurprise "Wow! I think I get it!"
            j jsmug "Of course, such instantaneous mastery is to be expected, seeing as I'm Jam, the world's greatest kid detective between the ages of 4 and 17 in the western half of Linn County."
            j "A prodigy like me eats newtons for breakfast."
            j jneutral ". . . well, fig newtons, anyway."
            show screen sc_stuff_pane
            $ ev_bo = False
            $ have_ruler = True
            jump investistart
        label .req2:
            j jthink "I suppose if I lit it on fire, it might make for a decent torch."
            j "Not that there's any arson I urgently need to commit right now, but I'll keep that in mind!"
            jump stuff_prompt
        label .req3:
            j jsurprise "Aha! Brilliant idea, Jam!"
            j jsmug "If I attach the revolver to the end of the stick, I can practically double my range!"
            j "The final boss won't even know what hit it."
            j jdoubt "There is going to be a final boss, isn't there?"
            j jgrim "Hmmm . . . Maybe there's a better way to use this."
            jump stuff_prompt
label check_staffroom_3:
    if not used_mask:
        j jterror "can't look at candle too busy trying not to get my soul sucked out through my teeth"
        jump investistart
    else:
        j jthink "Ha, ha, alright, well, now that the taxidermied demonic entity is out of the way, I can get back to what's really important here:"
        j jneutral "Pocketing everything within eyeshot that isn't nailed down!"
        j jsmug "Starting with this candle!"
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_candle = True
        j jneutral "Not actually sure I'm gonna need this, seeing as the house is pretty adequately lit already, but I'm not really opposed to the ability to light random things on fire either."
        jump investistart

## securityroom ##
label check_securityroom_1:
    p "The Security Office."
    p "This is Jenny’s workplace, hence the smell."
    p "I’d rather spend as little time here as possible, but there might be something i can use here to get people to stop liking her."
    jump investistart

label check_security_room_2:

    if monitorCheck = 0:
        p "Hey, it’s the security monitor for the office area."
        p "Those four looks like ants from in here."
        p "Hey, i can listen into them if i press this."
        $ monitorCheck = 1
    #switch to monitor
    if monitorCheck = 1:
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
        a "I… What?"
        h "Throw yourself off the balcony. It’ll distract the raptors for us. They’ll go round to feast on your body, and we can all get out."
        a "Well… i mean."
        h "Paul as well."
        a "Right. Okay. I’m sorry. I’m just terrified, and my wife has no idea and… I just needed to vent."
        h "I know."
        a "..."
        h "Success is never a guarantee in general. But failure is the default result of inaction."
        h "Do nothing, and you’ll just die, no matter how long it takes."
        a "Right. You’re right. I’ve just got to have hope."
        h "No. You’ve just got to run fast."
        #switch back
        p "..."
        p "Ha. Adrian is such a loser."
        $ monitorCheck = 2
    if monitorCheck = 2:
        p "They're just milling around now."
        p "So unproductive."
        jump investistart    

label play_with_grenade:
    if playWithGrenade = 0:
        p "This is a grenade i found in Jenny’s Bunk"
        p "I do not know why she has a grenade."
        p "I only know that her having a grenade will be used in exchange for me having a seat on the helicopter."
        p "As such, it is vital that i ensure this grenade is kept in one piece and not be used for anything."
        $ playWithGrenade = 1
        jump investistart
    if playWithGrenade = 0:
        p "I know itis tempting."
        p "To have a grenade is to want to use a grenade."
        p "Grenades have long been the chocolate bar of the armed forces."
        p "To have a grenade is to want to use the grenades."
        p "Vide games have taught me well for this."
        p "But i must hold back."
        $ playWithGrenade = 2
        jump investistart
    if playWithGrenade = 2:
        p "I must be rational about this."
        p "Ther are uses for this grenade. IT could even save the day."
        p "To use grenade on raptor could result in the deaths of many raptors"
        p "But it is unlikely that a single grenade could receive the result i am looking for."
        p "No. It is better to use the grenade as evidence"
        p "To ensure that another takes my place"
        p "On the Raptor killing grounds."
        $ playWithGrenade = 3
        jump investistart
    if playWithGrenade = 3:
        p "Though saying all that…"
        p "It is entirely possible that this grenade simply does not work."
        p "It is not out of the question that Jenny would have a dud grenade."
        p "She is know for her crazy irrational ways."
        p "And as an uncrazy unirrational person,"
        p "It is clear to me that relying on Jenny to have a working grenade is not something i can rely on."
        p "Perhaps testing is in order."
        $ playWithGrenade = 4
        jump investistart
    if playWithGrenade = 4:
        p "But a test alone wuld be difficult to do."
        p "For one, there is only one grenade."
        p "I would need some kind of second control grenade in order to compare it to."
        p "Also, to achieve statistical reigour, i would need about another thirty seven grenades."
        p "Also, i would probably still need this grenade afterwards."
        p "Which would be difficult if it is in pieces."
        $ playWithGrenade = 5
        jump investistart
    if playWithGrenade = 5:
        p "Perhaps the key here would be to stick to the hypothesis, rather than wade into the complexities of the practical."
        p "Being a man of science, which i now am, for i am doing experiments, i am smart enough to know that i can only test the grenade once. "
        p "And to attempt to test the grenade a second time would be impractical."
        p "And so, i should not do it."
        p "But whatis science, is not a traversal from the realm of the hypothetical, to a realm of practical."
        p "Would Louis Pastuer have not created pasta in his kitchen sink, if he spent so long worrying about the theoretical possibilities of bacteria?"
        p "Wold von Nueman have ever created the computer, if he had not stopped dating Turing first?"
        p "Clearly there is a time for action."
        p "But is that time now? (picture of Paul holding grenade pin!!)"
        $ playWithGrenade = 6
        jump investistart
    if playWithGrenade = 6:
        p "Ulp. Never mind. The pin just fell out."
        p "Barely touched it and it slipped right through its…"
        p "its…"
        p "Ah, what’s the latch thing called. The thing that just popped off."
        p "I know it’s got a name."
        p "Is it just latch?"
        p "People probably do just call it a latch."
        p "Perhaps i should go ask someone."
        jump grenadeend