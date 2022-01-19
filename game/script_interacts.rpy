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
                p "Alrighty, time to wrap this up."
                p "I know what you did, and I've got the evidence to prove it!"
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

label check_reception_1:
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
        jump investistart

label check_reception_2:
    p "Yup. that is one locked filing cabinet."
    p "Not getting in there anytime soon."
    p "Certain not with any tools."
    p "That i might happen to find."
    p "Certainly not a crowbar or anything."
    p "Though to speed up game testing, let's say i found a personal printout here, which incriminates Adrian for certain."
    show screen sc_evidence_pane
    $ ev_bo = True
    $ have_printout = True
    $ evi_count += 1
    jump investistart

label check_reception_3:
    if receptionDoorsCheck == 0:
        p "A beautiful garden… erm… front entryway thing."
        p "You know, the things that they have in front of businessey buildings"
        p "With grass and seats and fountains."
        p "To make the corporate world seem more in tune with nature."
        p "They probably have a term. I should ask somebody."
        p "It feels like it’s one of those things that everyone sort of knows, but it escapes your mind when you’re trying to think of it."
        p "But yeah, basically one of those."
        p "Oh, and there are four velociraptors on the lawn parts."
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


## corridor ##
label check_corridor_1:
    alt "The bust stares eerily at Jam."
    j jdoubt "Billy S. . . ."
    j jgrim "No idea who this chump is, but he's got some seriously creepy eyes."
    j "It's like they can follow you around the room."

    $ interacting_with = "check_corridor_1"
    $ req = ["gun","mask","key"]
    jump stuff_prompt

    label .req1:
        j jgun "Probably not the best idea."
        j jgun "But I mean, I can't say I'm not tempted."
        jump investistart
    label .req2:
        alt "Jam dons the horse mask."
        j jmask "Hey, you."
        j "Yeah, you there, Billy. You lookin' at me? Huh?"
        j "What's that? No? Yeah, I didn't think so!"
        j "Better watch yourself, punk. I've got my upsettingly detailed eye on you."
        jump investistart
    label .req3:
        j jthink "Maybe this statue's got some kinda secret mechanism in it?"
        j jsmug "And if that's the case, there must be a way to activate it."
        j jthink "Maybe if I use this key . . ."
        j jgrim "Kinda hard to fit it up his nose, though."
        jump investistart
label check_corridor_2:
    j jsurprise "Ooh, what's this? A mysterious letter?"
    j jsmug "I bet it's full of all kinds of dirt on Badmann!"
    show mono jthink
    "The concludent statement of Dee Kieller:"
    "As this rubescent haze essipates from abouts my consciousness, in most total clarity do I revisit those actions which over the preceding month I did peragitate."
    "This house—how it reeks of that most sanguinous humor! And so too my sullied, sullied hands, which did that humor spill!"
    "He and I thought ourselves bold, but that facade crumbled like ash before that timendous horror that from out mine floor did emerge."
    "To merely witness it rising from the circle would, itself, percuss the brain to insensibility."
    show mono jneutral
    "It is best not to think of such things."
    "The deed is done, and undone can it not be, yet these words assuage my woe little."
    "That vitessence which from mine friend I reapt that I might invoke the demon—how glad would I be to have it back, and the demon perlineated from this earth!"
    "I was mad, then. So too was he."
    show mono jgrim
    "And now, of him, only his lone mandible remains."
    "As for that demon, I have sealed its essence within the lawn statuary, and transpaled its corporeal form upon my harpooning gun."
    "Still does it stand, as though a corpus lifelorn."
    "But full well I know that comely Death desires as little to do with the demon as I."
    "And oh! the worms—the worms that out from its immaculate corpse do wriggle and breem!"
    "The worms!"
    "The WORMS!"
    "I am but a festering rind of cheese swollen to bursting with worms!"
    "Their bloodravenous susurrations churn the rancid milk of my soul!"
    "The writhing! The gnawing! The boundless hunger!"
    "Even now, I can feel their corpulent bodies crawling within my teeth{nw}"
    j janger "BORING!"
    j jdoubt "I could barely even read most of that."
    j jneutral "But whatever it said, I'm pretty sure it has nothing to do with the crimes that Badmann definitely committed here."
    jump investistart

label check_corridor_3:
    j jsurprise "A locked box!"
    j jsmug "Narrative convention dictates that it's gotta be full of treasure, or at least an important bit of evidence."
    j jthink "But how to open it . . ."

    $ interacting_with = "check_corridor_3"
    $ req = ["key","book","gun"]
    jump stuff_prompt

    label .req1:
        j jneutral "I guess a key would probably make the most sense."
        j ". . . and it's open!"
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_knife = True
        $ evi_count += 1
        j jalarm "A bloodstained knife!"
        j jthink "There's like a zero-percent chance this baby wasn't involved in some crime or another."
        j "Not really sure what crime, but I can work it out as I go."
        jump evi_tally
    label .req2:
        j jthink "Maybe—just maybe—this box is actually locked . . ."
        j jneutral ". . . in metric."
        j jthink "Let's see . . . If you carry the nine, and follow PEMDAS . . ."
        j ". . . . . ."
        j jgrim "Nope, still locked."
        j "Maybe if I tried radians . . ."
        jump stuff_prompt
    label .req3:
        j jgun "I could try unlocking it with the gun, I suppose."
        j jgrim "Though a bobby pin would be a lot easier to fit into the tumbler."
        jump stuff_prompt

## ceo ##
label check_ceo_1:
    j jsurprise "Why, who's that supremely graceful and astute supersleuth in the mirror?"
    j "Could it be . . ."
    j jsmug ". . . Jam, the world's greatest kid detective between the ages of 4 and 17 in the western half of Linn County?"
    j jneutral "Oh, I'm ever so busy solving crimes; I couldn't possibly stop to pose for the cover of the Nancy Drew Review."
    j jsmug "Okay, maybe just this once."

    $ interacting_with = "check_ceo_1"
    $ req = ["mask","book","gun"]
    jump stuff_prompt

    label .req1:
        j jneutral "Please, just a moment while I put on something more suitable."
        alt "Jam puts on the mask."
        j jmask ". {w}. {w}."
        j ". . . Why did I think this was a good idea?"
        jump investistart
    label .req2:
        j jthink "Maybe I should be holding a book, to showcase my thoughtful, meticulous side?"
        j "Just casually brushing up on the metric system, you know."
        j "Been measuring some Kelvins lately. Doin' some hec—some hecta—uh, heckometers."
        j "Why yes, I do use the 24-hour clock. How did you know?"
        jump investistart
    label .req3:
        j jgun "It's a dark and stormy night in the city, and a mysterious figure is prowling the streets with a gun in hand . . ."
        j "That's right . . ."
        j jsmug "Jam the world's greatest adult detective above the age of 18 in the western half of Linn County is on the case!"
        j jsurprise "Taller than two kids in a trenchcoat, and infinitely more capable of voting in state and federal elections!"
        j jsmug "And of course, legally allowed to say cusses."
        j jneutral "Sh . . ."
        j "Shi . . ."
        j "S . . .{w} on of a heck."
        j jgrim "Well, maybe give it 1–14 years . . ."
        jump investistart
label check_ceo_2:
    j jthink "Is there something in the tub?"
    j "Let's see . . ."
    show screen sc_stuff_pane
    $ ev_bo = False
    $ have_mask = True
    alt "Jam retrieves an upsettingly detailed horse mask from the tub."
    j jdoubt "Oh."
    j "Oh god."
    j "I don't want this."
    j "I don't think anyone has ever wanted this."
    jump investistart

label check_ceo_3:
    if have_jaw:
        j jdoubt "Pretty sure I don't need to be rummaging around in this trash fire again."
        jump investistart
    else:
        if trash_fire:
            j jdoubt "Well, that's pretty soundly on fire."
            j jsurprise "Ooh! And it looks like there's something in there after all!"
            j jgrim "Just gotta reach through the flames real quick and . . ."
            show screen sc_evidence_pane
            $ ev_bo = True
            $ have_jaw = True
            $ evi_count += 1
            j jsurprise "Got it!"
            j jdoubt "Oh."
            j janger "That . . . is definitely someone's jaw."
            j "What a lovely piece of evidence."
            j jdoubt "I think I'm gonna wash my hands now."
            jump evi_tally
        else:
            j jsurprise "If there's one thing I've learned from playing a copious amount of video games, it's that you always need to check the trash cans."
            j jneutral "You never know where someone might have hidden a secret treasure, or even an equippable item that heals one sixteenth of your maximum HP per turn!"
            j jgrim ". . . Okay, maybe one of those is slightly less useful than the other in this situation."
            j jdoubt "Still, even if there were something good in there, I can't say I'm super thrilled about reaching in and grabbing it."
            j "There are some pretty nasty-looking tissues wadded up in there . . ."

            $ interacting_with = "check_ceo_3"
            $ req = ["candle","ruler","key"]
            jump stuff_prompt

            label .req1:
                j jneutral "Good thing I have this handy candle already lit!"
                j "If there's a second thing I've learned from playing a copious amount of video games, it's that an adequate quantity of fire solves pretty much anything."
                alt "Jam lights the trash can on fire."
                $ trash_fire = True
                $ fire_count += 1
                jump fire_tally
            label .req2:
                j jneutral "Yeah, that's a great idea! I'll use my trusty meterstick and my newfound mastery of the metric arts to solve this puzzle!"
                j jthink "Let's see . . . factoring in the amperage, and rounding to three significant figures . . ."
                j "According to my calculations and measurements, this trash can is . . ."
                j janger ". . . absolutely disgusting."
                jump stuff_prompt
            label .req3:
                j jthink "I've got a bit of string in my backpack, and I've got this key."
                j "If there's something at the bottom of the trash can, maybe I could fish it out?"
                j jneutral "Alright, let's give it a shot."
                j ". . ."
                j jgrim "Hmmm . . . Nothing biting, huh?"
                j jdoubt "Ugh, and now the key is gross too . . ."
                jump stuff_prompt

## bunks ##
label check_bunks_1:
    if not have_gun:
        j jsurprise "Hey, that bedside table looks pretty promising."
        j jsmug "Bet there's some solid evidence in there."
        j jgrim "That, or another Gideon Bible . . ."
        j jthink "Let's see . . ."
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_gun = True
        j jgun "Lucky me! It's a revolver!"
        j "And it's still got five bullets loaded in it!"
        j "What a totally innocuous and normal item for an American teenager to find lying around the house."
        j jneutral "Ha, ha, totally normal."
    else:
        j jgrim "Yeah, I'm gonna have to pass on the Gideon Bible."
    jump investistart
label check_bunks_2:
    if summoning == 0:
        j jdoubt "That's got to be the most terribly drawn demonic summoning circle I've ever seen."
        j "Still pretty spooky, though."
        j jneutral "In terms of occultic likelihood to corrupt the youth and steal their souls for the devil, I'd rank it like five points above rock music, and just a smidge below Magic: The Gathering."

        $ interacting_with = "check_bunks_2"
        $ req = ["candle","mask","ruler"]
        jump stuff_prompt

        label .req1:
            j jthink "Maybe I could get in on a little of this demon-summoning action. Just need to put the candle in place and . . ."
            j jalarm "O mighty demons or whatever! Heed my call!"
            j "I dunno what your deal is, but I've got a pretty ripe soul to trade, if that's your thing."
            j jsurprise "It's all yours, as long as you can get me a bestselling series of beloved children's detective novels about my heroic exploits."
            j jsmug "And the Netflix adaptation had better last at least three seasons, or the deal's off."
            jump stuff_prompt
        label .req2:
            j jthink "I wonder if it's possible to commune with the demons."
            j jneutral "Only one way to find out . . ."
            j jmask "hey."
            j ". . . . . ."
            j "Actually, maybe this would be better for exorcising them . . ."
            jump stuff_prompt
        label .req3:
            j jgrim "Honestly, though, with a pentagram this poorly arranged, I doubt you could commune with the ghost of Colonel Sanders, let alone any proper demons."
            j jneutral "Good thing I've got this meterstick to help fix things up!"
            j jthink "An acute angle here . . .{w} a fallen angel here . . ."
            $ summoning += 1
            alt "Jam finishes correcting the summoning circle."
            j jneutral "And we're done!"
            j jsmug "Now then, let's see how it works."
            jump investistart
    elif summoning == 1:
        j jalarm "Demons of the afterrealm! I invoke thee!"
        j "Rise! Ascend! Materialize!"
        j "Come on out or whatever!"
        j jsurprise ". . . Uh, demons? Hello?"
        j "Is anybody there?"
        j "Can you hear me? Should I, like, invoke louder or—"
        $ summoning += 1
        $ fire_count += 1
        alt "The summoning circle bursts into flame."
        j ". . ."
        j jdoubt "Well, alrighty then."
        j "I guess that's a no?"
        jump fire_tally
    else:
        j jdoubt "I think I'm good on the whole demon-summoning thing for now, actually."
        jump investistart

label check_bunks_3a:
    ">>> The middle clown stares down with an expression of incalculable grief, his hands raised in supplication to an absent god."
    ">>> Jam boops him on the nose."
    if clown_code[0] == 0:
        $ clown_code[0] = 2
        ">>> There is a faint click."
    elif clown_code[1] == 0:
        $ clown_code[1] = 2
        ">>> The click is slightly louder this time."
    elif clown_code[2] == 0:
        $ clown_code[2] = 2
        jump check_bunks_3part4
    jump investistart
label check_bunks_3b:
    ">>> The right-hand clown smirks in the shadows. His bowtie weighs heavy with the sacred promise of a seltzer to the face."
    ">>> Jam boops him on the nose."
    if clown_code[0] == 0:
        $ clown_code[0] = 3
        ">>> There is a faint click."
    elif clown_code[1] == 0:
        $ clown_code[1] = 3
        ">>> The click is slightly louder this time."
    elif clown_code[2] == 0:
        $ clown_code[2] = 3
        jump check_bunks_3part4
    jump investistart
label check_bunks_3c:
    ">>> The left-hand clown barrels toward the viewer like the world's most exuberant freight train, the vector of his relentless advance a reminder of one's own impotence."
    ">>> Jam boops him on the nose."
    if clown_code[0] == 0:
        $ clown_code[0] = 1
        ">>> There is a faint click."
    elif clown_code[1] == 0:
        $ clown_code[1] = 1
        ">>> The click is slightly louder this time."
    elif clown_code[2] == 0:
        $ clown_code[2] = 1
        jump check_bunks_3part4
    jump investistart
label check_bunks_3part4:
    if clown_code == [1,3,2]:
        $ clown_down = True
        ">>> The painting opens to reveal a secret compartment!"
        jump investistart
    else:
        $ clown_code = [0,0,0]
        $ clowning_around += 1

        if clowning_around == 7:
            "C R E A K"
            ">>> From somewhere behind the painting comes the sound of delicate machinery shattering into a thousand tiny pieces."
            $ clown_down = True
            ">>> The painting opens to reveal a secret compartment!"
            j jsurprise "Wow! Sure looks like I solved that puzzle."
            j jneutral "And by 'solved', I mean 'brute-forced my way through with no idea what I was actually doing', but that still technically counts."
            jump investistart
        else:
            ">>> From somewhere behind the painting comes the sound of shifting machinery."
            ">>> The mechanism seems to have reset itself."
            if clowning_around == 1:
                j jthink "Hmmm . . . Is there something I'm missing?"
                jump investistart
            else:
                if hint_get:
                    $ big_hint += 1

                    if big_hint == 1:
                        j jthink "Alright, so that wasn't it."
                        j "I wonder what the pattern could be . . ."
                    elif big_hint == 2:
                        j jgrim "That didn't work either, huh? This puzzle must be trickier than I thought."
                        j jthink "Hmmm. A trio of clowns . . . There's something familiar about that. Maybe it's their gestures?"
                    elif big_hint == 3:
                        j jthink "Okay, so maybe it wasn't their gestures."
                        j jgrim "But they are, beyond a doubt, jesters."
                    elif big_hint == 4:
                        j jdoubt "Wait, didn't I read a book about jesters recently?"
                        j "Or try to read anyway? I'm pretty sure like half of that thing was in German, but it definitely had a trio of clowns in it."
                    elif big_hint == 5:
                         j janger "Okay, I've just about had it with this clown puzzle."
                         j jgrim "The nose-booping thing was kinda fun at first, but now my finger's getting booped out, and I still haven't solved it."
                         j "If this next combination doesn't solve it, when I'm done with this case, I'm gonna have to write a very strongly worded letter to Cirque du Soleil."
                else:
                    if clowning_around == 2:
                        j jgrim "It still feels like I'm missing some piece of this puzzle."
                        j jthink "Now, according to the sacred Law of Puzzles, whoever designed this thing was legally obligated to hide some kind of clue inside this mansion."
                        j "The only question is where?"
                    elif clowning_around == 3:
                        j jthink "Okay, I guess the third time isn't always the charm."
                    elif clowning_around == 4:
                        j jthink "Is there, like, a manual for this thing?"
                    elif clowning_around == 5:
                        j jgrim ". . . lousy juggling nose-honking tiny-car-driving glorified stand-up comedians . . ."
                    elif clowning_around == 6:
                        j janger "Okay, I've just about had it with this clown puzzle."
                        j jgrim "The nose-booping thing was kinda fun at first, but now my finger's getting booped out, and I still haven't solved it."
                        j "If this next combination doesn't solve it, when I'm done with this case, I'm gonna have to write a very strongly worded letter to Cirque du Soleil."
                jump investistart

label check_bunks_3d:
    if not have_gnome:
        j jsmug "Alright, let's see what's in here."
        j "It'd better be something cool considering it was locked behind that stupid clown puzzle."
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_gnome = True
        $ evi_count += 1
        j jsurprise "A garden gnome?"
        j jgrim "Eh, I could live without it."
        j jthink "Weird thing to put in a secret compartment, though."
        j "Guess that means I could use it as evidence?"
        jump evi_tally
    else:
        j jgrim "As much as I wish there'd been something cooler than a garden gnome in that secret compartment, I'm pretty sure that's all there was."
        jump investistart

## toilet ##
label check_toilet_1:
    if not cake_bake:
        if not cake_prep:
            j jneutral "The oven seems to work, at least."
            j "Might be fun to try my hand at a little baking while I'm here."
            jump investistart
        else:
            j jneutral "Now then, let's get this cake a-bakin\'!"
            j jthink "Just need to figure out how."

            $ interacting_with = "check_toilet_1"
            $ req = ["book","candle","gun"]
            jump stuff_prompt

            label .req1:
                j jthink "Naturally, the only proper way to bake a cake is in degrees Celsius."
                j jgrim "Wait, or was that Kelvins?"
                j "Uh, just to be safe, why don't we go with something halfway in-between the two?"
                j jthink "Okay, so if it's like between 180 C and 450 K, that would be . . ."
                j jdoubt "320 C? Yeah, that sounds right."
                j "And if we're working in centiminutes, then I should probably leave it in for a good three hours."
                j jneutral "Alright, there we go. All set!"
                $ cake_bake = True
                $ fire_count += 1
                alt "The oven bursts into flames."
                j "Gosh I love baking."
                jump fire_tally
            label .req2:
                j jsurprise "Ooh, I think I saw this in a fancy restaurant once!"
                j "The waitress set the cake on fire and then served it!"
                j jthink "They called it a baked Arkansas or something."
                j jneutral "Well, whatever it was, I'm sure it can't be that hard."
                j jthink "I just need to take my trusty candle, and . . ."
                $ cake_bake = True
                $ fire_count += 1
                alt "The oven bursts into flames."
                j jneutral "Viola!"
                j "Gosh I love baking."
                jump fire_tally
            label .req3:
                j jthink "If this is a gas stove, then I guess I need some kind of spark to ignite it."
                j "But just to be safe, I should light it from a distance."
                j jgun "For this sort of situation, I've got just the tool."
                j jthink "But first, I'd better figure out how to open the gas vent or whatever."
                j jdoubt "Wow, these metal bits are really stuck."
                j jgun "Maybe if I whack it with the gun . . ."
                $ cake_bake = True
                $ fire_count += 1
                alt "The oven bursts into flames."
                ""
                j jneutral "Well, I guess that worked."
                j jneutral "Gosh I love baking."
                jump fire_tally
    else:
        j jneutral "Pretty sure that cake's gonna need at least another hour."
        jump investistart
label check_toilet_2:
    if not have_fish:
        j jthink "You do hear an awful lot about dead bodies being stuffed in fridges."
        j "Assuming it's still functional, it'd be the perfect place to hide evidence."
        j "I'll just open it up, and . . ."
        j janger "Huh."
        j jdoubt"I guess that's technically still food."
        j "The yellow mold seems to be enjoying it, anyway."
        j jsurprise "Oh, what's this?"
        show screen sc_evidence_pane
        $ ev_bo = True
        $ have_fish = True
        $ evi_count += 1
        alt "Jam finds a red fish in the fridge."
        j jdoubt "This fish seems . . . well, relatively fresh."
        j "Which, given the circumstances, is pretty suspicious if you ask me!"
        j "Guess I'll just . . . take it . . . with me?"
        jump evi_tally
    else:
        j jdoubt "Yeah, no. I'm good."
    jump investistart
label check_toilet_3:
    j jsurprise "Ooh, someone left out their ingredients!"
    j jneutral "Looks like they were going to bake a cake with all this."
    j jsmug "Hehehe. If they're not gonna do it, maybe I'll take a crack at it."
    j jthink "Okay, let's add the flour . . ."
    j ". . . some eggs . . ."
    j jneutral "(whole, of course, for the extra nutrition!)"
    j jthink ". . . then a stick of butter . . ."
    j ". . . a spoonful of sugar . . ."
    j ". . . whatever this weird bitter almond sauce is . . ."
    j ". . . vanilla flavoring . . ."
    j ". . . and mix it all together!"
    $ cake_prep = True
    j jneutral "Looking good! Next up, time to bake!"
    jump investistart

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
    j jsurprise "Hey, there's a book on that chair! Well spotted, Jam!"
    j jsmug "A book tucked away in a hard-to-find location? It's gotta have all sorts of clues and evidence squirreled away inside."
    j "I'll just open it and . . ."
    show screen sc_evidence_pane
    $ ev_bo = True
    $ have_note = True
    $ evi_count += 1
    j jsurprise "Oh! Something fell out!"
    j jthink "An aging post-it note . . . Was someone using this as a bookmark?"
    j "And the text . . ."
    j "\'Iron Snail Authorization\'"
    j "What could it mean?"
    j jgrim "I mean, aside from \'Alexandre V. Badmann is super, super guilty,\' because that's totally what it says to me."
    jump evi_tally
    jump investistart
label check_securityroom_2:
    ## A translation from the faux-Middle English

    ## The Book of Dubiously Plot-Related Information
    ## Chapter Fifteen: The Tale of the Three Brothers
    ## Once upon a time, there were three jesters who called themselves brothers.
    ## The first jester was named Melech; the second, Mahendra; the third, Jimbo.
    ## One day, these three brothers were merrily strolling down the street when they were halted by the specter of Death.
    ## "Ho, knaves!" cried Death. "Of you three, one of you must die, in order for the other two to pass."
    ## At this, the brothers wept profoundly: alas, how tragic!
    ## None of them wished to see his brothers die before himself, so they devised a cunning plan.
    ## "If one of us must die," said Mahendra, a man of relentless exuberance, "take me first! I was born first, so I should die first."
    ## "No!" shouted Jimbo with a grin, his hand upon his bowtie. "First in, last out, as they say. It should be me instead!"
    ## "Can't we compromise?" wept Mahendra, his hands raised in supplication. "Instead, take me, the middle brother!"
    ## And so, moved by this show of brotherly loyalty, Death killed all three jesters and went off on their merry way.
    ## The end.
    ## Chapter Sixteen: The Tale of the Unreadable Text
    ## Once upon a time, there was a curse that randomly changed vowels into Y's and stuck E's onto the ends of words...

    ">>> The book is titled \'Ye Tome of Dubiously Plotte-Related Infourmacioun\'."
    ">>> It's open to a chapter somewhere in the middle."
    "Chaptere Fifteen: Ye Taile of ye Broutheres Three:"
    "Once ypon a tyme there weren three jesteres who dyd themselves broutheres call."
    "Ye fyrst jester was clepped Melech; ye secounde, Mahendra; and ye thirdde, Jimbo."
    "One daye weren these three broutheres with fulle merrimount ajaunte doun ye streete, when yon spectre of Deathe did them stoppe."
    "\'Ho! knaves,\' cryed Deathe. \'Of ye three, one muste needes die, that ye othere two mayen pass.\'"
    "To this, ye broutheres wepte profoundly; allas and weylaway!"
    "Nonne of them wished to seen his kinne befoure hymself peryshe, so a cunninge planne didst they devyse."
    "\'Yf one of us must needs die,\' spake Melech, a manne of relentless exuberance, \'taken me fyrst! Fyrst was I bourne, and fyrst shallen I die.\'"
    "\'Nay!\' excabrulated Jimbo withe a grinne, his honde upon his bow-tye. \'Fyrst inne, laste oute, as they sayen. It muste needs be me!\'"
    "\'Canne we notte comprymyse?\' wept Mahendra, his hondes raised inne supplicacioun. \'Instead, taken me, ye myddle brouthere!\'"
    "And so Deathe, mouved by this shouw of broutherely louyaulty, killed all three jesteres and wente off on their merrie way."
    "The ende."
    "Chaptere Syxteene: Ye Tyle yf ye Ynryedyble Tyxte:"
    "Ynce ypon a tyme, thyre wysen y cyrse thyte ryndymly dydst chyngen vywels ynto Ys, ynd yponne the yndes of wyrdes yffyxe Es . . ."
    if not hint_get:
        $ hint_get = True
    jump investistart
label check_securityroom_3:
    if not have_book:
        j jthink "If this is a proper spooky mansion, it stands to reason that there must be at least one rotating bookshelf."
        j "Badmann probably has a secret passage hidden behind it, safe from prying eyes."
        j jsmug "But not from me!"
        j jthink "Now, if I were Badmann, which book would I choose as the switch?"
        j "This riddle will require a thorough analysis of his life and background."
        j ". . ."
        j jgrim ". . . though on second thought, I'm not sure I actually know anything personal about him."
        j jdoubt "Uh, his name sounds kinda old-timey?"
        j "Is he like European or something?"
        j janger "Well, if that's the case, then there's only one book on this shelf that could be the switch!"
        show screen sc_stuff_pane
        $ ev_bo = False
        $ have_book = True
        j jgrim "Huh."
        j jdoubt "Well, I guess that wasn't it."
        j "Maybe it's just a regular bookshelf after all."
    else:
        j jgrim "If I wanted more weird, vaguely European reading material, I'd pirate it off the internet."
        j jdoubt "Or try and figure out how securityroom cards work, I guess."
    jump investistart
