init:
    screen sc_room_frame():
        layer "under_master"
        add "images/black.png"
        viewport:
            ypos 100
            xpos 0
            transclude

## 0: Outside
    screen sc_room_0():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/outside.png"

## 1: officess Was Living Room/ livingroon
    screen sc_room_1():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/offices.png"
            imagebutton:
                style "interacter"
                auto "interactives/offices/%s/2.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_offices_2')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if prog == 1:
                    auto "interactives/offices/%s/3b.png"
                else:
                    auto "interactives/offices/%s/3a.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_offices_3')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/offices/%s/4.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_offices_4')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if prog == 0:
                    auto "interactives/offices/%s/1a.png"
                else:
                    auto "interactives/offices/%s/1b.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_offices_1')]
                else:
                    sensitive False
            if inferno:
                add "interactives/offices/5.png"

## 2: Reception was Parlor/parlor
    screen sc_room_2():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/reception.png"
            if not have_key:
                imagebutton:
                    style "interacter"
                    auto "interactives/reception/%s/1.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_reception_1')]
                    else:
                        sensitive False
            imagebutton:
                style "interacter"
                if not still_life:
                    auto "interactives/reception/%s/2a.png"
                else:
                    auto "interactives/reception/%s/2b.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_reception_2')]
                else:
                    sensitive False
            if not have_cash:
                imagebutton:
                    style "interacter"
                    auto "interactives/reception/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_reception_3')]
                    else:
                        sensitive False
            if siggy:
                add "interactives/reception/2c.png"

## 3: Corridor was Study / study
    screen sc_room_3():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/corridor.png"
            if not have_knife:
                imagebutton:
                    style "interacter"
                    auto "interactives/corridor/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_corridor_3')]
                    else:
                        sensitive False
            imagebutton:
                style "interacter"
                idle "billy"
                hover "interactives/corridor/hover/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_corridor_1')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/corridor/%s/2.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_corridor_2')]
                else:
                    sensitive False

## 4: Ceo was Bathroom \ bathroom
    screen sc_room_4():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/ceo.png"
            if not have_mask and not used_mask:
                imagebutton:
                    style "interacter"
                    auto "interactives/ceo/%s/2.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_ceo_2')]
                    else:
                        sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/ceo/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_ceo_1')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if trash_fire:
                    auto "interactives/ceo/%s/3b.png"
                else:
                    auto "interactives/ceo/%s/3a.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_ceo_3')]
                else:
                    sensitive False

## 5: Bunks was Bedroom
    screen sc_room_5():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/bunks.png"
            imagebutton:
                style "interacter"
                auto "interactives/bunks/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_bunks_1')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if summoning == 0:
                    auto "interactives/bunks/%s/2a.png"
                elif summoning == 1:
                    auto "interactives/bunks/%s/2b.png"
                else:
                    auto "interactives/bunks/%s/2c.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_bunks_2')]
                else:
                    sensitive False
            if clown_down:
                imagebutton:
                    style "interacter"
                    auto "interactives/bunks/%s/3d.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_bunks_3d')]
                    else:
                        sensitive False
            else:
                imagebutton:
                    style "interacter"
                    auto "interactives/bunks/%s/3a.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_bunks_3a')]
                    else:
                        sensitive False
                imagebutton:
                    style "interacter"
                    auto "interactives/bunks/%s/3b.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_bunks_3b')]
                    else:
                        sensitive False
                imagebutton:
                    style "interacter"
                    auto "interactives/bunks/%s/3c.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_bunks_3c')]
                    else:
                        sensitive False

## 6: Toilet Was Kitchen
    screen sc_room_6():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/toilet.png"
            imagebutton:
                style "interacter"
                auto "interactives/toilet/%s/2.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_toilet_2')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/toilet/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_toilet_1')]
                else:
                    sensitive False
            if cake_bake:
                add "interactives/toilet/1b.png"
            if not cake_prep:
                imagebutton:
                    style "interacter"
                    auto "interactives/toilet/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_toilet_3')]
                    else:
                        sensitive False

## 7: Staff Room
    screen sc_room_7():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/staffroom.png"
            imagebutton:
                style "interacter"
                if used_mask:
                    auto "interactives/staffroom/%s/1b.png"
                else:
                    auto "interactives/staffroom/%s/1a.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_staffroom_1')]
                else:
                    sensitive False
            if not have_ruler:
                imagebutton:
                    style "interacter"
                    auto "interactives/staffroom/%s/2.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_staffroom_2')]
                    else:
                        sensitive False
            if not have_candle:
                imagebutton:
                    style "interacter"
                    auto "interactives/staffroom/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_staffroom_3')]
                    else:
                        sensitive False
## 8: Security Room
    screen sc_room_8():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/securityroom.png"
            if not have_note:
                imagebutton:
                    style "interacter"
                    auto "interactives/securityroom/%s/1.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_securityroom_1')]
                    else:
                        sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/securityroom/%s/2.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_securityroom_2')]
                else:
                    sensitive False
            if not have_book:
                imagebutton:
                    style "interacter"
                    auto "interactives/securityroom/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_securityroom_3')]
                    else:
                        sensitive False
