from pygame import image

animations = {
    "death": {
        "attack": {
            "blood": {
                "no": {
                    "back": [image.load("../animation/death/attack/blood/no/back/0.png"),
                             image.load("../animation/death/attack/blood/no/back/1.png"),
                             image.load("../animation/death/attack/blood/no/back/2.png"),
                             image.load("../animation/death/attack/blood/no/back/3.png")],

                    "front": [image.load("../animation/death/attack/blood/no/front/0.png"),
                              image.load("../animation/death/attack/blood/no/front/1.png"),
                              image.load("../animation/death/attack/blood/no/front/2.png"),
                              image.load("../animation/death/attack/blood/no/front/3.png")],

                    "left": [image.load("../animation/death/attack/blood/no/left/0.png"),
                             image.load("../animation/death/attack/blood/no/left/1.png"),
                             image.load("../animation/death/attack/blood/no/left/2.png"),
                             image.load("../animation/death/attack/blood/no/left/3.png")],

                    "right": [image.load("../animation/death/attack/blood/no/right/0.png"),
                              image.load("../animation/death/attack/blood/no/right/1.png"),
                              image.load("../animation/death/attack/blood/no/right/2.png"),
                              image.load("../animation/death/attack/blood/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/attack/blood/crown/back/0.png"),
                             image.load("../animation/death/attack/blood/crown/back/1.png"),
                             image.load("../animation/death/attack/blood/crown/back/2.png"),
                             image.load("../animation/death/attack/blood/crown/back/3.png")],

                    "front": [image.load("../animation/death/attack/blood/crown/front/0.png"),
                              image.load("../animation/death/attack/blood/crown/front/1.png"),
                              image.load("../animation/death/attack/blood/crown/front/2.png"),
                              image.load("../animation/death/attack/blood/crown/front/3.png")],

                    "left": [image.load("../animation/death/attack/blood/crown/left/0.png"),
                             image.load("../animation/death/attack/blood/crown/left/1.png"),
                             image.load("../animation/death/attack/blood/crown/left/2.png"),
                             image.load("../animation/death/attack/blood/crown/left/3.png")],

                    "right": [image.load("../animation/death/attack/blood/crown/right/0.png"),
                              image.load("../animation/death/attack/blood/crown/right/1.png"),
                              image.load("../animation/death/attack/blood/crown/right/2.png"),
                              image.load("../animation/death/attack/blood/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/attack/blood/rage/back/0.png"),
                             image.load("../animation/death/attack/blood/rage/back/1.png"),
                             image.load("../animation/death/attack/blood/rage/back/2.png"),
                             image.load("../animation/death/attack/blood/rage/back/3.png")],

                    "front": [image.load("../animation/death/attack/blood/rage/back/0.png"),
                              image.load("../animation/death/attack/blood/rage/back/1.png"),
                              image.load("../animation/death/attack/blood/rage/back/2.png"),
                              image.load("../animation/death/attack/blood/rage/back/3.png")],

                    "left": [image.load("../animation/death/attack/blood/rage/left/0.png"),
                             image.load("../animation/death/attack/blood/rage/left/1.png"),
                             image.load("../animation/death/attack/blood/rage/left/2.png"),
                             image.load("../animation/death/attack/blood/rage/left/3.png")],

                    "right": [image.load("../animation/death/attack/blood/rage/right/0.png"),
                              image.load("../animation/death/attack/blood/rage/right/1.png"),
                              image.load("../animation/death/attack/blood/rage/right/2.png"),
                              image.load("../animation/death/attack/blood/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/attack/blood/full/back/0.png"),
                             image.load("../animation/death/attack/blood/full/back/1.png"),
                             image.load("../animation/death/attack/blood/full/back/2.png"),
                             image.load("../animation/death/attack/blood/full/back/3.png")],

                    "front": [image.load("../animation/death/attack/blood/full/front/0.png"),
                              image.load("../animation/death/attack/blood/full/front/1.png"),
                              image.load("../animation/death/attack/blood/full/front/2.png"),
                              image.load("../animation/death/attack/blood/full/front/3.png")],

                    "left": [image.load("../animation/death/attack/blood/full/left/0.png"),
                             image.load("../animation/death/attack/blood/full/left/1.png"),
                             image.load("../animation/death/attack/blood/full/left/2.png"),
                             image.load("../animation/death/attack/blood/full/left/3.png")],

                    "right": [image.load("../animation/death/attack/blood/full/right/0.png"),
                              image.load("../animation/death/attack/blood/full/right/1.png"),
                              image.load("../animation/death/attack/blood/full/right/2.png"),
                              image.load("../animation/death/attack/blood/full/right/3.png")]
                }
            },
            "sickle": {
                "no": {
                    "back": [image.load("../animation/death/attack/sickle/no/back/0.png"),
                             image.load("../animation/death/attack/sickle/no/back/1.png"),
                             image.load("../animation/death/attack/sickle/no/back/2.png"),
                             image.load("../animation/death/attack/sickle/no/back/3.png")],

                    "front": [image.load("../animation/death/attack/sickle/no/front/0.png"),
                              image.load("../animation/death/attack/sickle/no/front/1.png"),
                              image.load("../animation/death/attack/sickle/no/front/2.png"),
                              image.load("../animation/death/attack/sickle/no/front/3.png")],

                    "left": [image.load("../animation/death/attack/sickle/no/left/0.png"),
                             image.load("../animation/death/attack/sickle/no/left/1.png"),
                             image.load("../animation/death/attack/sickle/no/left/2.png"),
                             image.load("../animation/death/attack/sickle/no/left/3.png")],

                    "right": [image.load("../animation/death/attack/sickle/no/right/0.png"),
                              image.load("../animation/death/attack/sickle/no/right/1.png"),
                              image.load("../animation/death/attack/sickle/no/right/2.png"),
                              image.load("../animation/death/attack/sickle/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/attack/sickle/crown/back/0.png"),
                             image.load("../animation/death/attack/sickle/crown/back/1.png"),
                             image.load("../animation/death/attack/sickle/crown/back/2.png"),
                             image.load("../animation/death/attack/sickle/crown/back/3.png")],

                    "front": [image.load("../animation/death/attack/sickle/crown/front/0.png"),
                              image.load("../animation/death/attack/sickle/crown/front/1.png"),
                              image.load("../animation/death/attack/sickle/crown/front/2.png"),
                              image.load("../animation/death/attack/sickle/crown/front/3.png")],

                    "left": [image.load("../animation/death/attack/sickle/crown/left/0.png"),
                             image.load("../animation/death/attack/sickle/crown/left/1.png"),
                             image.load("../animation/death/attack/sickle/crown/left/2.png"),
                             image.load("../animation/death/attack/sickle/crown/left/3.png")],

                    "right": [image.load("../animation/death/attack/sickle/crown/right/0.png"),
                              image.load("../animation/death/attack/sickle/crown/right/1.png"),
                              image.load("../animation/death/attack/sickle/crown/right/2.png"),
                              image.load("../animation/death/attack/sickle/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/attack/sickle/rage/back/0.png"),
                             image.load("../animation/death/attack/sickle/rage/back/1.png"),
                             image.load("../animation/death/attack/sickle/rage/back/2.png"),
                             image.load("../animation/death/attack/sickle/rage/back/3.png")],

                    "front": [image.load("../animation/death/attack/sickle/rage/front/0.png"),
                              image.load("../animation/death/attack/sickle/rage/front/1.png"),
                              image.load("../animation/death/attack/sickle/rage/front/2.png"),
                              image.load("../animation/death/attack/sickle/rage/front/3.png")],

                    "left": [image.load("../animation/death/attack/sickle/rage/left/0.png"),
                             image.load("../animation/death/attack/sickle/rage/left/1.png"),
                             image.load("../animation/death/attack/sickle/rage/left/2.png"),
                             image.load("../animation/death/attack/sickle/rage/left/3.png")],

                    "right": [image.load("../animation/death/attack/sickle/rage/right/0.png"),
                              image.load("../animation/death/attack/sickle/rage/right/1.png"),
                              image.load("../animation/death/attack/sickle/rage/right/2.png"),
                              image.load("../animation/death/attack/sickle/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/attack/sickle/full/back/0.png"),
                             image.load("../animation/death/attack/sickle/full/back/1.png"),
                             image.load("../animation/death/attack/sickle/full/back/2.png"),
                             image.load("../animation/death/attack/sickle/full/back/3.png")],

                    "front": [image.load("../animation/death/attack/sickle/full/front/0.png"),
                              image.load("../animation/death/attack/sickle/full/front/1.png"),
                              image.load("../animation/death/attack/sickle/full/front/2.png"),
                              image.load("../animation/death/attack/sickle/full/front/3.png")],

                    "left": [image.load("../animation/death/attack/sickle/full/left/0.png"),
                             image.load("../animation/death/attack/sickle/full/left/1.png"),
                             image.load("../animation/death/attack/sickle/full/left/2.png"),
                             image.load("../animation/death/attack/sickle/full/left/3.png")],

                    "right": [image.load("../animation/death/attack/sickle/full/right/0.png"),
                              image.load("../animation/death/attack/sickle/full/right/1.png"),
                              image.load("../animation/death/attack/sickle/full/right/2.png"),
                              image.load("../animation/death/attack/sickle/full/right/3.png")]
                }
            },
            "wand": {
                "no": {
                    "back": [image.load("../animation/death/attack/wand/no/back/0.png"),
                             image.load("../animation/death/attack/wand/no/back/1.png"),
                             image.load("../animation/death/attack/wand/no/back/2.png"),
                             image.load("../animation/death/attack/wand/no/back/3.png")],

                    "front": [image.load("../animation/death/attack/wand/no/front/0.png"),
                              image.load("../animation/death/attack/wand/no/front/1.png"),
                              image.load("../animation/death/attack/wand/no/front/2.png"),
                              image.load("../animation/death/attack/wand/no/front/3.png")],

                    "left": [image.load("../animation/death/attack/wand/no/left/0.png"),
                             image.load("../animation/death/attack/wand/no/left/1.png"),
                             image.load("../animation/death/attack/wand/no/left/2.png"),
                             image.load("../animation/death/attack/wand/no/left/3.png")],

                    "right": [image.load("../animation/death/attack/wand/no/right/0.png"),
                              image.load("../animation/death/attack/wand/no/right/1.png"),
                              image.load("../animation/death/attack/wand/no/right/2.png"),
                              image.load("../animation/death/attack/wand/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/attack/wand/crown/back/0.png"),
                             image.load("../animation/death/attack/wand/crown/back/1.png"),
                             image.load("../animation/death/attack/wand/crown/back/2.png"),
                             image.load("../animation/death/attack/wand/crown/back/3.png")],

                    "front": [image.load("../animation/death/attack/wand/crown/front/0.png"),
                              image.load("../animation/death/attack/wand/crown/front/1.png"),
                              image.load("../animation/death/attack/wand/crown/front/2.png"),
                              image.load("../animation/death/attack/wand/crown/front/3.png")],

                    "left": [image.load("../animation/death/attack/wand/crown/left/0.png"),
                             image.load("../animation/death/attack/wand/crown/left/1.png"),
                             image.load("../animation/death/attack/wand/crown/left/2.png"),
                             image.load("../animation/death/attack/wand/crown/left/3.png")],

                    "right": [image.load("../animation/death/attack/wand/crown/right/0.png"),
                              image.load("../animation/death/attack/wand/crown/right/1.png"),
                              image.load("../animation/death/attack/wand/crown/right/2.png"),
                              image.load("../animation/death/attack/wand/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/attack/wand/rage/back/0.png"),
                             image.load("../animation/death/attack/wand/rage/back/1.png"),
                             image.load("../animation/death/attack/wand/rage/back/2.png"),
                             image.load("../animation/death/attack/wand/rage/back/3.png")],

                    "front": [image.load("../animation/death/attack/wand/rage/front/0.png"),
                              image.load("../animation/death/attack/wand/rage/front/1.png"),
                              image.load("../animation/death/attack/wand/rage/front/2.png"),
                              image.load("../animation/death/attack/wand/rage/front/3.png")],

                    "left": [image.load("../animation/death/attack/wand/rage/left/0.png"),
                             image.load("../animation/death/attack/wand/rage/left/1.png"),
                             image.load("../animation/death/attack/wand/rage/left/2.png"),
                             image.load("../animation/death/attack/wand/rage/left/3.png")],

                    "right": [image.load("../animation/death/attack/wand/rage/right/0.png"),
                              image.load("../animation/death/attack/wand/rage/right/1.png"),
                              image.load("../animation/death/attack/wand/rage/right/2.png"),
                              image.load("../animation/death/attack/wand/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/attack/wand/full/back/0.png"),
                             image.load("../animation/death/attack/wand/full/back/1.png"),
                             image.load("../animation/death/attack/wand/full/back/2.png"),
                             image.load("../animation/death/attack/wand/full/back/3.png")],

                    "front": [image.load("../animation/death/attack/wand/full/front/0.png"),
                              image.load("../animation/death/attack/wand/full/front/1.png"),
                              image.load("../animation/death/attack/wand/full/front/2.png"),
                              image.load("../animation/death/attack/wand/full/front/3.png")],

                    "left": [image.load("../animation/death/attack/wand/full/left/0.png"),
                             image.load("../animation/death/attack/wand/full/left/1.png"),
                             image.load("../animation/death/attack/wand/full/left/2.png"),
                             image.load("../animation/death/attack/wand/full/left/3.png")],

                    "right": [image.load("../animation/death/attack/wand/full/right/0.png"),
                              image.load("../animation/death/attack/wand/full/right/1.png"),
                              image.load("../animation/death/attack/wand/full/right/2.png"),
                              image.load("../animation/death/attack/wand/full/right/3.png")]
                }
            }
        },

        "move": {
            "blood": {
                "no": {
                    "back": [image.load("../animation/death/move/blood/no/back/0.png"),
                             image.load("../animation/death/move/blood/no/back/1.png"),
                             image.load("../animation/death/move/blood/no/back/2.png"),
                             image.load("../animation/death/move/blood/no/back/3.png")],

                    "front": [image.load("../animation/death/move/blood/no/front/0.png"),
                              image.load("../animation/death/move/blood/no/front/1.png"),
                              image.load("../animation/death/move/blood/no/front/2.png"),
                              image.load("../animation/death/move/blood/no/front/3.png")],

                    "left": [image.load("../animation/death/move/blood/no/left/0.png"),
                             image.load("../animation/death/move/blood/no/left/1.png"),
                             image.load("../animation/death/move/blood/no/left/2.png"),
                             image.load("../animation/death/move/blood/no/left/3.png")],

                    "right": [image.load("../animation/death/move/blood/no/right/0.png"),
                              image.load("../animation/death/move/blood/no/right/1.png"),
                              image.load("../animation/death/move/blood/no/right/2.png"),
                              image.load("../animation/death/move/blood/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/move/blood/crown/back/0.png"),
                             image.load("../animation/death/move/blood/crown/back/1.png"),
                             image.load("../animation/death/move/blood/crown/back/2.png"),
                             image.load("../animation/death/move/blood/crown/back/3.png")],

                    "front": [image.load("../animation/death/move/blood/crown/front/0.png"),
                              image.load("../animation/death/move/blood/crown/front/1.png"),
                              image.load("../animation/death/move/blood/crown/front/2.png"),
                              image.load("../animation/death/move/blood/crown/front/3.png")],

                    "left": [image.load("../animation/death/move/blood/crown/left/0.png"),
                             image.load("../animation/death/move/blood/crown/left/1.png"),
                             image.load("../animation/death/move/blood/crown/left/2.png"),
                             image.load("../animation/death/move/blood/crown/left/3.png")],

                    "right": [image.load("../animation/death/move/blood/crown/right/0.png"),
                              image.load("../animation/death/move/blood/crown/right/1.png"),
                              image.load("../animation/death/move/blood/crown/right/2.png"),
                              image.load("../animation/death/move/blood/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/move/blood/rage/back/0.png"),
                             image.load("../animation/death/move/blood/rage/back/1.png"),
                             image.load("../animation/death/move/blood/rage/back/2.png"),
                             image.load("../animation/death/move/blood/rage/back/3.png")],

                    "front": [image.load("../animation/death/move/blood/rage/back/0.png"),
                              image.load("../animation/death/move/blood/rage/back/1.png"),
                              image.load("../animation/death/move/blood/rage/back/2.png"),
                              image.load("../animation/death/move/blood/rage/back/3.png")],

                    "left": [image.load("../animation/death/move/blood/rage/left/0.png"),
                             image.load("../animation/death/move/blood/rage/left/1.png"),
                             image.load("../animation/death/move/blood/rage/left/2.png"),
                             image.load("../animation/death/move/blood/rage/left/3.png")],

                    "right": [image.load("../animation/death/move/blood/rage/right/0.png"),
                              image.load("../animation/death/move/blood/rage/right/1.png"),
                              image.load("../animation/death/move/blood/rage/right/2.png"),
                              image.load("../animation/death/move/blood/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/move/blood/full/back/0.png"),
                             image.load("../animation/death/move/blood/full/back/1.png"),
                             image.load("../animation/death/move/blood/full/back/2.png"),
                             image.load("../animation/death/move/blood/full/back/3.png")],

                    "front": [image.load("../animation/death/move/blood/full/front/0.png"),
                              image.load("../animation/death/move/blood/full/front/1.png"),
                              image.load("../animation/death/move/blood/full/front/2.png"),
                              image.load("../animation/death/move/blood/full/front/3.png")],

                    "left": [image.load("../animation/death/move/blood/full/left/0.png"),
                             image.load("../animation/death/move/blood/full/left/1.png"),
                             image.load("../animation/death/move/blood/full/left/2.png"),
                             image.load("../animation/death/move/blood/full/left/3.png")],

                    "right": [image.load("../animation/death/move/blood/full/right/0.png"),
                              image.load("../animation/death/move/blood/full/right/1.png"),
                              image.load("../animation/death/move/blood/full/right/2.png"),
                              image.load("../animation/death/move/blood/full/right/3.png")]
                }
            },
            "sickle": {
                "no": {
                    "back": [image.load("../animation/death/move/sickle/no/back/0.png"),
                             image.load("../animation/death/move/sickle/no/back/1.png"),
                             image.load("../animation/death/move/sickle/no/back/2.png"),
                             image.load("../animation/death/move/sickle/no/back/3.png")],

                    "front": [image.load("../animation/death/move/sickle/no/front/0.png"),
                              image.load("../animation/death/move/sickle/no/front/1.png"),
                              image.load("../animation/death/move/sickle/no/front/2.png"),
                              image.load("../animation/death/move/sickle/no/front/3.png")],

                    "left": [image.load("../animation/death/move/sickle/no/left/0.png"),
                             image.load("../animation/death/move/sickle/no/left/1.png"),
                             image.load("../animation/death/move/sickle/no/left/2.png"),
                             image.load("../animation/death/move/sickle/no/left/3.png")],

                    "right": [image.load("../animation/death/move/sickle/no/right/0.png"),
                              image.load("../animation/death/move/sickle/no/right/1.png"),
                              image.load("../animation/death/move/sickle/no/right/2.png"),
                              image.load("../animation/death/move/sickle/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/move/sickle/crown/back/0.png"),
                             image.load("../animation/death/move/sickle/crown/back/1.png"),
                             image.load("../animation/death/move/sickle/crown/back/2.png"),
                             image.load("../animation/death/move/sickle/crown/back/3.png")],

                    "front": [image.load("../animation/death/move/sickle/crown/front/0.png"),
                              image.load("../animation/death/move/sickle/crown/front/1.png"),
                              image.load("../animation/death/move/sickle/crown/front/2.png"),
                              image.load("../animation/death/move/sickle/crown/front/3.png")],

                    "left": [image.load("../animation/death/move/sickle/crown/left/0.png"),
                             image.load("../animation/death/move/sickle/crown/left/1.png"),
                             image.load("../animation/death/move/sickle/crown/left/2.png"),
                             image.load("../animation/death/move/sickle/crown/left/3.png")],

                    "right": [image.load("../animation/death/move/sickle/crown/right/0.png"),
                              image.load("../animation/death/move/sickle/crown/right/1.png"),
                              image.load("../animation/death/move/sickle/crown/right/2.png"),
                              image.load("../animation/death/move/sickle/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/move/sickle/rage/back/0.png"),
                             image.load("../animation/death/move/sickle/rage/back/1.png"),
                             image.load("../animation/death/move/sickle/rage/back/2.png"),
                             image.load("../animation/death/move/sickle/rage/back/3.png")],

                    "front": [image.load("../animation/death/move/sickle/rage/front/0.png"),
                              image.load("../animation/death/move/sickle/rage/front/1.png"),
                              image.load("../animation/death/move/sickle/rage/front/2.png"),
                              image.load("../animation/death/move/sickle/rage/front/3.png")],

                    "left": [image.load("../animation/death/move/sickle/rage/left/0.png"),
                             image.load("../animation/death/move/sickle/rage/left/1.png"),
                             image.load("../animation/death/move/sickle/rage/left/2.png"),
                             image.load("../animation/death/move/sickle/rage/left/3.png")],

                    "right": [image.load("../animation/death/move/sickle/rage/right/0.png"),
                              image.load("../animation/death/move/sickle/rage/right/1.png"),
                              image.load("../animation/death/move/sickle/rage/right/2.png"),
                              image.load("../animation/death/move/sickle/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/move/sickle/full/back/0.png"),
                             image.load("../animation/death/move/sickle/full/back/1.png"),
                             image.load("../animation/death/move/sickle/full/back/2.png"),
                             image.load("../animation/death/move/sickle/full/back/3.png")],

                    "front": [image.load("../animation/death/move/sickle/full/front/0.png"),
                              image.load("../animation/death/move/sickle/full/front/1.png"),
                              image.load("../animation/death/move/sickle/full/front/2.png"),
                              image.load("../animation/death/move/sickle/full/front/3.png")],

                    "left": [image.load("../animation/death/move/sickle/full/left/0.png"),
                             image.load("../animation/death/move/sickle/full/left/1.png"),
                             image.load("../animation/death/move/sickle/full/left/2.png"),
                             image.load("../animation/death/move/sickle/full/left/3.png")],

                    "right": [image.load("../animation/death/move/sickle/full/right/0.png"),
                              image.load("../animation/death/move/sickle/full/right/1.png"),
                              image.load("../animation/death/move/sickle/full/right/2.png"),
                              image.load("../animation/death/move/sickle/full/right/3.png")]
                }
            },
            "wand": {
                "no": {
                    "back": [image.load("../animation/death/move/wand/no/back/0.png"),
                             image.load("../animation/death/move/wand/no/back/1.png"),
                             image.load("../animation/death/move/wand/no/back/2.png"),
                             image.load("../animation/death/move/wand/no/back/3.png")],

                    "front": [image.load("../animation/death/move/wand/no/front/0.png"),
                              image.load("../animation/death/move/wand/no/front/1.png"),
                              image.load("../animation/death/move/wand/no/front/2.png"),
                              image.load("../animation/death/move/wand/no/front/3.png")],

                    "left": [image.load("../animation/death/move/wand/no/left/0.png"),
                             image.load("../animation/death/move/wand/no/left/1.png"),
                             image.load("../animation/death/move/wand/no/left/2.png"),
                             image.load("../animation/death/move/wand/no/left/3.png")],

                    "right": [image.load("../animation/death/move/wand/no/right/0.png"),
                              image.load("../animation/death/move/wand/no/right/1.png"),
                              image.load("../animation/death/move/wand/no/right/2.png"),
                              image.load("../animation/death/move/wand/no/right/3.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/move/wand/crown/back/0.png"),
                             image.load("../animation/death/move/wand/crown/back/1.png"),
                             image.load("../animation/death/move/wand/crown/back/2.png"),
                             image.load("../animation/death/move/wand/crown/back/3.png")],

                    "front": [image.load("../animation/death/move/wand/crown/front/0.png"),
                              image.load("../animation/death/move/wand/crown/front/1.png"),
                              image.load("../animation/death/move/wand/crown/front/2.png"),
                              image.load("../animation/death/move/wand/crown/front/3.png")],

                    "left": [image.load("../animation/death/move/wand/crown/left/0.png"),
                             image.load("../animation/death/move/wand/crown/left/1.png"),
                             image.load("../animation/death/move/wand/crown/left/2.png"),
                             image.load("../animation/death/move/wand/crown/left/3.png")],

                    "right": [image.load("../animation/death/move/wand/crown/right/0.png"),
                              image.load("../animation/death/move/wand/crown/right/1.png"),
                              image.load("../animation/death/move/wand/crown/right/2.png"),
                              image.load("../animation/death/move/wand/crown/right/3.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/move/wand/rage/back/0.png"),
                             image.load("../animation/death/move/wand/rage/back/1.png"),
                             image.load("../animation/death/move/wand/rage/back/2.png"),
                             image.load("../animation/death/move/wand/rage/back/3.png")],

                    "front": [image.load("../animation/death/move/wand/rage/front/0.png"),
                              image.load("../animation/death/move/wand/rage/front/1.png"),
                              image.load("../animation/death/move/wand/rage/front/2.png"),
                              image.load("../animation/death/move/wand/rage/front/3.png")],

                    "left": [image.load("../animation/death/move/wand/rage/left/0.png"),
                             image.load("../animation/death/move/wand/rage/left/1.png"),
                             image.load("../animation/death/move/wand/rage/left/2.png"),
                             image.load("../animation/death/move/wand/rage/left/3.png")],

                    "right": [image.load("../animation/death/move/wand/rage/right/0.png"),
                              image.load("../animation/death/move/wand/rage/right/1.png"),
                              image.load("../animation/death/move/wand/rage/right/2.png"),
                              image.load("../animation/death/move/wand/rage/right/3.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/move/wand/full/back/0.png"),
                             image.load("../animation/death/attack/wand/full/back/1.png"),
                             image.load("../animation/death/attack/wand/full/back/2.png"),
                             image.load("../animation/death/attack/wand/full/back/3.png")],

                    "front": [image.load("../animation/death/move/wand/full/front/0.png"),
                              image.load("../animation/death/move/wand/full/front/1.png"),
                              image.load("../animation/death/move/wand/full/front/2.png"),
                              image.load("../animation/death/move/wand/full/front/3.png")],

                    "left": [image.load("../animation/death/move/wand/full/left/0.png"),
                             image.load("../animation/death/move/wand/full/left/1.png"),
                             image.load("../animation/death/move/wand/full/left/2.png"),
                             image.load("../animation/death/move/wand/full/left/3.png")],

                    "right": [image.load("../animation/death/move/wand/full/right/0.png"),
                              image.load("../animation/death/move/wand/full/right/1.png"),
                              image.load("../animation/death/move/wand/full/right/2.png"),
                              image.load("../animation/death/move/wand/full/right/3.png")]
                }
            }
        },

        "idle": {
            "blood": {
                "no": {
                    "back": [image.load("../animation/death/idle/blood/no/back/idle.png")],
                    "front": [image.load("../animation/death/idle/blood/no/front/idle.png")],
                    "left": [image.load("../animation/death/idle/blood/no/left/idle.png")],
                    "right": [image.load("../animation/death/idle/blood/no/right/idle.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/idle/blood/crown/back/idle.png")],
                    "front": [image.load("../animation/death/idle/blood/crown/front/idle.png")],
                    "left": [image.load("../animation/death/idle/blood/crown/left/idle.png")],
                    "right": [image.load("../animation/death/idle/blood/crown/right/idle.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/idle/blood/rage/back/idle.png")],
                    "front": [image.load("../animation/death/idle/blood/rage/front/idle.png")],
                    "left": [image.load("../animation/death/idle/blood/rage/left/idle.png")],
                    "right": [image.load("../animation/death/idle/blood/rage/right/idle.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/idle/blood/full/back/idle.png")],
                    "front": [image.load("../animation/death/idle/blood/full/front/idle.png")],
                    "left": [image.load("../animation/death/idle/blood/full/left/idle.png")],
                    "right": [image.load("../animation/death/idle/blood/full/right/idle.png")]
                }
            },
            "sickle": {
                "no": {
                    "back": [image.load("../animation/death/idle/sickle/no/back/idle.png")],
                    "front": [image.load("../animation/death/idle/sickle/no/front/idle.png")],
                    "left": [image.load("../animation/death/idle/sickle/no/left/idle.png")],
                    "right": [image.load("../animation/death/idle/sickle/no/right/idle.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/idle/sickle/crown/back/idle.png")],
                    "front": [image.load("../animation/death/idle/sickle/crown/front/idle.png")],
                    "left": [image.load("../animation/death/idle/sickle/crown/left/idle.png")],
                    "right": [image.load("../animation/death/idle/sickle/crown/right/idle.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/idle/sickle/rage/back/idle.png")],
                    "front": [image.load("../animation/death/idle/sickle/rage/front/idle.png")],
                    "left": [image.load("../animation/death/idle/sickle/rage/left/idle.png")],
                    "right": [image.load("../animation/death/idle/sickle/rage/right/idle.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/idle/sickle/full/back/idle.png")],
                    "front": [image.load("../animation/death/idle/sickle/full/front/idle.png")],
                    "left": [image.load("../animation/death/idle/sickle/full/left/idle.png")],
                    "right": [image.load("../animation/death/idle/sickle/full/right/idle.png")]
                }
            },
            "wand": {
                "no": {
                    "back": [image.load("../animation/death/idle/wand/no/back/idle.png")],
                    "front": [image.load("../animation/death/idle/wand/no/front/idle.png")],
                    "left": [image.load("../animation/death/idle/wand/no/left/idle.png")],
                    "right": [image.load("../animation/death/idle/wand/no/right/idle.png")]
                },
                "crown": {
                    "back": [image.load("../animation/death/idle/wand/crown/back/idle.png")],
                    "front": [image.load("../animation/death/idle/wand/crown/front/idle.png")],
                    "left": [image.load("../animation/death/idle/wand/crown/left/idle.png")],
                    "right": [image.load("../animation/death/idle/wand/crown/right/idle.png")]
                },
                "rage": {
                    "back": [image.load("../animation/death/idle/wand/rage/back/idle.png")],
                    "front": [image.load("../animation/death/idle/wand/rage/front/idle.png")],
                    "left": [image.load("../animation/death/idle/wand/rage/left/idle.png")],
                    "right": [image.load("../animation/death/idle/wand/rage/right/idle.png")]
                },
                "full": {
                    "back": [image.load("../animation/death/idle/wand/full/back/idle.png")],
                    "front": [image.load("../animation/death/idle/wand/full/front/idle.png")],
                    "left": [image.load("../animation/death/idle/wand/full/left/idle.png")],
                    "right": [image.load("../animation/death/idle/wand/full/right/idle.png")]
                }
            }
        },

        "tp_in": [image.load("../animation/death/tp_in/0.png"),
                  image.load("../animation/death/tp_in/1.png"),
                  image.load("../animation/death/tp_in/2.png"),
                  image.load("../animation/death/tp_in/3.png")],
        "tp_out": [image.load("../animation/death/tp_out/0.png"),
                   image.load("../animation/death/tp_out/1.png"),
                   image.load("../animation/death/tp_out/2.png"),
                   image.load("../animation/death/tp_out/3.png")],
        "damage": [image.load("../animation/death/damage/0.png"),
                   image.load("../animation/death/damage/1.png"),
                   image.load("../animation/death/damage/2.png"),
                   image.load("../animation/death/damage/3.png")]
    },

    "bug": {
        "attack": [image.load("../animation/bug/attack/0.png"),
                   image.load("../animation/bug/attack/1.png"),
                   image.load("../animation/bug/attack/2.png"),
                   image.load("../animation/bug/attack/3.png")],
        "move": [image.load("../animation/bug/move/0.png"),
                 image.load("../animation/bug/move/1.png"),
                 image.load("../animation/bug/move/2.png"),
                 image.load("../animation/bug/move/3.png")],
        "idle": [image.load("../animation/bug/idle.png")],
        "damage": [image.load("../animation/bug/damage/0.png"),
                   image.load("../animation/bug/damage/1.png"),
                   image.load("../animation/bug/damage/2.png"),
                   image.load("../animation/bug/damage/3.png")]
    },
    "rat": {
        "attack": [image.load("../animation/rat/attack/0.png"),
                   image.load("../animation/rat/attack/1.png"),
                   image.load("../animation/rat/attack/2.png"),
                   image.load("../animation/rat/attack/3.png")],
        "move": [image.load("../animation/rat/move/0.png"),
                 image.load("../animation/rat/move/1.png"),
                 image.load("../animation/rat/move/2.png"),
                 image.load("../animation/rat/move/3.png")],
        "idle": [image.load("../animation/rat/idle.png")],
        "damage": [image.load("../animation/rat/damage/0.png"),
                   image.load("../animation/rat/damage/1.png"),
                   image.load("../animation/rat/damage/2.png"),
                   image.load("../animation/rat/damage/3.png")]},
    "bat": {
        "attack": [image.load("../animation/bat/attack/0.png"),
                   image.load("../animation/bat/attack/1.png"),
                   image.load("../animation/bat/attack/2.png"),
                   image.load("../animation/bat/attack/3.png")],
        "move": [image.load("../animation/bat/move/0.png"),
                 image.load("../animation/bat/move/1.png"),
                 image.load("../animation/bat/move/2.png"),
                 image.load("../animation/bat/move/3.png")],
        "idle": [image.load("../animation/bat/idle.png")],
        "damage": [image.load("../animation/bat/damage/0.png"),
                   image.load("../animation/bat/damage/1.png"),
                   image.load("../animation/bat/damage/2.png"),
                   image.load("../animation/bat/damage/3.png")]},
    "slime": {
        "attack": [image.load("../animation/slime/attack/0.png"),
                   image.load("../animation/slime/attack/1.png"),
                   image.load("../animation/slime/attack/2.png"),
                   image.load("../animation/slime/attack/3.png")],
        "move": [image.load("../animation/slime/move/0.png"),
                 image.load("../animation/slime/move/1.png"),
                 image.load("../animation/slime/move/2.png"),
                 image.load("../animation/slime/move/3.png")],
        "idle": [image.load("../animation/slime/idle.png")],
        "damage": [image.load("../animation/slime/damage/0.png"),
                   image.load("../animation/slime/damage/1.png"),
                   image.load("../animation/slime/damage/2.png"),
                   image.load("../animation/slime/damage/3.png")],
        "split": [image.load("../animation/slime/split/0.png"),
                  image.load("../animation/slime/split/1.png"),
                  image.load("../animation/slime/split/2.png"),
                  image.load("../animation/slime/split/3.png")]
    },

    "plague": [image.load("../animation/plague/idle.png")],
    "war": {
        "move": [image.load("../animation/war/move/0.png"),
                 image.load("../animation/war/move/1.png"),
                 image.load("../animation/war/move/2.png"),
                 image.load("../animation/war/move/3.png")],
        "idle": [image.load("../animation/war/idle.png")]
    },
    "starve": {
        "idle": [image.load("../animation/starve/idle.png")],
        "move": {
            "back": [image.load("../animation/starve/move/back.png")],
            "front": [image.load("../animation/starve/move/front.png")],
            "left": [image.load("../animation/starve/move/left.png")],
            "right": [image.load("../animation/starve/move/right.png")]
        }
    },
    "cerberus": {
        "idle": {
            1: [image.load("../animation/cerberus/idle/1/idle.png")],
            2: [image.load("../animation/cerberus/idle/2/idle.png")],
            3: [image.load("../animation/cerberus/idle/3/idle.png")],
            4: [image.load("../animation/cerberus/idle/4/idle.png")],
            5: [image.load("../animation/cerberus/idle/5/idle.png")]
        },
        "attack": {
            1: [image.load("../animation/cerberus/attack/1/idle.png")],
            2: [image.load("../animation/cerberus/attack/2/idle.png")],
            3: [image.load("../animation/cerberus/attack/3/idle.png")],
            4: [image.load("../animation/cerberus/attack/4/idle.png")],
            5: [image.load("../animation/cerberus/attack/5/idle.png")]
        }
    },
    "apocalypse": {
        "idle": [image.load("../animation/apocalypse/idle.png")],
        "attack": [image.load("../animation/apocalypse/attack.png")]
    }
}
