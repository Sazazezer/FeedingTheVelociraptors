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

label evi_tally:
    if evi_count == 1:
        p "I'm no fool though."
        p "I know i need at least two pieces of watertight evidence in order to pin this on someone."
        p "And one piece is all leaky and stuff."
    elif evi_count == 2:
        p "Excellent. Two pieces of evidence."
        p "That's more than enough to make some kind of accusation."
        p "I could always look for more though."
        p "Maybe make the accusation valid."
    elif evi_count == 8:
        p "I can safetly say with absolute certainly..."
        p "Almost s if the god of this world was speaking through me..."
        p "That all the evidence has definitely been found."
        p "That being said..."
        p "There's more than one way to obtain evidence beyond merely 'finding' it."
        p "Heh heh heh."
        p "I wonder why i don't have any friends."
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
    p "So… i guess i should sneak back out of the room before anyone asks what i’m dong back here again?"
    t "You do realise we can all hear you right?"
    p "NO YOU CAN’T!"
    jump investistart

label finale:
    #if "gnome" in evidence_selected and "knife" in evidence_selected:
    #    $ route = _("3/16: The Gutter of Depravity")
    #    jump route01
    if "photo" in evidence_selected and "printout" in evidence_selected:
        $ route = _("3/16: Definitely Adrian's fault") #!! maybe rephrase for the adrian forgery ending
        jump route01
    elif "gnome" in evidence_selected and "cash" in evidence_selected:
        $ route = _("2/16: Lucky Benny’s House of Gnomes")
        jump route02
    elif "gnome" in evidence_selected and "jaw" in evidence_selected:
        $ route = _("13/16: The Necrognomicon")
        jump route03
    elif "gnome" in evidence_selected and "fish" in evidence_selected:
        $ route = _("12/16: Schrodinger’s KFC/Taco Bell")
        jump route04
    elif "gnome" in evidence_selected and "note" in evidence_selected:
        $ route = _("7/16: Gnome Crime Doesn’t Pay")
        jump route05
    elif "jaw" in evidence_selected and "cash" in evidence_selected:
        $ route = _("14/16: Inspector Valjert")
        jump route06
    elif "jaw" in evidence_selected and "fish" in evidence_selected:
        $ route = _("5/16: Red Herring")
        jump route07
    elif "jaw" in evidence_selected and "note" in evidence_selected:
        $ route = _("6/16: Palexandre")
        jump route08
    elif "jaw" in evidence_selected and "knife" in evidence_selected:
        $ route = _("15/16: The Perfect Crime")
        jump route09
    elif "fish" in evidence_selected and "note" in evidence_selected:
        $ route = _("1/16: O Canada")
        jump route10
    elif "fish" in evidence_selected and "cash" in evidence_selected:
        $ route = _("10/16: La Fin")
        jump route11
    elif "fish" in evidence_selected and "knife" in evidence_selected:
        $ route = _("8/16: A Raw Deal")
        jump route12
    elif "knife" in evidence_selected and "cash" in evidence_selected:
        $ route = _("4/16: Not Illegal; Still Kinda Weird")
        jump route13
    elif "knife" in evidence_selected and "note" in evidence_selected:
        $ route = _("11/16: Westside of Linn County Story")
        jump route14
    elif "cash" in evidence_selected and "note" in evidence_selected:
        $ route = _("9/16: The Escargot Debacle")
        jump route15
    else:
        j jdoubt "Hey, you. Yeah, you, at the computer."
        j janger "I think you broke the game."
        jump investistart

label endcard:
    $ interact_mode = False
    $ evidence_cue = False
    $ stuff_cue = False

    if "photo" in evidence_selected and "printout" in evidence_selected:
        $ persistent.end_03 = True
    elif "gnome" in evidence_selected and "cash" in evidence_selected:
        $ persistent.end_02 = True
    elif "gnome" in evidence_selected and "jaw" in evidence_selected:
        $ persistent.end_13 = True
    elif "gnome" in evidence_selected and "fish" in evidence_selected:
        $ persistent.end_12 = True
    elif "gnome" in evidence_selected and "note" in evidence_selected:
        $ persistent.end_07 = True
    elif "jaw" in evidence_selected and "cash" in evidence_selected:
        $ persistent.end_14 = True
    elif "jaw" in evidence_selected and "fish" in evidence_selected:
        $ persistent.end_05 = True
    elif "jaw" in evidence_selected and "note" in evidence_selected:
        $ persistent.end_06 = True
    elif "jaw" in evidence_selected and "knife" in evidence_selected:
        $ persistent.end_15 = True
    elif "fish" in evidence_selected and "note" in evidence_selected:
        $ persistent.end_01 = True
    elif "fish" in evidence_selected and "cash" in evidence_selected:
        $ persistent.end_10 = True
    elif "fish" in evidence_selected and "knife" in evidence_selected:
        $ persistent.end_08 = True
    elif "knife" in evidence_selected and "cash" in evidence_selected:
        $ persistent.end_04 = True
    elif "knife" in evidence_selected and "note" in evidence_selected:
        $ persistent.end_11 = True
    elif "cash" in evidence_selected and "note" in evidence_selected:
        $ persistent.end_09 = True
    else:
        $ persistent.end_16 = True

    if persistent.end_01 == True and persistent.end_02 == True and persistent.end_03 == True and persistent.end_04 == True and persistent.end_05 == True and persistent.end_06 == True and persistent.end_07 == True and persistent.end_08 == True and persistent.end_09 == True and persistent.end_10 == True and persistent.end_11 == True and persistent.end_12 == True and persistent.end_13 == True and persistent.end_14 == True and persistent.end_15 == True and persistent.end_16 == True:
        $ persistent.completionist = True

    $ renpy.save_persistent()

    $ evidence_selected = []

    show screen sc_end with fade
    ""(advance=False)
    return
