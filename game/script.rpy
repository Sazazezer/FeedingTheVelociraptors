init -2:
    style say_thought:
        line_spacing 6
    style say_dialogue:
        line_spacing 6

default persistent.end_01 = False
default persistent.end_02 = False
default persistent.end_03 = False
default persistent.end_04 = False
default persistent.end_05 = False
default persistent.end_06 = False
default persistent.end_07 = False
default persistent.end_08 = False
default persistent.end_09 = False
default persistent.end_10 = False
default persistent.end_11 = False
default persistent.end_12 = False
default persistent.end_13 = False
default persistent.end_14 = False
default persistent.end_15 = False
default persistent.end_16 = False

default persistent.completionist = False

init:
## Remove the ability to hide windows, since the game leans on them pretty heavily.
    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['hide_windows'].remove('h')

    python:
## A simple function to set the active screen to match the player's location.
        def refresh_location():
            global location
            renpy.show_screen("sc_room_"+str(location))

## Reset persistent data
        def reset_persistent():
            persistent.end_01 = False
            persistent.end_02 = False
            persistent.end_03 = False
            persistent.end_04 = False
            persistent.end_05 = False
            persistent.end_06 = False
            persistent.end_07 = False
            persistent.end_08 = False
            persistent.end_09 = False
            persistent.end_10 = False
            persistent.end_11 = False
            persistent.end_12 = False
            persistent.end_13 = False
            persistent.end_14 = False
            persistent.end_15 = False
            persistent.end_16 = False
            persistent.completionist = False
            renpy.save_persistent()

## Debug only
        def get_persistent():
            persistent.end_01 = True
            persistent.end_02 = True
            persistent.end_03 = True
            persistent.end_04 = True
            persistent.end_05 = True
            persistent.end_06 = True
            persistent.end_07 = True
            persistent.end_08 = True
            persistent.end_09 = True
            persistent.end_10 = True
            persistent.end_11 = True
            persistent.end_12 = True
            persistent.end_13 = True
            persistent.end_14 = True
            persistent.end_15 = True
            persistent.end_16 = True
            persistent.completionist = True
            renpy.save_persistent()

## No rollback in a point-and-click
        config.rollback_enabled = False

## This is code from PyTom, which allows the tooltop to track the cursor. I don't understand a lick of it.
        class TrackCursor(renpy.Displayable):
            def __init__(self, child):
                super(TrackCursor, self).__init__()
                self.child = renpy.displayable(child)
                self.x = None
                self.y = None
            def render(self, width, height, st, at):
                rv = renpy.Render(width, height)
                if self.x is not None:
                    cr = renpy.render(self.child, width, height, st, at)
                    cw, ch = cr.get_size()
                    rv.blit(cr, (self.x - cw / 2, self.y - ch - 10))
                return rv
            def event(self, ev, x, y, st):
                if (x != self.x) or (y != self.y):
                    if x < 200:
                        self.x = 200
                    elif x > 1400:
                        self.x = 1400
                    else:
                        self.x = x
                    if y > 0:
                        self.y = y
                    renpy.redraw(self, 0)

#############
## Screens ##
#############
    screen sc_left_ui():
        zorder 3
        add "scene_frame.png" xpos 0 ypos 100
        text _("Feeding the Velociraptors") xpos 300 ypos 6 size 24 xalign 0.5 alt ""
        text location_index[location] xpos 300 ypos 50 size 42 xalign 0.5 alt ""

    screen sc_right_pane():
        zorder 3
        viewport:
            xysize (400,850)#(400,550)
            xalign 1.0
            ypos 100
            draggable False
            mousewheel False
            vbox:
                ypos 50
                xpos 50
                transclude
            add "ite_frame.png" ypos 0 xpos 0

    screen sc_evidence_pane():
        zorder 2
        tag rightpane
        use sc_right_pane():
            vpgrid:
                mousewheel False
                draggable False
                cols 2
                spacing 0
                side_xalign 0.0
#matt evidence
                if have_photo:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Human Photo?")
                        tooltip _("Human Photo?")

                        if "photo" in evidence_selected:
                            idle "evidence/photo_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"photo")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/photo.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"photo")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"photo"),Jump("finale")]
                            else:
                                action NullAction()
                if have_printout:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Printout")
                        tooltip _("Printout")

                        if "printout" in evidence_selected:
                            idle "evidence/printout_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"printout")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/printout.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"printout")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"printout"),Jump("finale")]
                            else:
                                action NullAction()
                if have_grenade:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Grenade")
                        tooltip _("Grenade")

                        if "grenade" in evidence_selected:
                            idle "evidence/grenade_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"grenade")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/grenade.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"grenade")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"grenade"),Jump("finale")]
                            else:
                                action NullAction()
                if have_dictaphone:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Dictaphone")
                        tooltip _("Dictaphone")

                        if "dictaphone" in evidence_selected:
                            idle "evidence/dictaphone_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"dictaphone")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/dictaphone.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"dictaphone")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"dictaphone"),Jump("finale")]
                            else:
                                action NullAction()
                if have_raptorclaw:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Raptor Claw")
                        tooltip _("Raptor Claw")

                        if "raptorclaw" in evidence_selected:
                            idle "evidence/raptorclaw_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"raptorclaw")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/raptorclaw.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"raptorclaw")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"raptorclaw"),Jump("finale")]
                            else:
                                action NullAction()
                if have_research:
                                    imagebutton:
                                        hover_sound "button_hover.wav"
                                        focus_mask True
                                        hovered NullAction()

                                        alt _("Research Journal?")
                                        tooltip _("Research Journal?")

                                        if "research" in evidence_selected:
                                            idle "evidence/research_select.png"
                                            if evidence_cue:
                                                action Function(evidence_selected.remove,"research")
                                            else:
                                                action NullAction()
                                        else:
                                            idle "evidence/research.png"
                                            if evidence_cue:
                                                activate_sound "button_select.wav"
                                                if len(evidence_selected) == 0:
                                                    action Function(evidence_selected.append,"research")
                                                else:
                                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"research"),Jump("finale")]
                                            else:
                                                action NullAction()    
                if have_wadofcash:
                                    imagebutton:
                                        hover_sound "button_hover.wav"
                                        focus_mask True
                                        hovered NullAction()

                                        alt _("Wad of Cash")
                                        tooltip _("Wad of Cash")

                                        if "wadofcash" in evidence_selected:
                                            idle "evidence/wadofcash_select.png"
                                            if evidence_cue:
                                                action Function(evidence_selected.remove,"wadofcash")
                                            else:
                                                action NullAction()
                                        else:
                                            idle "evidence/wadofcash.png"
                                            if evidence_cue:
                                                activate_sound "button_select.wav"
                                                if len(evidence_selected) == 0:
                                                    action Function(evidence_selected.append,"wadofcash")
                                                else:
                                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"wadofcash"),Jump("finale")]
                                            else:
                                                action NullAction()    
                if have_contract:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Assassin Contract")
                        tooltip _("Assassin Contract")

                        if "contract" in evidence_selected:
                            idle "evidence/contract_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"contract")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/contract.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"contract")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"contract"),Jump("finale")]
                            else:
                                action NullAction()    
                if have_fakePaper1:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Manufactured Evidence 1 of 2")
                        tooltip _("Manufactured Evidence 1 of 2")

                        if "fakepaper1" in evidence_selected:
                            idle "evidence/fakepaper_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"fakepaper1")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/fakepaper.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"fakepaper1")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"fakepaper1"),Jump("finale")]
                            else:
                                action NullAction()  
                if have_fakePaper2:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        hovered NullAction()

                        alt _("Manufactured Evidence 2 of 2")
                        tooltip _("Manufactured Evidence 2 of 2")

                        if "fakepaper2" in evidence_selected:
                            idle "evidence/fakepaper_select.png"
                            if evidence_cue:
                                action Function(evidence_selected.remove,"fakepaper2")
                            else:
                                action NullAction()
                        else:
                            idle "evidence/fakepaper.png"
                            if evidence_cue:
                                activate_sound "button_select.wav"
                                if len(evidence_selected) == 0:
                                    action Function(evidence_selected.append,"fakepaper2")
                                else:
                                    action [SetVariable("evidence_cue",False),Function(evidence_selected.append,"fakepaper2"),Jump("finale")]
                            else:
                                action NullAction() 
    screen sc_stuff_pane():
        zorder 2
        tag rightpane
        use sc_right_pane():
            vpgrid:
                mousewheel False
                draggable False
                cols 2
                spacing 0
                side_xalign 0.0

#matt stuff
                if have_crowbar:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/crowbar.png"
                        tooltip _("Crowbar")
                        alt _("Crowbar")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","crowbar"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_grenade:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/grenade.png"
                        tooltip _("Grenade")
                        alt _("Crowbar")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","grenade"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_ak47:
                                    imagebutton:
                                        hover_sound "button_hover.wav"
                                        focus_mask True
                                        idle "stuff/ak47.png"
                                        tooltip _("AK47")
                                        alt _("AK47")
                                        if stuff_cue:
                                            activate_sound "button_select.wav"
                                            action [SetVariable("stuff_selected","ak47"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                                        else:
                                            action NullAction()
                if have_fuelcan:
                                    imagebutton:
                                        hover_sound "button_hover.wav"
                                        focus_mask True
                                        idle "stuff/fuelcan.png"
                                        tooltip _("fuelcan")
                                        alt _("fuelcan")
                                        if stuff_cue:
                                            activate_sound "button_select.wav"
                                            action [SetVariable("stuff_selected","fuelcan"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                                        else:
                                            action NullAction()
                if have_idcard:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/idcard.png"
                        tooltip _("ID card")
                        alt _("ID card")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","idcard"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_hammer:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/hammer.png"
                        tooltip _("Hammer")
                        alt _("Hammer")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","hammer"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_blankPaper:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/blankpaper.png"
                        tooltip _("Blank Paper")
                        alt _("Blank Paper")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","blankPaper"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_adrianID:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/adrianid.png"
                        tooltip _("Adrian ID")
                        alt _("Adrian ID")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","adrianid"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
                if have_matchbox:
                    imagebutton:
                        hover_sound "button_hover.wav"
                        focus_mask True
                        idle "stuff/matchbox.png"
                        tooltip _("Matchbox")
                        alt _("Matchbox")
                        if stuff_cue:
                            activate_sound "button_select.wav"
                            action [SetVariable("stuff_selected","matchbox"),SetVariable("stuff_cue",False),Jump("stuff_check")]
                        else:
                            action NullAction()
    screen sc_buttons():
        zorder 3
        ## STUFF ##
        imagebutton:
            style "interacter"
            xpos 1000
            ypos 0
            if ev_bo:
                auto "buttons/widebutton_%s.png"
                action [Function(renpy.show_screen,"sc_stuff_pane"),SetVariable("ev_bo",False)]
            else:
                idle "buttons/widebutton_active.png"
            alt _("Stuff")

        ## EVIDENCE ##
        imagebutton:
            style "interacter"
            xpos 800
            ypos 0
            if not ev_bo:
                auto "buttons/widebutton_%s.png"
                action [Function(renpy.show_screen,"sc_evidence_pane"),SetVariable("ev_bo",True)]
            else:
                idle "buttons/widebutton_active.png"
            alt _("Evidence")

        vpgrid:
            mousewheel False
            draggable False
            cols 2
            spacing 0
            xpos 800
            ypos 0
            hbox:
                xysize (200,100)
                text _("EVIDENCE"):
                    color "#ffffff"
                    xalign 0.5
                    yalign 0.5
                    size 40
                    outlines [(3,'#413a3a',0,0)]
                    alt ""
                    if _preferences.language == "spanish":
                        if style.default.font == "SourceSansPro-Regular.ttf":
                            size 38
            hbox:
                xysize (200,100)
                text _("STUFF"):
                    color "#ffffff"
                    xalign 0.5
                    yalign 0.5
                    size 40
                    outlines [(3,'#413a3a',0,0)]
                    alt ""
                    if _preferences.language == "spanish":
                        if style.default.font == "SourceSansPro-Regular.ttf":
                            size 38

        ## THOSE ONES ##
        imagebutton:
            style "interacter"
            xpos 800
            ypos 900#650
            if interact_mode and prog == 2:
                auto "buttons/general_button_%s.png"
                action Function(renpy.show_screen,"sc_map")
            else:
                idle "buttons/general_button_idle.png"
            alt _("Open map")
        imagebutton:
            style "interacter"
            xpos 900
            ypos 900#650
            auto "buttons/general_button_%s.png"
            action ShowMenu('preferences')
            alt _("Options menu")
        imagebutton:
            style "interacter"
            xpos 1000
            ypos 900#650
            auto "buttons/general_button_%s.png"
            action ShowMenu('save')
            alt _("Save game")
        imagebutton:
            style "interacter"
            xpos 1100
            ypos 900#650
            auto "buttons/general_button_%s.png"
            action ShowMenu('help')
            alt _("Open help")
        vpgrid:
            mousewheel False
            draggable False
            cols 4
            spacing 0
            xpos 800
            ypos 900#650
            hbox:
                xysize (100,100)
                if interact_mode and prog == 2:
                    text _("MAP"):
                        style "duo"
                        alt ""
                        if _preferences.language == "spanish":
                            if style.default.font == "SourceSansPro-Regular.ttf":
                                size 18
                            else:
                                size 25
                else:
                    text _("MAP"):
                        style "duo"
                        alt ""
                        color "#555555"
                        if _preferences.language == "spanish":
                            if style.default.font == "SourceSansPro-Regular.ttf":
                                size 18
                            else:
                                size 25
            hbox:
                xysize (100,100)
                text _("MENU"):
                    style "duo"
                    alt ""
                    if _preferences.language == "spanish":
                        if style.default.font == "SourceSansPro-Regular.ttf":
                            size 18
                        else:
                            size 25
            hbox:
                xysize (100,100)
                text _("SAVE"):
                    style "duo"
                    alt ""
                    if _preferences.language == "spanish":
                        if style.default.font == "SourceSansPro-Regular.ttf":
                            size 18
                        else:
                            size 25
            hbox:
                xysize (100,100)
                text _("HELP"):
                    style "duo"
                    alt ""
                    if _preferences.language == "spanish":
                        if style.default.font == "SourceSansPro-Regular.ttf":
                            size 18
                        else:
                            size 25

    screen sc_map():
        zorder 50
        modal True
        add "black.png" xpos 0 ypos 0
        text _("Map") xpos 50 ypos 30 size 100
        hbox:
            xpos 50
            ypos 150
            text _("Current location: ")
            text location_index[location] xpos 10
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_toilet.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",6),Function(refresh_location),Jump("investistart")]
            alt _("Toilet")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_offices.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",1),Function(refresh_location),Jump("investistart")]
            alt _("Offices")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_reception.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",2),Function(refresh_location),Jump("investistart")]
            alt _("Reception")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_ceo.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",4),Function(refresh_location),Jump("investistart")]
            alt _("Ceo")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_bunks.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",5),Function(refresh_location),Jump("investistart")]
            alt _("Bunks")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_corridor.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",3),Function(refresh_location),Jump("investistart")]
            alt _("Corridor")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_securityroom.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",8),Function(refresh_location),Jump("investistart")]
            alt _("Security Office")
        imagebutton:
            style "interacter"
            xpos 0
            ypos 0
            auto "mappy/%s/m_staffroom.png"
            action [Function(renpy.hide_screen,"sc_map"),SetVariable("location",7),Function(refresh_location),Jump("investistart")]
            alt _("Staff Room")
        textbutton _("> Close map <"):
            hover_sound "button_hover.wav"
            activate_sound "button_select.wav"
            xpos 750
            ypos 650
            action [Function(renpy.hide_screen,"sc_map"),Jump("investistart")]
            text_style "closer"
            alt _("Close map")


        add "mappy/map_ov.png" xpos 0 ypos 0

        text _("") xpos 450 ypos 600 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 255 ypos 425 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 240 ypos 600 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 580 ypos 650 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""

        text _("") xpos 460 ypos 425 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 480 ypos 250 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 650 ypos 525 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""
        text _("") xpos 550 ypos 90 size 28 xanchor 0.5 outlines [(3,'#413a3a',0,0)] alt ""

    screen sc_tips():
        modal False
        zorder 6
        $ tooltip = GetTooltip()
        if tooltip:
            add TrackCursor(Text([tooltip], color = "fff", outlines = [(6, "#413a3a", 0, 0)], xmaximum = 200))

    screen sc_end():
        modal True
        zorder 50
        add "theend.png" xpos 0 ypos 0
        text _("THE END") xalign 0.5 ypos 100 size 180
        hbox:
            xalign 0.5
            ypos 300
            text _("Ending #")
            text route xpos 0
        if location == 0:
            textbutton _("> Try a different ending <"):
                hover_sound "button_hover.wav"
                activate_sound "button_select.wav"
                xalign 0.5
                ypos 500
                action [SetVariable("location",1),SetVariable("kickedOut",False),SetVariable("raptorRoomAK",False),SetVariable("raptorRoomGrenade",False),SetVariable("raptorRoomGrenadeNoPin",False),SetVariable("raptorRoomWadOfCash",False),Function(renpy.hide_screen,"sc_end"),Jump("investistart")]
                text_style "closer"
                alt _("Try a different ending")
        else:
            textbutton _("> Try a different set of evidence <"):
                hover_sound "button_hover.wav"
                activate_sound "button_select.wav"
                xalign 0.5
                ypos 500
                action [SetVariable("location",3),SetVariable("kickedOut",False),SetVariable("raptorRoomAK",False),SetVariable("raptorRoomGrenade",False),SetVariable("raptorRoomGrenadeNoPin",False),SetVariable("raptorRoomWadOfCash",False),Function(renpy.hide_screen,"sc_end"),Jump("investistart")]
                text_style "closer"
                alt _("Try a different set of evidence")
        textbutton _("> Exit to title screen <"):
            hover_sound "button_hover.wav"
            activate_sound "button_select.wav"
            xalign 0.5
            ypos 575
            action [Function(renpy.hide_screen,"sc_end"),MainMenu(confirm=False)]
            text_style "closer"
            alt _("Exit to title screen")

## STYLES ##
style closer:
    color "#FFFFFF"
    hover_color "#ffffff"
    idle_color "#aaaaaa"
    insensitive_color "#aaaaaa"
    size 30

style interacter:
    hover_sound "button_hover.wav"
    activate_sound "button_select.wav"
    focus_mask True

style duo:
    color "#ffffff"
    xalign 0.5
    yalign 0.5
    size 30
    outlines [(3,'#413a3a',0,0)]

## TRANSFORMS ##
transform basic:
    size (768,768) #600,450
    xpos 0
    ypos 100
    xzoom 1.0

## CHARACTERS ##
define p = Character(_('PAUL'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define a = Character(_('ADRIAN'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define h = Character(_('HELEN'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define t = Character(_('TONY'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define j = Character(_('JENNY'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define r = Character(_('RAPTOR'), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')
define n = Character(_(''), image='mono', what_prefix='"', what_suffix='"', color='#ffffff')


## SHAKES ##
image billy:
    "interactives/Corridor/idle/1b.png"
    7
    "interactives/Corridor/idle/1a.png"
    1
    repeat

## START
label start:
## Location variables
    $ location = 1
    $ location_index = [_("Outside"),_("Offices"),_("Reception"),_("Corridor"),_("Ceo"),_("Bunks"),_("Toilet"),_("Staff Room"),_("Security Room"),_("Temp Corridor"),("Outside")]

## Bool for whether the right pane is Evidence or Stuff
    $ ev_bo = True

## Logic variables used to navigate the point-and-click gameplay
    $ interact_mode = False
    $ stuff_cue = False
    $ evidence_cue = False

    $ interacting_with = ""
    $ req = ["",""]

    $ stuff_selected = ""
    $ evidence_selected = []

## Inventory variables
    $ have_knife = False
    $ have_gnome = False
    $ have_jaw = False
    $ have_wadofcash = False
    $ have_fish = False
    $ have_note = False

    $ have_gun = False
    $ have_mask = False
    $ have_book = False
    $ have_candle = False
    $ have_ruler = False
    $ have_key = False

    $ have_photo = False
    $ have_printout = False
    $ have_ak47 = False
    $ have_grenade = False
    $ have_poop = False
    $ have_crowbar = False
    #$ have_match = False
    $ have_fuelcan = False
    $ have_dictaphone = False
    $ have_idcard = False
    $ have_raptorclaw = False
    $ have_research = False
    $ have_wadofcash = False
    $ have_hammer = False
    $ have_contract = False
    $ have_blankPaper = False
    $ have_adrianID = False
    $ have_fakePaper1 = False
    $ have_fakePaper2 = False
    $ have_matchbox = False

## Other stuff
    $ evi_count = 0

    $ route = ""

    $ prog = 0
    $ unprog = 0

## matt variables  
    $ desk_check = 0
    $ receptionDoorsCheck = 0
    $ westTowerQuest = 0
    $ tonyincorridor = True
    $ raptorRoomAK = False
    $ raptorRoomGrenade = False
    $ raptorRoomGrenadeNoPin = False
    $ raptorRoomWadOfCash = False
    $ kickedOut = False
    $ filingCabinetOpen = False
    $ playWithGrenade = 0
    $ lookOutsideReception = False
    $ securityCabinetClosed = True
    $ fuelApplied = False
    $ matchApplied = False
    $ showIDCard = False
    $ tonyChestOpen = False
    $ globeSmashed = False
    $ showAdrianID = False
    $ viewSecurityPanel = False
    $ ak47Scare = False
    $ monitorCheck = False
    $ monitorCheckStop = False
    $ corridorCheck1 = 0
    $ checkCEO2 = 0
    $ hideTempTony = False
    $ checkBunks4 = 0
    # security room puzzle
    $ securityPuzzleOpen = False
    $ adrianAccused = False
    $ currentPuzzleState = 0
    $ puzzleFailedAttempts = 0

    # Pertaining to this and that
    $ used_mask = False
    $ paint_talk = False
    $ siggy = False
    # Pertaining to the secret ending
    $ summoning = 0
    $ trash_fire = False
    $ cake_prep = False
    $ cake_bake = False
    $ still_life = False
    $ fire_count = 0
    $ inferno = False
    # Pertaining to the stupid clown puzzle
    $ clowning_around = 0
    $ hint_get = False
    $ big_hint = 0
    $ clown_down = False
    $ clown_code = [0,0,0]

###########
## Start ##
###########
    scene bg_transparent
    show mono empty at basic zorder 1
    show screen sc_buttons
    show screen sc_evidence_pane
    show screen sc_left_ui
    show screen sc_tips
    show screen sc_room_frame

    ">>> How to play:\n>>> Press \[SPACE\] or \[LEFT CLICK\] to begin and to advance text.{fast}"

    $ refresh_location()
    jump falsestart
