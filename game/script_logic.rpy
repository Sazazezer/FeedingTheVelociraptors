label falsestart:
    $ location = 1
    $ interact_mode = True
    ">>> Investigate the room with \[MOUSE\].\n>>> Inspect highlighted objects with \[LEFT CLICK\].{fast}"(advance=False)

label investistart:
    $ refresh_location()
    show mono empty
    $ interacting_with = ""
    $ interact_mode = True
    ">>> Investigate the room with \[MOUSE\].\n>>> Change rooms with \[MAP\].{fast}"(advance=False)

label forceroomrefresh:
    $ refresh_location()
    show mono empty
    $ interacting_with = ""
    $ interact_mode = True
    ">>> Investigate the room with \[MOUSE\].\n>>> Change rooms with \[MAP\].{fast}"(advance=False)

label evi_tally:
    if evi_count == 1:
        p "Welp. That's one piece of evidence."
        p "I'm no fool though."
        p "I know i need at least two pieces of watertight evidence in order to pin this on someone."
        p "And one piece is all leaky and stuff."
        jump investistart
    elif evi_count == 2:
        p "Excellent. Two pieces of evidence."
        p "That's more than enough to make some kind of accusation."
        p "I could always look for more though."
        p "Maybe make the accusation valid."
        jump investistart
    elif evi_count == 8:
        p "I can safetly say with absolute certainly..."
        p "Almost as if the god of this world was speaking through me..."
        p "That all the evidence has definitely been found."
        p "That being said..."
        p "There's more than one way to obtain evidence beyond merely 'finding' it."
        p "Heh heh heh."
        p "I wonder why i don't have any friends."
        jump investistart
    elif evi_count == 10:
        p "And with that-"
        p "I must definitely have all the evidence i would ever need."
        p "There definitely can't be anymore."
        p "For one, the box to the right of me is all filled up."
        p "Guess i better go finish this."
        jump investistart

label fire_tally:
    if fire_count == 4:
        p "Will fire exist in this game."
        p "Find out on the next episode of Feeding the raptors Z"
        jump investistart
    else:
        jump investistart

## Stuff prompt
label stuff_prompt:
    $ interact_mode = False
    $ stuff_cue = True
    $ stuff_selected = ""

    show screen sc_stuff_pane
    $ ev_bo = False

    ">>> Click to use an item from \[STUFF\].\n>>> Press \[SPACE\] or \[LEFT CLICK\] to return.{fast}"
## If the player clicks out of the interact screen, wipe the variables and return to the room.
    $ interacting_with = ""
    $ stuff_cue = False
    $ stuff_selected = ""
    $ req = ["","",""]
    jump investistart

label stuff_check:
    $ jamp_1 = str(interacting_with+".req1")
    $ jamp_2 = str(interacting_with+".req2")
    $ jamp_3 = str(interacting_with+".req3")
    if stuff_selected == req[0]:
        $ renpy.jump(jamp_1)
    elif stuff_selected == req[1]:
        $ renpy.jump(jamp_2)
    elif stuff_selected == req[2]:
        $ renpy.jump(jamp_3)
    else:
        if interacting_with == "check_lounge_1":
            p "This is a special option that MAtt forgot to set."
        else:
            p "That's probably not right."
            p "Maybe if i smoosh them together."
            p "Nope. Not right."
        jump stuff_prompt

## Evidence prompt
label accusation:
    $ interact_mode = False
    $ evidence_cue = True
    $ evidence_selected = []

    show screen sc_evidence_pane
    $ ev_bo = True

    ">>> Click two pieces of \[EVIDENCE\].\n>>> Press \[SPACE\] or \[LEFT CLICK\] to return.{fast}"
## If the player clicks out of the interact screen, wipe the variables and return to the room.
    $ evidence_cue = False
    $ evidence_selected = []

    p "Ah, i don't think i'm quite ready yet."
    p "So... i guess i should sneak back out of the room before anyone asks what i’m dong back here again?"
    t "You do realise we can all hear you right?"
    p "NO YOU CAN’T!"
    jump investistart

label finale:
    #if "gnome" in evidence_selected and "knife" in evidence_selected:
    #    $ route = _("3/16: The Gutter of Depravity")
    #    jump route01
    if "photo" in evidence_selected and "printout" in evidence_selected:
        $ route = _("3/16: Definitely Adrian's fault")
        jump route01
    elif "grenade" in evidence_selected and "dictaphone" in evidence_selected:
        $ route = _("4/16: J'accuse La Jenny")
        jump route02
    elif "raptorclaw" in evidence_selected and "research" in evidence_selected:
        $ route = _("5/16: Oh... Helen actually did do something bad.")
        jump route03
    elif "contract" in evidence_selected and "wadofcash" in evidence_selected:
        $ route = _("6/16: Tony the Ass Asser")
        jump route04
    elif "fakepaper1" in evidence_selected and "fakepaper2" in evidence_selected:
        $ route = _("7/16: Definitely defiitely Adrian's fault")
        jump route05
    else:
        $ route = _("8/16: The evidence isn't random!?")
        jump route06
    #else:
     #   j jdoubt "Hey, you. Yeah, you, at the computer."
      #  j janger "I think you broke the game."
       # jump investistart

label endcard:
    $ interact_mode = False
    $ evidence_cue = False
    $ stuff_cue = False

    if "photo" in evidence_selected and "printout" in evidence_selected:
        $ persistent.end_03 = True
    elif "grenade" in evidence_selected and "dictaphone" in evidence_selected:
        $ persistent.end_04 = True
    elif "raptorclaw" in evidence_selected and "research" in evidence_selected:
        $ persistent.end_05 = True
    elif "contract" in evidence_selected and "wadofcash" in evidence_selected:
        $ persistent.end_06 = True
    elif "fakepaper1" in evidence_selected and "fakepaper2" in evidence_selected:
        $ persistent.end_07 = True
    else:
        $ persistent.end_08 = True

    if persistent.end_01 == True and persistent.end_02 == True and persistent.end_03 == True and persistent.end_04 == True and persistent.end_05 == True and persistent.end_06 == True and persistent.end_07 == True and persistent.end_08 == True and persistent.end_09 == True and persistent.end_10 == True and persistent.end_11 == True and persistent.end_12 == True and persistent.end_13 == True and persistent.end_14 == True and persistent.end_15 == True and persistent.end_16 == True:
        $ persistent.completionist = True

    $ renpy.save_persistent()

    $ evidence_selected = []

    show screen sc_end with fade
    ""(advance=False)
    return
