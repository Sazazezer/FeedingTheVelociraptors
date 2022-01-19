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
        j jneutral "Alright, that's one piece of evidence down."
        j jthink "I think I should get at least one more before I go and confront Alexandre."
    elif evi_count == 2:
        j jneutral "Anyway, that makes two pieces of evidence."
        j jsmug "I should be able to figure out what Alexandre's up to with this."
        j jthink "Still, maybe gathering a little more evidence could be useful?"
    elif evi_count == 6:
        j jthink "Now, let's see . . ."
        j jneutral "Wow, that's six pieces of evidence!"
        j jdoubt "I seriously doubt there's anything else useful left in this trash heap."
        j jneutral "Better go confront Alexandre and get it done with."
    jump investistart

label fire_tally:
    if fire_count == 4:
        j jdoubt "Wait, what's that smell?"
        j "Is it just me, or is it starting to get kinda smoky in here?"
        j jthink "What a mysterious phenomenon . . ."
        j ". . ."
        j jgrim "Okay, in hindsight, maybe not that mysterious."
        j "Guess I'd better go find that fire extinguisher . . ."
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
            j jterror "oh god i don't think that's gonna work"
        else:
            j jgrim "I don't think that's gonna work."
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

    j jthink "Hmmm. Actually, I'm gonna need another minute."
    a aalarm "Wait! Don't just leave me here!"

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
