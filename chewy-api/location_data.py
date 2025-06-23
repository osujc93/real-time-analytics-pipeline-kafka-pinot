import random
from uszipcode import SearchEngine

class USZipcodeLocationData:
    """
    Provides ZIP/city/state from uszipcode, then merges a simple dictionary
    of state -> possible area codes for phone number generation.
    """

    STATE_AREA_CODES = {
        "AL": [205, 251, 256, 334, 938],
        "AK": [907],
        "AZ": [480, 520, 602, 623, 928],
        "AR": [479, 501, 870],
        "CA": [209, 213, 279, 310, 323, 341, 369, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 628, 650, 657, 661, 669, 707, 714, 747, 752, 760, 805, 818, 820, 831, 840, 858, 909, 916, 925, 949, 951],
        "CO": [303, 719, 970],
        "CT": [203, 475, 860],
        "DE": [302],
        "FL": [239, 305, 321, 352, 386, 407, 448, 561, 627, 652, 689, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954],
        "GA": [229, 404, 470, 478, 678, 706, 762, 770],
        "HI": [808],
        "ID": [208, 986],
        "IL": [217, 224, 309, 312, 331, 447, 464, 618, 630, 708, 730, 773, 779, 815, 847, 872],
        "IN": [219, 260, 317, 574, 765, 812],
        "IA": [319, 515, 563, 641, 712],
        "KS": [316, 620, 785, 913],
        "KY": [270, 364, 502, 606, 859],
        "LA": [225, 318, 337, 504, 985],
        "ME": [207],
        "MD": [240, 301, 410, 443, 667],
        "MA": [339, 351, 413, 508, 617, 774, 781, 857, 978],
        "MI": [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989],
        "MN": [218, 320, 507, 612, 651, 763, 952],
        "MS": [228, 601, 662, 769],
        "MO": [314, 417, 573, 636, 660, 816],
        "MT": [406],
        "NE": [308, 402, 531],
        "NV": [702, 725, 775],
        "NH": [603],
        "NJ": [201, 551, 609, 732, 848, 856, 862, 908, 973],
        "NM": [505, 575],
        "NY": [212, 315, 332, 347, 516, 518, 585, 607, 631, 646, 680, 716, 718, 838, 845, 914, 917, 929, 934],
        "NC": [252, 336, 704, 828, 910, 919, 980, 984],
        "ND": [701],
        "OH": [216, 234, 330, 419, 440, 513, 567, 614, 740, 937],
        "OK": [405, 539, 580, 918],
        "OR": [458, 503, 541, 971],
        "PA": [215, 267, 272, 412, 484, 570, 610, 717, 724, 814, 878],
        "RI": [401],
        "SC": [803, 843, 854, 864],
        "SD": [605],
        "TN": [423, 615, 629, 731, 865, 901, 931],
        "TX": [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 726, 737, 806, 817, 830, 832, 903, 915, 936, 940, 945, 956, 972, 979],
        "UT": [385, 435, 801],
        "VT": [802],
        "VA": [276, 434, 540, 571, 703, 757, 804],
        "WA": [206, 253, 360, 425, 509],
        "WV": [304, 681],
        "WI": [262, 414, 534, 608, 715, 920],
        "WY": [307]
    }

    _initialized = False
    _all_zips = []

    @classmethod
    def init_uszipcode_data(cls):
        """Load ZIP records from a local DB (bundled with uszipcode)."""
        if cls._initialized:
            return
        search = SearchEngine(simple_zipcode=True)
        cls._all_zips = search.by_population(lower=0, upper=999999999, returns=50000)
        random.shuffle(cls._all_zips)
        cls._initialized = True

    @classmethod
    def get_random_location(cls):
        """
        Returns (city, state, zipcode, area_code).
        Area code is picked from the state dict, or 999 if none found.
        """
        if not cls._initialized or not cls._all_zips:
            raise RuntimeError("Location data not initialized. Call init_uszipcode_data() first.")

        z = random.choice(cls._all_zips)
        city = z.major_city
        state = z.state
        zipcode = z.zipcode

        possible_codes = cls.STATE_AREA_CODES.get(state, [999])
        area_code = random.choice(possible_codes)

        return city, state, zipcode, area_code
