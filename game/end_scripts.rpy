label raptorroom:
    show mono empty
    t "And... go go go."
    #!!replace tony with door
    $ kickedOut = True
    p "Gah."
    p "Guys?"
    p "Guys..."
    p "Let me back in."
    p "Hey, you can’t do this."
    p "Let me in."
    p "Oh geez."
    r "..."
    p "Hello there"
    r "..."
    p "You’re closer than i thought you would be."
    r "..."
    p "... Don’t suppose you’ll gve me a ten second start."
    r "..."
    p "Well then. Howzabout..."
    if have_ak47:
        p "i just..."
        p "Use this?"
        $ raptorRoomAK = True
        p "Er... can i pick that up, and try again?"
        r "..."
        p "No? Okay. Well then... Howzabout..."
    if have_grenade:
        p "this?"
        $ raptorRoomGrenade = True
        p "Ha ha. Not expecting that, are we. Now i'll just do this."
        $ raptorRoomGrenadeNoPin = True
        $ raptorRoomGrenade = False
        p "I guess that was older than it looked."
        p "Well. Go play catch."
        #!!(throws grenade)"
        p "Not a catch player. Ok i get it. Not much of one myself."
        p "Well then... howzaabout:"
        $ raptorRoomGrenadeNoPin = False
    if have_wadofcash:
        p "this?"
        $ raptorRoomWadOfCash = True
        p ". . ."
        p "Yeah, i don't know what i was expectign either."
        $ raptorRoomWadOfCash = False
    p "Crud. Well, i got nothing."
    p "Kind of a docile fellow, aren’t you."
    p "Howzabout, i just back... away slowly... and... maybe... get to the choppa."
    p "Kind of... always... wanted... to say... that."
    p "Oh crap."
    show mono empty
    r "Crunch."
    jump endcard

label route01: #accussing adrian - Evidence -  print out and personal photo / Stuff - Crowbar - Find Crowbar in toilets. USe it to break open Locker. Both items are found in Reception
    p "My fellow employees."
    #!!toskip for testing
    $ location = 10
    jump investistart
    t " Oh. You’re back."
    p "But of course. I have something most pressing-"
    t " I honestly wold have thought we would have to come get you."
    p "Not at all. I am here-"
    t " I’m actually kind of impressed. Who wold have thought you would have braved your own death so willingly."
    p "Well, i am not so-"
    t " Touched even. It seems you are truly a man among men. I am sorry that we have had to fall to this route, and push such a terrible burden onto so noble a sul that-"
    p "Actually, if you would let me finish."
    t " Oh, i am sorry my good man. Do go on."
    p "I’m here to accuse Adrian of his crimes so that he can take my place."
    t "..."
    p "..."
    t "..."
    t "I’m not sure how to feel now."
    p "neither i am to be honest."
    a "I’m sorry. Crimes? What have i done exactly?"
    t " Glad you asked. Traitor to mankind. For you see-"
    h "I’m sorry. Traitor to mankind. What could you have possibly found out that means that he’s betrayed all of mankind?"
    p "Well, traitor to mankind might be a bit much, i admit."
    p "Maybe a traitor to the procedures and polices of the office workplace, as documented on teh staff website."
    h "That’s quite a significant difference. What could he have possibly done?"
    p "Well, if you would actually let me start-"
    j "Look, does this matter at all? He’s clearly just stalling so he doesn’t get eaten."
    t "Feel quite sickened that i referred to him as noble to be honest."
    j "This is what this man does. He’s a useless little nobody who blames others and-"
    t " I feel i could actually throw up."
    j "passes off his mistakes to them. Listening to him will get us nowhere but eventually eaten because we were too busy listening to him."
    h "I don’t see the harm in it."
    j "Are you kidding me? We can’t just-"
    h "We have just a short time left before we have no choice but to attempt an escape. Why not let him has his last meal?"
    j "Because we’re about to be eaten."
    h "Paul, what was your evidence."
    a "I feel i should at least get a say in this if-"
    h "Quiet. The accessed may nt speak."
    a "But-"
    h "Silence."
    h "Paul, you were about to give your testimony."
    p "Thank you, your honour."
    j "Oh good lord."
    p "So... Take a look at this!"
    #*!!image of table with Adrian evidence*"
    t "My god."
    h "Is that-"
    p "Exactly, a personal item on his desk, and personal use of the office photocopier to print off some tcvkets."
    p "Why, if Todd hadn’t been devoured he would be-"
    t " I can’t believe it."
    j "Ohmy stars."
    a "What?"
    h "It is shocking, i admit."
    a "Gys/ You can’t be serious."
    j "All this time. I would never have suspected."
    a "Seriously. This can’t be enough to-"
    t " I can’t believe he’s actually married."
    a "What?"
    p "Huh? (dumb smiliey face)"
    h "She’s actually not bad looking either. And is this your kid?"
    a "Well, yeah but-"
    j "He’s adorable. What’s his name?"
    a "It’s Toby."
    h "Why haven’t you brought him in before?"
    a "Wel, Isabelle did suggest it, but we travel here by boat and-"
    h "Oh nonsence. If the place finds a way to continue, you definitely have to bring him over. Hes so sweet."
    a "Aw, thanks."
    t " And all this time i could have sworn you were- well, nevermind."
    p "Erm-"
    a "Well i;m sure i must havementioned them."
    t " Well, i suppose it sounds foolish, but i’m usually ina  bit of a rush when coming into reception, so i’ve probably-"
    j "Yeah, me too. Sorry, Adrian."
    h "Situations like this makes you realise how we take each other for granted in the workplace."
    p "But-"
    a "Oh i know. I’m just the receptionist. You just smile at me and make small talk. I’m used to it."
    t " No no. We’re in the wrong here. I saw you as just another pen pusher, but you’ve got a whole life."
    t "God, i’m a shitty person. I just see people as floating heads, their individual liveseasily ignored as i move past them."
    p "-this is his crime."
    t " Tell you what. When we get ast all of this, i’m taking you and your family to dinner."
    a "Oh you don’t have to-"
    t " Nonsense, we’ll all go."
    p "Hes guilty."
    t " I know a great place. They have their own michilena star chef. Does incredibly !!food!!"
    h "Oh do you mean Tanon’s. It’s a good place. Definitely worth it."
    t " Well then i guess we all definitely have to survive then? Ha"
    a "Yeah, i guess we do. Ha."
    t "Hahaha"
    h "Hahaha"
    j "Hahaha"
    p "Hahaha"
    $ location = 10
    jump investistart

label route02: # Accussing Jenny - Evidence - Grenade - Dictaphone/Transcript / Stuff - Match/ some other firestarter - Grenade found in Security Room - Dictaphone found in JEnny's Bunk box, accessible by start a fire in the bunks, with match and fuel can. Match found in CEO Office, Fuel can found in Corridor.
    p "My fellow employees"
    t "Oh. You’re back."
    $ location = 10
    jump investistart
    #!!removeaftertesting
    p "Yes, i have indeed returned. With justice."
    t "I don’t think that will help in the current man eating dinosaurs situation, "
    t "but i appreciate your enthusiasm."
    p "Oh it will help. Help it will indeed provide. With help i bring. In the form of justice."
    h "Well now it just looks like you’re stalling."
    p "Stalling with help."
    h "Ok. Well lok, should we just get started? Those raptors aren’t going to eat Paul themselves."
    h "Well, i guess they are. That’s the whole point. You all know what i mean."
    h "Freaking weirdo."
    p "Behold. My evidence."
    h "Evidence?"
    p "You asked me to get evidence."
    h "I... no."
    p "Evidence of the crimes of another, to prove them less worthy than i to get on board the helicopter that will usher us in to safety."
    h "Oh right. Well, i don’t think t really matters now. I doubt anything you can really say would result in anything changing-"
    p "I nominate Jenny;’s crimes."
    j "The hell?"
    p "Jenny’s crimes are most unconsciousable, and it would do you all well to heed and words and take action from them."
    j "Oh like we should be putting up with this. I was going to get you a last meal and now you accuse me of something-"
    h "Jenny."
    j "I mean it was just going to be something from the vending machine but he wasn’t going to have to pay."
    h "Jenny."
    j "Now he tries to pass the bck off to me."
    p "You are the most meatiestof us. It would increase the time it would take the raptors to consume you."
    j "..."
    h "..."
    t "..."
    p "(smiling)..."
    j "You can start running now."
    h "Settle down."
    j "I am not settling-"
    h "It doesn’t matter, Jenny. He’ll be dead soon, rememebr. LEt him get this stuff out of his system."
    j "Grrr."
    h "Also, the stuff in the vending machines is not safe for human consumption and him getting a stomachache may prevent him from getting a good initial panic dash in."
    j "..."
    j "Fine."
    h "Now, what were you saying about evidence?"
    j "Seriously?"
    h "I’m just curious. What do you have to show us, Paul?"
    p "Yes. My evidence.Of Jenny’s most devious and smelly crimes !!kind of get him into a grand protector mindset beforehand!!"
    p "Behold!"
    t "Jesus. Is that a grenade? Where dd you find that?"
    h "And a transcript? What is this? (reading image?)"
    t "I think the grenade is more pressing."
    h "It has a pin in it, right. Should be safe."
    j "That’s my grenade. You went through my stuff."
    t "Why do you have a grenade?"
    j "It was my father’s."
    t "That does not answer the question."
    h "(still reading) Kind of does. Is this a conversation between me and my... client. One that we had ver the phone."
    j "What? Er..."
    a "And this is one between me and my family. Were you listening in on us?"
    j "..."
    t "What? Is there any for me?"
    h "There’s a bunch here. Phone transcripts for a bunch of employees."
    t "But any for me?"
    h "You don’t even have a phone here."
    t "Oh, the land lines. That’s cool then."
    h "Jenny? What is this?"
    p "They are her crimes."
    h "Shut up."
    p "..."
    h "Jenny?"
    j "Mr Willowisk asked me to make them. He got me to plant bugs on all the phones, and then make transcripts."
    h "For just random conversations."
    j "Look, night shifts are long, and i have nothing to do. He took away my little tv, and i was bored so..."
    a "You spied on us."
    j "Only to pass the time. IT’s not like anyone really said anything too important. IT was just work stuff."
    h "So you don’t know that-"
    h "Ok."
    a "Ok?"
    h "I’m fine with this."
    h "Absolutely fine."
    #H goes up to a shredder."
    h "I think we can all just agree that this didn’t happen."
    p "Indeed. All crimes never happen if you destroy the evidecne i spent hours desperately trying to-"
    a "I guess it’s no big deal."
    p "SILENCE You-"
    h "Things like this hardly seem important when the rest of the staff are dead. It’s not like the Park’s continuing after this anyway."
    h "Honestly, i was in talks with another park. Looking to move on. No sense hiding it now."
    j "I’m sorry everyone. I was a real jerk."
    h "Yeah you were. But, you’re our jerk."
    t "Yeah. And hey, you got us a grenade. That might be the handiest thing we have in the next hour."
    j "I actually kind of forgot about it in all the ruckus. It’s just a memento from my dad’s army day."
    j "I just keep it in my bunk locker."
    h "Insanely dangerous, but i’m not complaining..."
    t "Wait, did you say your bunk locker."
    p "That is where the evidence was recovered, yes."
    t "Have you been going through our stuff?"
    p "..."
    $ location = 10
    jump investistart

label route03: # Accussing Helen - Evidence - Research Journal/Raptor Claw / Stuff - Research Journal found under chair in Lab (staff room) - Raptor Claw found by using security card on containment lock. Card found in CEO office
    p "My fellow Americans"
    $ location = 10
    jump investistart
    #!!removeaftertesting
    h "Actually, i’m Canadian"
    t "Me too."
    a "British"
    j "I’m actually from Hawai"
    p "That couldn’t count."
    j "The hell you say!!!"
    p "Anyway,i bring to you, in this most dire f times, evidence. "
    p "Evidence that supports my case and makes it clear that one among us is a traitor, and should be totally thrown out of the airlock first."
    j "Wha on earth are you talking about?"
    p "I mean, i guess that’s kind of what all this is."
    p "Though it totally wasn’t my intention when it all started."
    p "It was more just about finding reasons why someone should be thrown out to be eaten by Veliciraptors"
    p "and why that someone shouldn’t be me."
    p "That was the whole premise of this entire escapade."
    h "I think you’re getting off track."
    p "Or perhaps it is the only track i should be on."
    p "Maybe this is my life now. Endlessly finding ways to stay on track, the track of accusing other people of crimes that they may or may not have committed. "
    p "all in the hopes of saving myself, a person who may nto be worthy of being saved."
    t "Well if you’re just going to admi it..."
    p "I admit nothing. Instead, i provide evidence."
    h "What’s this?"
    p "EVDENCE."
    h "Of What?"
    p "Huh?"
    h "Evidence that proves what?"
    p "Oh right, that Helen is secretly evil and was conspiing with a rival corproation to take this palace down."
    p "Huh? That actually seems like a pretty good fine."
    j "(as the judge) What’s this?"
    a "Huh? These appear to be research notes on the the Veliciraptor Reproduction Analysis. "
    a "It’s a method of giving asexual dinosaurs the ability to reproduce, and how to increase the frequency."
    h "Erm"
    t "Jesus."
    a "With this method, reproduction rates would increase from zero to three raptors a day within the space of about three weeks. "
    t "Wouldn’t that overrun the park?"
    j "We were having problems keeping the ten we have at the moment contained"
    j "I mean, it was doable, but there were daily issues."
    a "IF this happened, it would have been so much worse than the current situation."
    h "Well yes, but the research was entirely hypothetical. It’s not like i actually planned to go through with it-"
    a "And this is a transcript of you speaking with Hammond Industreies CEO"
    a "Where he asks you to sabotage the park by introducing the changes in the raptors DNA via their water supply."
    p "I found it under a chair!"
    t "Helen. This. This is horrible"
    t "Were you really going to put us all at risk like this."
    h "No. Not necceasrilly. I mean, in order to even get away with something like this, "
    h "i would have had to do it at a time when there was a low staff turnout on the island."
    h "People would notice far too quickly if i tried to sabotage the water supply. I at least had to do it when the environmental officer was on leave."
    a "Well i suppose..."
    h "In four days times."
    a "..."
    h "Look, it’s not as bad as it sounds."
    j "Why would you do this? Why would you risk getting us all killed like this?"
    h "You wouldn’t have gotten killed. I don’t want anyone to die. The jump in reproduction rates would have been noticed within the first week. "
    h "We would respond by disabling the raptors, enacting a castration protocol for the males,"
    h "including the baby ones, and the long terms effects of the issue would be resolved within the year."
    h "The point was is that i would fix the issue and get commended for doing so. "
    h "That way i’d finally actually get noticed and not be passed up for promotion again."
    t "This was all for a promotion."
    h "Not all for a promotion.I didn’t even do anything in the end. It was just a plan i was considering."
    p "But, she was talking to the CEO of="
    h "Exactly, our CEO found my research papers. He cotton onto t."
    h "We actually just had a talk yesterday about it. Got the entre thing out in the open."
    h "He even apologised to me. Realsiign how stressed i had been."
    h "He was sucha  sweet man. I just wish this moron hadn’t gotten him eaten."
    p "But-"
    t "I guess we don’t consider how stressful it is for those of you in the Research sector."
    j "Yeah i guess because it looks like you have the cushy science jobs that you’re getting by just fine."
    j "You just have all sorts of stresses that we working plebs don’t have to deal with."
    h "Oh come on guys. I’m not some elite pretentious jerk, looking to screw everyone else over just to get a promotion."
    h "I have to clock in at 10am the same as the rest of you."
    a "My shift starts nine."
    j "I start at six."
    t "I’m on call 24/7."
    h "Even so, we’re all just working for a paycheck. I was even going to use my bonus to spring for a big dinner for all the staff. "
    h "It’s a shame  it won’t happen now."
    p "I think that-"
    j "You were going to do that for us?"
    h "Yeah, fanciest place on the port. I was really looking forward to announcing it as well."
    p "We may be missing the point-"
    t "Hey, why don;t we go there now?"
    h "Now? But, the raptors."
    t "Once we get off this island. When we survive this, you can take us to dinner."
    h "Tony..."
    h "Everyone..."
    h "Thank you."
    h "I don’t deserve to have co-workers like you."
    a "You sure don’t."
    j "Come on. Bring it in guys."
    p "But the transcript-"
    a "Let’s go out there, and get to that helicopter."
    p "Is anyone listening..."
    $ location = 10
    jump investistart
    #!!removeaftertesting


label route04: # Accussing Tony - Evidence - Assassin Contract/Wad of Cash / Stuff - Hammer Wad of cash found in Tony's bunk. Contract found in CEO office globe by smashing globe with hammer. HAmmer found under teddy bear in bunks
    j "Oh good. You’re here."
    $ location = 10
    jump investistart
    #!!removeaftertesting
    p "Ok. Everyone. You have to listen to me."
    h "Ah, the desperate bargaining."
    h "I was wondering when he would start."
    p "No, this isn’t just- I mean. It’s not as simple as-"
    t "..."
    p " Oh geez."
    a "Calm down, Paul. I know it’s a lot to take in but-"
    p "Oh shut up, Adrian. No one likes you."
    a "I..."
    a "Oh."
    t "Don’t listen to him, Adrian. He’s just panicked because of wa we’re asking him to do."
    a "Really."
    t "Of course. Why, i’d kill to just sit down and have a beer with you sometime. We should do so after this."
    p "..."
    a "Thanks man. I guess my ego’s not the best at handling that knd of thing."
    t "Don’t sweat it. I’d hate for you to get all cut to pieces about this."
    p "..."
    a "Heh. I’ve been told i get a little imposter syndrome at times. I knwo it’s not healthy, but it’s part of my life i guess."
    t "Hey, ti’s nothing to get blown up into little pieces about. "
    t "It’s not like someone’s going to seal you inside a concrete coffin just because yo get nervous at times."
    p "..."
    a "Heh. Thanks man."
    t "Don’t sweat it."
    p " He’s a murderer."
    h " What?"
    j "What?"
    t "..."
    a "What? No, i’m not."
    p " No. Not you. Tony."
    t "Hey, what i did i did for my country. I served. It doesn’t count."
    p " No. I mean...he’s a hitman. Look at this."
    h " Contract of Assassination. This contract is an agreeded upon set of of principals for the sum of $200,000 shall be exchanged"
    h "of the target of the contract life ends within the agreed upon date range."
    t "Erm..."
    h " This contract stipulates that Tony Floyover shall within the agreed upon amount in the wake of the death of Cretanious corner’s CEO Todd munckin."
    j "What is this? Some kind of joke."
    t "Yeah. Yeah, it’s a joke. Me and Paul here are just having a laugh at you. But he got the timingwrong."
    t "Didn’t you Paul? I wouldn’t want you to trip over such a simple mistake and hurt yourself."
    a "..."
    h "..."
    j ".."
    j "Well that sounded like an obviously veiled threat to me."
    t "Really? Usually it goes right over people’s heads."
    t "Well, can’t blame a guy for continuing to do what worked so well before."
    h " So. You mean."
    t "Yes. I am a contract killer. And i was hired to kill your boss."
    t "Not that that matters now."
    j "How could this be-"
    t "Huh, you know. You leave the army. No one will take you on for work. You end up being homeless. End up doing a few jobs for the mob."
    t "End up doing them really well, and they give you all sorts of roles to do."
    t "Not long before you end up going back to the government for work."
    t "Helps that i actually am a helicopter pilot. LEts me go all over the place."
    a "So you were going to-"
    t "Kill the cEO, yes. Turns out his competitors hate that he got out of paying settlement costs for obvious copyright infringement."
    t "Again. Not thast any of itmatters."
    h "... (still reading)"
    t "Though,  suppose that now you all know."
    p "..."
    j ",,,"
    a "..."
    h "..."
    h " As far as i’m concerned, this changes nothing."
    t "What?"
    p "What?"
    h " I am saying this is not reason enough to swap you out with Tony."
    p "But he’s a paid killer."
    h " Tony. Were their contracts out on any of us besides the CEO?"
    t "..."
    t "There were not."
    h " And would death by raptor still get you paid."
    t "It would. I can claim it was a planned accident."
    h " So this doesn’t really cange anything fo us,"
    p "But, but he’s a killer A murderer. Who knows when he’lll plan to just off one of us-"
    t "Hey. I’m a professional. You only die by my hand if you’re a contract, or if you’re in my way."
    t "And you’re looking very mch like an obstruction, boy."
    p "..."
    h " It’s irrelevant. And it doesn’t change the most important fact about all fo this."
    t "Yeah, and what’s that?"
    h " That you’re the only one that can pilo the helicopter. We can’t leave you behind."
    t "..."
    p "..."
    t "Oh right."
    p "Yeah, that makes total sense."
    p "Don’t know what  was thinking. Sorry."
    t "Don’t worry about it. You’re just not thinking straight. Happens to anyone in a situation like this."
    p "Yeah..."
    h "Anyway, if we’ve all had enough shenanigans. let’s continue with the escape plan with Paul being used as bait."
    t "Okay..."
    p "Yeah okay."
    p "..."
    p " Hey wait-"
    $ location = 10
    jump investistart

label route05: # faking evidence to accuse Adrian - Evidence - Fake Transcript/ Fake ID card / Stuff - Plain paper/ Plain ID card - Plain paper found in reception, ID found in Lab, security puzzle completed in security room
    a "And that’s why i’m thinking we should be nicer to the guy. IF he is going to die today, then the least we could do is not be dicks about it and-"
    $ location = 10
    jump investistart
    #!!removeaftertesting
    p "Yoohoo. I have here evidence to present to all of you."
    a "Ah Paul. IT is good to see you. Tank you for coming back-"
    p "Shut up, Adrian."
    a "I- excuse me."
    p "Oh i’m sorry. Was i unclear. Stop. Making. Noises."
    a "Well there’s no need to be so-"
    p "I am onto your evil scheme. I have discovered all the proof i require."
    a "Wh- what is ths? What are you going on about."
    p "Here. I present to you all.... Evidence. Evidence that Adrian is the cause of our current situation."
    a "What?"
    h "Seriously?"
    p "Please do not question how i came upon this evidence in such a short period of time, and instead question Adrian’s true motives. "
    p "For he is te one who attempted to hide this evidence, and i am the one who attempted to find it."
    p "And er... did."
    h "What are you babbling about. Give that here."
    a "What is he talking about."
    h "This..."
    h "These are the access logs for the raptor exhibit at the time of their escape."
    h "It shows someone intentionally unlocked the exhibit at the time the CEO and the others were in the area. "
    h "ID: 4025202 four zero two five two xzero two... whose is that?"
    a "Erm... that’s mine. But i didn’t. I couldn’t have- wouldn’t have. I mean..."
    p "I overheard a conversation between Adrian and Todd the other day. Adrian was annoyed that Todd didn’t approve his bonus for this year. "
    p "Said he hadn’t been working long enough."
    h "Erm yeah. Geez, this shows you disabling the security locks and taking out the defence grid."
    a "No. It’s wrong. I mean, i know it looks like-"
    t "Shut up. Is this genuine?"
    h "These are how the access logs show up on the sstem, and Paul wouldn’t have access to modify that system. "
    h "Only the systems administrator and the CEO would have that. You could view it but that’s about it."
    p "I printed it off as a pdf, then copied it to word to print out."
    h "It definitely looks accurate, and makes it clear that Adrian’s responsible."
    a "But... i’m not. I seriously don’t know what this is. I’ve never seen-"
    j "Never seen, huh?"
    a "What?"
    j "The Reception would have access to these systems as a security precaution. "
    j "Adrian can theoretically activate and deactivate defences at any time, since he’s most likely the first person to notice a dinosaur coming up the main entrance."
    t "I would have thought hed just be able to activate it. Shouldn’t a manager or something be the one to deactivate it."
    j "It’s not a bank. He’d need to be able to turn these things on and off just in case someone came running up to the doors after the force field was up."
    h "So it’s entirely possible that he could do this."
    a "B ut-"
    p "I just thought you should all know what he did before i died."
    p "I suppose we should get on with my final moments."
    p "I hope you all make it out alive."
    h "Wait."
    a "Oh no."
    h "We need to reconsider things."
    t "Yeah. We were doing this to Paul because we thought he was responsible."
    j "But he was responsible."
    j "We saw it on the cameras that he was the one that deactivated everything by accident."
    p "..."
    p "(oh right)"
    h "Yes, but he did it by accident at the same time Adrian apparently did it intentionally."
    a "I did no such thing. You guys- i think someone may be trying to frame me."
    a "Though who would do that?"
    h "Look, we’re nearly out of time."
    h "And, as far as i’m concerned, either one of you is suitable to the task of distracting raptors through sheer panic."
    a "You don’t mean-"
    j "Wait."
    j "We don’t know if he really did this."
    j "What if someone used his access in order to do this as him?>"
    h "Well presumably such a person would keep themselves safe and be one of the remaining survivors."
    h "Which basically means that it’s still one of us, and we would need to determine who within the next minute or two."
    j "..."
    j "Objection withdrawn."
    a "What?"
    j "I ain’t wasting time trying to figure thai out. LEt’s just have them felip a coin or something."
    p "What?"
    a "Seriously."
    j "Yeah. One definitely helped cause this by accident, and one may have intentioanlly done it. Either is pretty bad. Let’s flip a coin and decided that way."
    h "Seems reasonable."
    p "Wait-"
    t "Yeah, let’ws go with that."
    a "I don’t think."
    h "It doesn’t matter what you think. IT’s three against two. Anyone got a coin."
    a "I mean i do but-"
    h "Thank you."
    h "So. Paul. Heads or Tails."
    #coin flip switch between the two
    p "It’s nice to know things work out well in the end."
    p "You clock in everyday. You work hard."
    p "You get noticed by your boss and you’re appreciated for your efforts."
    p "Life goes by nicely. "
    p "Sure i’ll have to get a new job now."
    p "And i don’t have anyone left to give me a reference from my old job."
    p "But it’s sure to make an interesting story in the next interview."
    p "All it requires is a way to bring it up organically."
    p "Oh, i could also mention i got to ride on a helicopter."
    p "That’ll make me stand out."
    p "Yep. Sure is a good day."
    #!!fixforspecialending
    $ location = 10
    jump investistart
    #!!removeaftertesting

label route06: # any combination of incorrect evidence
    p "Greetings all. I have returned."
    $ location = 10
    jump investistart
    #!!removeaftertesting
    j "‘bout damn time. We were just about to come fish you out of whatever cupboard you had hidden yourself in."
    p "I- wait, was that an option."
    j "..."
    j "I mean, technically, yes. I suppose."
    j "Couldn’t we all just hide in cupboards until this goes away."
    h "The forcefield will break down shortly. After that, it’s just a matter of the raptors entering the building and sniffing us out."
    h "It’s possible they’ll get bored and wander away from the building, but then we’ll be trapped here indefinitely."
    t "It’s not like anyone knows to come rescue us. People probably won;t be getting suspicious tere’s something wrong for at least four days."
    h "And at any point the raptors could just burst in here and start chewing down on us."
    h "Better we do it this way, then get eaten in our sleep."
    j "Okay okay. So no, it’s not an option."
    p "Duh. Of course it’s not an option."
    j "Shut it you."
    a "So i guess we get started then?"
    p "Actually, before we do that. I have some evidence to present."
    p "Evidence i dare say you should find most illuminating."
    t "Evidence? For what?"
    p "Evidence that shows one of us is not worthy for survival of course."
    p "At least, less worthy than I."
    a "han me."
    p "Exactly."
    a "No no. ‘Less worthy than ‘me’’. You use the object pronoun, not the subject pronoun."
    p "Exactly."
    a "..."
    h "What is this evidence?"
    t "Yeah, let’s get this over with quickly. I get the feeling this is going nowhere."
    p "Very well."
    p "Behold."
    p "My evidence."
    j "Oh my word."
    h "Interesting."
    t "This..."
    t "Is absolutely meaningless."
    p "It is?"
    t "Yes of course."
    t "The two items, which are so meaningless in their relationship i will now only refer to them ambiguously, have no connection to each other whatsoever."
    p "Really?"
    p "But what if i arrange them in this configuration?"
    t "I... i mean that’s actually really good."
    j "It’s beautiful."
    h "What have i been doing with my life before this moment?"
    t "But it still doesn’t really mean anything."
    t "The two pieces of evidence, which are both still admittedly wonderful but also still unworthy of being labeled, do not have any connection to each other."
    t "Sorry Paul, but i think you just weren’t paying enough attention."
    p "D’aawwww. I guess i’ll have to try again."
    t "I guess so."
    h "No. No he won’t."
    h "Times up. We have to go."
    h "Sorry Paul. But you’re attempt to pass the bame onto someone else has been fruitless."
    p "Aww, but i tried really hard."
    h "I know you did, sweetie."
    p "..."
    h "..."
    t "..."
    h "Okay, people. Let’s get a move on. Those raptors aren’t going to eat themselves."
    h "We in R&D had to wrok hard to prevent that happening."
    h "In retrospect it wasn’t worth it."
    j "Hey..."
    j "Do you suppose we could take this evidence with us?"
    $ location = 10
    jump investistart
    #!!removeaftertesting

label route07: # brain broken due to puzzle
    p "So if this bit goes here and that bit goes there."
    p "And that bit goes there and this bit goes here."
    p "Then it makes sense that this bit doesn’t belong here."
    p "And that piece does belong there."
    p "So it’s pretty clear by this point..."
    p "That this puzzle box is secretly more than a puzzle box."
    p "It is actual a metaphor for all of everything in the universe,"
    p "The box emcompasses all of me."
    p "And i am all of the universe."
    p "There are probably even little versions of the puzzle box within the puzzle box."
    p "Since, by definition, something that emcompasses everything should also contain itself."
    p "And by that logic - why is my brain copper tasting."
    p "..."
    p pdumbass "It’s so delicious."
    show mono empty
    r "SOME TIME LATER"
    t "Found him. He’s here."
    t "Holy crap."
    t "I think he’s dead."
    a "Zounds!"
    h "Let me see."
    h "..."
    h "Looks like he is."
    h "Some kind of anueriysim."
    h "anueroism"
    h "an-nue-ro-ism"
    t "Aneurysm"
    h "That’s what i said."
    h "His head has basically exploded."
    h "Possibly, from too much thinking."
    j "I suppose we did put a lot on his plate."
    j "Maybe we were too hard on the fellow."
    h "Possibly..."
    t "More importantly though, what are we going to do now?"
    t "do we choose between one of us who should go out there first."
    h "Actually, i have a better idea."
    r "MORE TIME LATER!"
    t "I just don’t get why you guys have a catapult on the roof."
    a "I always questioned it but someone always said-"
    h "Shut it, Adrian."
    h "There’s no time to explain."
    h "There is a remote controlled catapult installed on the roof. The CEO wanted it, and he’s rich, so it got made."
    h "Here’s the plan."
    h "We’ve loaded up Paul’s body. Now we all go back downstairs, get to the force field, activate the catapult, "
    h "wait for the raptors to take the bait, then turn off the forcefield and run. Everyone got it."
    a "so we’re using his body."
    h "As bait still, yes."
    h "Him still being alive wasn’t really necessary."
    h "Just being made of meat and able to covered a suitable distance."
    h "In fact, this is even better, as we’ll be able to pinpoint a general landing area far enough away for the corpse to land."
    h "Much better than Paul barely making it out of the front door."
    t "I guess it was a good job he did die then. He’s really raised our chances fo success."
    j "(!!Dispondant!!)Why did you make me haul the body up te stairs."
    j "He was so stiff."
    h "Right, so we’re all good to go. Calculations are set. No test shot so we’ll have to hope for t best."
    h "Everyone get downstairs and be prepared for the sprint of your life."
    j "Still warm."
    t "Come on Jenny. Time’s a wasting."
    #!!catapult ending
    jump endcard

label grenadeend: # checking the grenade
    jump endcard

