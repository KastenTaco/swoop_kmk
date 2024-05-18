print("Starting")

import board

from storage import getmount

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
#from kb import data_pin
from kmk.modules.split import Split, SplitSide
from kmk.modules.holdtap import HoldTap
from kmk.modules.holdtap import HoldTapRepeat
from kmk.modules.tapdance import TapDance
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.capsword import CapsWord



keyboard = KMKKeyboard()  

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())

combos = Combos()
keyboard.modules.append(combos)

keyboard.col_pins = (board.D22, board.D26, board.D27, board.D28, board.D29,)
keyboard.row_pins = (board.D4, board.D5, board.D6, board.D7,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# TODO Comment one of these on each side
split_side = SplitSide.LEFT if str(getmount('/').label)[-1] == 'L' else SplitSide.RIGHT

#split_side = SplitSide.RIGHT
split = Split(
    split_flip=True,
    split_side=split_side,
    uart_flip=True,
    use_pio=True,
    data_pin=board.D1,
    data_pin2=board.D0,
)

keyboard.modules.append(split)  # type: ignore sd

# coord_mapping = [
#     0,  1,  2,  3,  4,  18, 19, 20, 21, 22,
#     5,  6,  7,  8,  9,  23, 24, 25, 26, 27,
#    10, 11, 12, 13, 14,  28, 29, 30, 31, 32,
#            15, 16, 17,  33, 34, 35,
#]

#configure holdtap
holdtap = HoldTap()
holdtap.tap_time = 200
holdtap.tap_interrupted = True
holdtap.repeat = HoldTapRepeat.TAP
keyboard.modules.append(holdtap)

#configure tapdance
tapdance = TapDance()
tapdance.tap_time = 200
keyboard.modules.append(tapdance)

#configure MouseMovement
mousekeys = MouseKeys(
    max_speed = 100,
    acc_interval = 500, # Delta ms to apply acceleration
    move_step = 1
)
keyboard.modules.append(MouseKeys())

#CapsWord
caps_word=CapsWord()
keyboard.modules.append(caps_word)

#Homerow Mods
# Left side
F_SHIFT = KC.HT(KC.F, KC.LSFT, prefer_hold=False, tap_time=200)
D_CTRL = KC.HT(KC.D, KC.LCTRL, prefer_hold=False, tap_time=300)
S_ALT = KC.HT(KC.S, KC.LALT, prefer_hold=False, tap_time=300)
Z_GUI = KC.HT(KC.Z, KC.LWIN, prefer_hold=False, tap_time=300)

# Right side
J_SHIFT = KC.HT(KC.J, KC.LSFT, prefer_hold=False, tap_time=200)
K_CTRL = KC.HT(KC.K, KC.LCTRL, prefer_hold=False, tap_time=300)
L_ALT = KC.HT(KC.L, KC.LALT, prefer_hold=False, tap_time=300)
SLASH_GUI = KC.HT(KC.SLSH, KC.LWIN, prefer_hold=False, tap_time=300)


combos.combos = [
    #Select all
    Chord((KC.A, S_ALT), KC.LCTL(KC.A)),
    #Undo
    Chord((KC.W, KC.E), KC.LCTL(KC.Z)),
    #Redo
    Chord((KC.E, KC.R), KC.LCTL(KC.Y)),
    #Cut
    Chord((KC.X, KC.C), KC.LCTL(KC.X)),
    #Copy
    Chord((KC.C, KC.V), KC.LCTL(KC.C)),
    #Paste
    Chord((KC.V, KC.B), KC.LCTL(KC.V)),
    #Refresh
    Chord((KC.Y, KC.U), KC.F5),
    #Apos
    Chord((L_ALT, KC.SCOLON), KC.QUOT),
    #CapsWord
    Chord((F_SHIFT, J_SHIFT), KC.CW),
]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

keyboard.keymap = [
    #[0] QWERT BASE Layer 
    [KC.Q,     KC.W,     KC.E,                KC.R,                KC.T,                        KC.Y,                  KC.U,                KC.I,                KC.O,                               KC.P,
     KC.A,     S_ALT,    D_CTRL,              F_SHIFT,             KC.G,                        KC.H,                  J_SHIFT,             K_CTRL,              L_ALT,                              KC.SCOLON,
     Z_GUI,    KC.X,     KC.C,                KC.V,                KC.B,                        KC.N,                  KC.M,                KC.COMMA,            KC.DOT,                             SLASH_GUI,
     XXXXXXX,  XXXXXXX,  KC.LT((3), KC.ESC),  KC.LT((4), KC.ENT),  KC.LT((5), KC.TAB),          KC.LT((6), KC.BSPC),   KC.LT((7), KC.SPC),  KC.LT((8), KC.DEL),  XXXXXXX,                            XXXXXXX,
    ],
    #[1] GAME BASE Layer 
    [KC.TAB,                KC.Q,     KC.W,                 KC.E,                     KC.R,                             _______,   _______,  _______,  _______,  _______,
     KC.HT(KC.G, KC.LSFT),  KC.A,     KC.S,                 KC.D,                     KC.F,                             _______,   _______,  _______,  _______,  _______,
     KC.LCTRL,              KC.X,     KC.C,                 KC.V,                     KC.B,                             _______,   _______,  _______,  _______,  _______,
     XXXXXXX,               XXXXXXX,  KC.HT(KC.ESC, KC.M),  KC.HT(KC.ENT, KC.MO(2)),  KC.HT(KC.SPC, KC.MO(5)),          _______,   _______,  _______,  XXXXXXX,  XXXXXXX,
    ],
    #[2] GAMENUM Layer 
    [KC.N1,     KC.N2,    KC.N3,    KC.N4,    KC.N5,            KC.N6,     KC.N7,    KC.N8,    KC.N9,    KC.N0,
     _______,   _______,  _______,  _______,  _______,          _______,   _______,  _______,  _______,  _______,
     _______,   _______,  _______,  _______,  _______,          _______,   _______,  _______,  _______,  _______,
     XXXXXXX,   XXXXXXX,  _______,  _______,  _______,          _______,   _______,  _______,  XXXXXXX,  XXXXXXX,
    ],
    #[3] MEDIA Layer 
    [_______,   _______,  _______,  _______,  _______,          KC.R,     KC.M,     KC.H,     KC.S,     KC.V,
     _______,   _______,  _______,  _______,  _______,          KC.E,     KC.MPRV,  KC.VOLD,  KC.VOLU,  KC.MNXT,
     _______,   _______,  _______,  _______,  _______,          KC.O,     KC.N0,    KC.N1,    KC.N2,    KC.N3,
     XXXXXXX,   XXXXXXX,  _______,  _______,  _______,          KC.MSTP,  KC.MPLY,  KC.MUTE,  XXXXXXX,  XXXXXXX,
    ],
    #[4] NAVIGATION Layer 
    [KC.PAST,   KC.N7,    KC.N8,    KC.N9,    KC.PSLS,        KC.LCTL(KC.Z),  KC.LCTL(KC.X),  KC.LCTL(KC.C),  KC.LCTL(KC.V),  KC.LCTL(KC.Y),
     KC.PSLS,   KC.N4,    KC.N5,    KC.N6,    KC.PMNS,        KC.CAPS,        KC.HOME,        KC.UP,          KC.END,         KC.PGUP,
     KC.PDOT,   KC.N1,    KC.N2,    KC.N3,    KC.N0,          KC.INS,         KC.LEFT,        KC.DOWN,        KC.RIGHT,       KC.PGDN,
     XXXXXXX,   XXXXXXX,  KC.BSPC,  _______,  KC.DEL,         _______,        _______,        _______,        XXXXXXX,        XXXXXXX,
    ],
    #[5] MOUSE Layer 
    [KC.LCTL(KC.Z),  KC.LCTL(KC.X),  KC.LCTL(KC.C),  KC.LCTL(KC.V),  KC.HT(KC.LCTL(KC.Y), KC.PSCR),       KC.LCTL(KC.Z),  KC.LCTL(KC.X),  KC.LCTL(KC.C),  KC.LCTL(KC.V),  KC.LCTL(KC.Y),
     KC.LEFT,        KC.MB_LMB,      KC.MS_UP,       KC.MB_RMB,      KC.MW_UP,                            KC.LEFT,        KC.MB_LMB,      KC.MS_UP,       KC.MB_RMB,      KC.MW_UP,
     KC.RIGHT,       KC.MS_LT,       KC.MS_DN,       KC.MS_RT,       KC.MW_DN,                            KC.RIGHT,       KC.MS_LT,       KC.MS_DN,       KC.MS_RT,       KC.MW_DN,
     XXXXXXX,        XXXXXXX,        KC.TO(0),       KC.TO(1),       KC.DEL,                              KC.MB_LMB,      KC.MB_MMB,      KC.MB_RMB,      XXXXXXX,        XXXXXXX,
    ],
    #[6] SYMBOL Layer 
    [KC.LCBR,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RCBR,          _______,   _______,  _______,  _______,  _______,
     KC.COLN,  KC.DLR,   KC.PERC,  KC.CIRC,  KC.PLUS,          _______,   _______,  _______,  _______,  _______,
     KC.TILD,  KC.EXLM,  KC.AT,    KC.HASH,  KC.PIPE,          _______,   _______,  _______,  _______,  _______,
     XXXXXXX,  XXXXXXX,  KC.LPRN,  KC.RPRN,  KC.UNDS,          _______,   _______,  _______,  XXXXXXX,  XXXXXXX,
    ],
    #[7] NUMBER Layer 
    [KC.LBRC,   KC.N7,    KC.N8,    KC.N9,    KC.RBRC,        KC.PSLS,   KC.N7,    KC.N8,    KC.N9,    KC.PAST,
     KC.SCLN,   KC.N4,    KC.N5,    KC.N6,    KC.EQL,         KC.PMNS,   KC.N4,    KC.N5,    KC.N6,    KC.SLS,
     KC.GRV,    KC.N1,    KC.N2,    KC.N3,    KC.BSLS,        KC.N0,     KC.N1,    KC.N2,    KC.N3,    KC.PDOT,
     XXXXXXX,   XXXXXXX,  KC.DOT,   KC.N0,    KC.MINS,        _______,   _______,  _______,  XXXXXXX,  XXXXXXX,
    ],
    #[8] FUNCTION Layer 
    [KC.F12,   KC.F7,    KC.F8,     KC.F9,     KC.PSCR,        KC.RLD,    KC.RESET,  _______,  _______,  _______,
     KC.F11,   KC.F4,    KC.F5,     KC.F6,     KC.SLCK,        _______,   _______,   _______,  _______,  _______,
     KC.F10,   KC.F1,    KC.F2,     KC.F3,     KC.PAUS,        _______,   _______,   _______,  _______,  _______,
     XXXXXXX,  XXXXXXX,  KC.TO(0),  KC.TO(1),  _______,        _______,   _______,   _______,  XXXXXXX,  XXXXXXX,
    ],

]

if __name__ == '__main__':
    keyboard.go()
