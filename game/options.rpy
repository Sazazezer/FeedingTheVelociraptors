init -1 python hide:
## MUNRO ##
    renpy.register_style_preference(
        "text", "Default", style.say_dialogue, "size", 24)
    renpy.register_style_preference(
        "text", "Default", style.say_dialogue, "line_spacing", 6)
    renpy.register_style_preference(
        "text", "Default", style.say_dialogue, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.say_label, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.default, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.gui_text, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.gui_medium_button_text, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.navigation_text, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.navigation_button_text, "font", "munro.ttf")
    renpy.register_style_preference(
        "text", "Default", style.gui_button_text, "font", "munro.ttf")

## VT323 ##
    renpy.register_style_preference(
        "text", "VT323", style.say_dialogue, "size", 24)
    renpy.register_style_preference(
        "text", "VT323", style.say_dialogue, "line_spacing", 6)
    renpy.register_style_preference(
        "text", "VT323", style.say_dialogue, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.say_label, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.default, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.gui_text, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.gui_medium_button_text, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.navigation_text, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.navigation_button_text, "font", "VT323-Regular.ttf")
    renpy.register_style_preference(
        "text", "VT323", style.gui_button_text, "font", "VT323-Regular.ttf")

## SOURCE SANS PRO ##
    renpy.register_style_preference(
        "text", "Sans Serif", style.say_dialogue, "size", 22)
    renpy.register_style_preference(
        "text", "Sans Serif", style.say_dialogue, "line_spacing", 1)
    renpy.register_style_preference(
        "text", "Sans Serif", style.say_dialogue, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.say_label, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.default, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.gui_text, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.gui_medium_button_text, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.navigation_text, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.navigation_button_text, "font", "SourceSansPro-Regular.ttf")
    renpy.register_style_preference(
        "text", "Sans Serif", style.gui_button_text, "font", "SourceSansPro-Regular.ttf")

## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

define config.equal_mono = False

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Feeding the Velociraptors")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.1"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
                      Excuse for a story, sloppy art and general code by Sazazezer (Matt Staples) - 2022.

                      Heavily modified from the base game 'Jam and the mystery of the mysteriously spooky mansion' by Res (Ray Clark) - (Go play it it's awesome)

                      https://arc-res.itch.io/jam-and-the-mystery-of-the-mysteriously-spooky-mansion

                      Music by Leon Spencer.

                      All fonts licensed under the SIL Open Font License, Version 1.1. The full text of the license is included as a .txt document in the game files.

                      VT323: Copyright 2011, The VT323 Project Authors (peter.hull@oikoi.com). Available at https://fonts.google.com/specimen/VT323

                      Munro: Copyright 2007 - 2020, Ten by Twenty. Available at https://www.fontsquirrel.com/fonts/munro

                      Sans Source Pro: Copyright 2010, 2012, Adobe Systems Incorporated (http://www.adobe.com/), with Reserved Font Name ‘Source’. Available at https://fonts.google.com/specimen/Source+Sans+Pro
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "FTV"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "FTV-B.wav"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "ftv-1567964321"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
