from .erd_washtemp_level import ErdWashTempLevel
from .washtemp_level import WashTempLevel

WASHTEMP_LEVEL_MAP = {
    ErdWashTempLevel.TAP_COLD_1: WashTempLevel.TAP_COLD,
    ErdWashTempLevel.COLD_1: WashTempLevel.COLD,
    ErdWashTempLevel.WARM_1: WashTempLevel.WARM,
    ErdWashTempLevel.HOT_1: WashTempLevel.HOT,
    ErdWashTempLevel.EXTRAHOT__1: WashTempLevel.EXTRA_HOT,
    ErdWashTempLevel.INVALID: WashTempLevel.DASH,
    ErdWashTempLevel.TAP_COLD_2: WashTempLevel.TAP_COLD,
    ErdWashTempLevel.COLD_2: WashTempLevel.COLD,
    ErdWashTempLevel.COOL_2: WashTempLevel.COOL,
    ErdWashTempLevel.COLORS_2: WashTempLevel.COLORS,
    ErdWashTempLevel.WARM_2: WashTempLevel.WARM,
    ErdWashTempLevel.HOT_2: WashTempLevel.HOT,
    ErdWashTempLevel.EXTRA_HOT_2: WashTempLevel.EXTRA_HOT
}
