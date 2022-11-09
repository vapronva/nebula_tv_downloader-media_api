from enum import Enum


class VideoNebulaAttributes(str, Enum):
    IS_NEBULA_ORIGINAL = "is_nebula_original"
    IS_NEBULA_PLUS = "is_nebula_plus"
    IS_NEBULA_FIRST = "is_nebula_first"
    FREE_SAMPLE_ELIGIBLE = "free_sample_eligible"
