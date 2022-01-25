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
                auto "interactives/offices/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_offices_1')]
                else:
                    sensitive False


## 2: Reception was Parlor/parlor
    screen sc_room_2():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/reception.png"
            imagebutton:
                style "interacter"
                auto "interactives/reception/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_reception_1')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if filingCabinetOpen:
                    auto "interactives/reception/%s/2a.png"
                else:
                    auto "interactives/reception/%s/2b.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_reception_2')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                auto "interactives/reception/%s/3.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_reception_3')]
                else:
                    sensitive False
            if siggy:
                add "interactives/reception/2c.png"
            if lookOutsideReception:
                imagebutton:
                    style "interacter"
                    auto "interactives/reception/%s/4.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_reception_1')]
                    else:
                        sensitive False

## 3: Corridor was Study / study
    screen sc_room_3():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/corridor.png"
            if not have_fuelcan:
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
            if not have_match:
                imagebutton:
                    style "interacter"
                    auto "interactives/ceo/%s/6.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_ceo_6')]
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
                if fuelApplied and matchApplied:
                    auto "interactives/bunks/%s/2c.png"
                elif fuelApplied and not matchApplied:
                    auto "interactives/bunks/%s/2b.png"
                else:
                    auto "interactives/bunks/%s/2a.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_bunks_2')]
                else:
                    sensitive False
            imagebutton:
                    style "interacter"
                    auto "interactives/bunks/%s/3.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_bunks_3')]
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
            if not have_crowbar:
                imagebutton:
                    style "interacter"
                    auto "interactives/toilet/%s/3a.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('check_toilet_3')]
                    else:
                        sensitive False
            else:
                imagebutton:
                    style "interacter"
                    auto "interactives/toilet/%s/3b.png"
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

## 8: Security Room
    screen sc_room_8():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/securityroom.png"
            imagebutton:
                style "interacter"
                auto "interactives/securityroom/%s/1.png"
                if interact_mode:
                    action [SetVariable("interact_mode",False),Jump('check_securityroom_1')]
                else:
                    sensitive False
            imagebutton:
                style "interacter"
                if not securityCabinetClosed and have_AK47:
                    auto "interactives/securityroom/%s/2c.png"
                elif not securityCabinetClosed and not have_AK47:
                    auto "interactives/securityroom/%s/2b.png"
                else:
                    auto "interactives/securityroom/%s/2a.png"
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
## 9: Temporary version of the corridor for early scene
    screen sc_room_9():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/corridor.png"
            if tonyincorridor:
                imagebutton:
                    style "interacter"
                    auto "interactives/corridor/%s/temp.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('temp_corridor')]
                    else:
                        sensitive False
## 10: Raptor room
    screen sc_room_10():
        tag room_screen
        layer "under_master"
        use sc_room_frame():
            add "site/raptorroom.png"
            
            if not kickedOut:
                imagebutton:
                    style "interacter"
                    auto "interactives/corridor/%s/temp.png" #!!fix!
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('raptorroom')]
                    else:
                        sensitive False
            if raptorRoomAK:
                imagebutton:
                    style "interacter"
                    auto "interactives/raptorroom/%s/ak.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('temp_corridor')]
                    else:
                        sensitive False
            if raptorRoomGrenade:
                imagebutton:
                    style "interacter"
                    auto "interactives/raptorroom/%s/grenade.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('temp_corridor')]
                    else:
                        sensitive False
            if raptorRoomGrenadeNoPin:
                imagebutton:
                    style "interacter"
                    auto "interactives/raptorroom/%s/grenadenopin.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('temp_corridor')]
                    else:
                        sensitive False
            if raptorRoomWadOfCash:
                imagebutton:
                    style "interacter"
                    auto "interactives/raptorroom/wadofcash.png"
                    if interact_mode:
                        action [SetVariable("interact_mode",False),Jump('temp_corridor')]
                    else:
                        sensitive False