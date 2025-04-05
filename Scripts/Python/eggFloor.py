# -*- coding: utf-8 -*-
# Python/fun/mystitech/eggFloor.py

"""
Module: eggFloor.py
Age: Kirel
Date: September 2015
Description:
    Merge in Jalak. Create a solid floor in the inner chamber of the Kirel meditation room
    using columns from Jalak. Then disable the walls so we can walk to the egg.
"""

from Plasma import (
    PtConsoleNet,
    PtFindSceneobject,
    ptMatrix44,
    PtSetAlarm
)

buildFloor = 0
disableWalls = 1

matrices = (
    ((-0.17084169387817383, 0.0, 0.9853301048278809, 488.4134216308594), (0.9853301048278809, 7.467727769494559e-09, 0.17084169387817383, -780.8757934570312), (0.0, 1.0, -4.371138828673793e-08, 4.878429412841797), (0.0, 0.0, 0.0, 1.0)),
    ((-0.17084169387817383, 0.0, 0.9853301048278809, 487.3757629394531), (0.9853301048278809, 7.467727769494559e-09, 0.17084169387817383, -774.8906860351562), (0.0, 1.0, -4.371138828673793e-08, 4.878429412841797), (0.0, 0.0, 0.0, 1.0)),
    ((-0.8888121843338013, -0.45834362506866455, 0.0, 525.871337890625), (0.45834362506866455, -0.8888121843338013, 0.0, -777.9674072265625), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((-0.9125127792358398, 0.4091287851333618, 0.0, 533.244873046875), (-0.4091287851333618, -0.9125127792358398, 0.0, -778.1688232421875), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((-0.24907264113426208, 0.968518853187561, 0.0, 537.9996948242188), (-0.968518853187561, -0.24907264113426208, 0.0, -772.5296020507812), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((0.6019241213798523, 0.79859459400177, 0.0, 536.5552978515625), (-0.79859459400177, 0.6019241213798523, 0.0, -765.296142578125), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((0.9996600151062012, 0.027312040328979492, 0.0, 529.9994506835938), (-0.027312040328979492, 0.9996600151062012, 0.0, -761.9153442382812), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((0.6446309089660645, -0.7645370960235596, 0.0, 523.2687377929688), (0.7645370960235596, 0.6446309089660645, 0.0, -764.93310546875), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((-0.19581758975982666, -0.9806739687919617, 0.0, 521.4315185546875), (0.9806739687919617, -0.19581758975982666, 0.0, -772.076904296875), (0.0, 0.0, 1.0, -18.961185455322266), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 493.52239990234375), (0.0, -0.18998122215270996, 0.9817876815795898, -776.3823852539062), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 499.92364501953125), (0.0, -0.18998122215270996, 0.9817876815795898, -775.1437377929688), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 506.32489013671875), (0.0, -0.18998122215270996, 0.9817876815795898, -773.9050903320312), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((1.0, 0.0, 0.0, 0.027889251709), (0.0, 1.0, 0.0, 0.0982389450073), (0.0, 0.0, 1.0, -29.6211242676), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 512.7261352539062), (0.0, -0.18998122215270996, 0.9817876815795898, -772.6664428710938), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 519.1273803710938), (0.0, -0.18998122215270996, 0.9817876815795898, -771.4277954101562), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 525.5286254882812), (0.0, -0.18998122215270996, 0.9817876815795898, -770.1891479492188), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 531.9298706054688), (0.0, -0.18998122215270996, 0.9817876815795898, -768.9505004882812), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 538.3311157226562), (0.0, -0.18998122215270996, 0.9817876815795898, -767.7118530273438), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 544.7323608398438), (0.0, -0.18998122215270996, 0.9817876815795898, -766.4732055664062), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 551.1336059570312), (0.0, -0.18998122215270996, 0.9817876815795898, -765.2345581054688), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 557.5348510742188), (0.0, -0.18998122215270996, 0.9817876815795898, -763.9959106445312), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 563.9360961914062), (0.0, -0.18998122215270996, 0.9817876815795898, -762.7572631835938), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((8.304342991038993e-09, -0.9817876815795898, -0.18998122215270996, 570.3373413085938), (0.0, -0.18998122215270996, 0.9817876815795898, -761.5186157226562), (-1.0, 0.0, -4.371138828673793e-08, 4.888424873352051), (0.0, 0.0, 0.0, 1.0)),
    ((-0.2010056972503662, 0.0, 0.9795899987220764, 523.7905883789062), (0.9795899987220764, 8.786238403502011e-09, 0.2010056972503662, -736.254638671875), (0.0, 1.0, -4.371138828673793e-08, 4.8884382247924805), (0.0, 0.0, 0.0, 1.0)),
    ((-0.2010056972503662, 0.0, 0.9795899987220764, 532.1405029296875), (0.9795899987220764, 8.786238403502011e-09, 0.2010056972503662, -802.6123657226562), (0.0, 1.0, -4.371138828673793e-08, 4.8884382247924805), (0.0, 0.0, 0.0, 1.0)),
)

# Merge in Jalak.
# Create a solid floor in the inner chamber of the Kirel meditation room using columns from Jalak.
# Then disable the walls so we can walk to the egg.
def RunMe():
    PtSetAlarm(4, __Callback(), buildFloor)
    PtSetAlarm(6, __Callback(), disableWalls)
    PtConsoleNet('Nav.PageInNode jlakArena', True)

class __Callback:
    def onAlarm(self, context):
        if context == buildFloor:
           for i in range(len(matrices)):
                m = ptMatrix44()
                m.setData(matrices[i])
                p = PtFindSceneobject('columnPhys_%02d' % i, 'Jalak').physics
                p.netForce(True)
                p.warp(m)
                if i != 12:
                    d = PtFindSceneobject('column_%02d' % i, 'Jalak').draw
                    d.netForce(True)
                    d.enable(False)
        elif context == disableWalls:
            p = PtFindSceneobject('prvtrm1CameraBlocker', 'Neighborhood02').physics
            p.netForce(True)
            p.enable(False)
